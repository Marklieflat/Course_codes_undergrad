*** This is the coding solution for Project 2 Case 1 Q1 (FIN 3080) ***

** This script constructs and tests size-based portfolios. Figures are plotted with case2_fig_plotting.R **

*** 0. Set program options and specify raw data path ***

set more off  // Set this option off to enable consecutive screen outputs
set excelxlsxlargefile on // Set this option on to enable Stata to import large excel files

* Change the following path to your own path to raw data * 
global path_to_data ="/Users/sjwang222/Desktop/FIN3080/Solution/project2/data_code"

*** 1. Load & clean stock return data ***

* Import stock return data *

import delimited $path_to_data/case2_raw_stock_return.csv, stringcols(_all) encoding(UTF-8)  clear 
//save $path_to_data/case1_raw_stock_return, replace
//use $path_to_data/case1_raw_stock_return, clear

* Convert original dates to Year-Month format *
gen year_mon = monthly(trdmnt, "YM")
format year_mon %tm


* Rename variables of interest *
rename mretnd stock_ret
rename stkcd stock_code
rename markettype market
rename msmvttl market_cap

* Keep mainboard stocks only *
keep if market == "1" |market == "4"

* Destring variables and save processed data *
destring stock_ret, replace
destring market_cap, replace
save $path_to_data/case2_processed_stock_return, replace


*** 2. Load market return data *** 

import delimited $path_to_data/case2_raw_market_return.csv, stringcols(_all) encoding(UTF-8)  clear 
//save $path_to_data/case2_raw_market_return, replace
//use $path_to_data/case2_raw_market_return, clear

* Keep SZ-SH Aggregated market return only*
keep if markettype == "5"

* Convert original dates to Year-Month format *
gen year_mon = monthly(trdmnt, "YM")
format year_mon %tm


* Rename and desting vars *
rename cmretmdos market_ret
destring market_ret, replace
rename markettype market

drop if year_mon == . | market_ret == .


* Save processed market return data *
keep year_mon market_ret
save $path_to_data/case2_processed_market_return, replace


*** 3. Load risk-free data ***

** Same procedures as in case1_1.do **
import delimited $path_to_data/case2_raw_risk_free.csv, stringcols(_all) encoding(UTF-8)  clear 

gen date = date(clsdt,"YMD")
format date %td

gen year_mon = ym(year(date), month(date))
format year_mon %tm

rename nrrmtdt risk_free
destring risk_free, replace
replace risk_free = risk_free/100

bys year_mon: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

keep year_mon risk_free
save $path_to_data/case2_processed_risk_free_rate, replace



*** 4. Merge market return and risk free rate data to individual stock return data ***

** Same as in case1_1.do **
use $path_to_data/case2_processed_stock_return, clear

merge m:1 year_mon using $path_to_data/case2_processed_market_return
keep if _merge == 3
drop _merge

merge m:1 year_mon using $path_to_data/case2_processed_risk_free_rate
keep if _merge == 3
drop _merge

save $path_to_data/case2_merged_stock_return, replace

*** 5. Form long-short portfolio using market cap ***

* Load merged data *
use $path_to_data/case2_merged_stock_return, clear

* Claim the data as panel *
egen stock_id = group(stock_code)
xtset stock_id year_mon

* Generate lagged market cap *
gen l_market_cap = l.market_cap
drop if l_market_cap == .

* Generate market cap quantiles *
bys year_mon: egen cap_quantile = xtile(l_market_cap), p(10(10)90)

** Calculate equal-weighted and value-weighted monthly returns **

* Calculate equal-weighted mean monthly return for Q10 and Q1 portfolios *

forvalue i = 1/10{
	bys year_mon: egen equal_ret_cap_q`i' = mean(cond(cap_quantile == `i', stock_ret, .))
}
//bys year_mon: egen equal_ret_cap_q10 = mean(cond(cap_quantile == 10, stock_ret, .))
//bys year_mon: egen equal_ret_cap_q1 = mean(cond(cap_quantile == 1, stock_ret, .))

* Calculate the difference between returns of q10 and q1 *
gen equal_ret_cap_q1_q10 = equal_ret_cap_q1 - equal_ret_cap_q10


* Calculate value-weighted mean montly return for Q10 and Q1 portfolios *
gen ret_cap = stock_ret * l_market_cap

forvalue j = 1/10{
bys year_mon: egen total_ret_cap_q`j' = total(cond(cap_quantile == `j',ret_cap, .))
bys year_mon: egen total_market_cap_q`j' = total(cond(cap_quantile==`j', l_market_cap, .))
gen value_ret_cap_q`j' = total_ret_cap_q`j'/total_market_cap_q`j'
}

/*
bys year_mon: egen total_ret_cap_q10 = total(cond(cap_quantile == 10,ret_cap, .))
bys year_mon: egen total_ret_cap_q1 = total(cond(cap_quantile == 1,ret_cap, .))
bys year_mon: egen total_market_cap_q10 = total(cond(cap_quantile==10, l_market_cap, .))
bys year_mon: egen total_market_cap_q1 = total(cond(cap_quantile==1, l_market_cap, .))
gen value_ret_cap_q10 = total_ret_cap_q10/total_market_cap_q10
gen value_ret_cap_q1 = total_ret_cap_q1/total_market_cap_q1
*/

* Calculate the difference between returns of q10 and q1 *
gen value_ret_cap_q1_q10 = value_ret_cap_q1 -  value_ret_cap_q10

save $path_to_data/case2_q1_data_for_regression, replace

* Calculate monthly within-group returns and save data for plotting with R *
bys year_mon cap_quantile: egen ew_monthly_ret_cap = mean(stock_ret)
bys year_mon cap_quantile: egen total_ret_cap = total(ret_cap)
bys year_mon cap_quantile: egen total_market_cap = total(l_market_cap)
gen vw_monthly_ret_cap = total_ret_cap/total_market_cap

bys cap_quantile: egen ew_ret = mean(ew_monthly_ret_cap)
bys cap_quantile: egen vw_ret = mean(vw_monthly_ret_cap)
bys cap_quantile: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

gen year = year(dofm(year_mon))
gen month = month(dofm(year_mon))
gen date = mdy(month,1,year)
format date %td
rename cap_quantile group

keep date group ew_ret vw_ret

save $path_to_data/case2_q1_data_for_plotting, replace



* Go back to previous data set data zip data to monthly time-series *
use $path_to_data/case2_q1_data_for_regression, clear

bys year_mon: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup


*** 3. Evaluate portfolio mean return ***

est clear
forvalue k=1/10{
	eststo: reg equal_ret_cap_q`k'
		estimates store f`k'
}
eststo: reg equal_ret_cap_q1_q10
	estimates store f11
	
esttab f* using $path_to_data/case2_q1_mean.tex, label stats(r2 N, fmt(3 0) labels(`"\(R^{2}\)"' `"Observations"')) compress t nogap b(%6.3f) noomitted drop ( ) star(* 0.1 ** 0.05 *** 0.01)  nonote  title() obslast replace




*** 4. Evaluate the CAPM Alpha ***

* Generate CAPM-related elements *
rename market_ret r_m
rename risk_free r_f
gen rm_rf = r_m - r_f

* Test the CAPM alpha for equal-weighted monthly returns * 
gen ew_cap_q1q10_rf = equal_ret_cap_q1_q10 - r_f


est clear
forvalue k=1/10{
	gen ew_cap_q`k'_rf = equal_ret_cap_q`k' - r_f
	eststo: reg ew_cap_q`k'_rf rm_rf
		estimates store f`k'
}


eststo: reg equal_ret_cap_q1_q10 rm_rf
	estimates store f11

/*
* Refine the regression with Newey-west standard errors *
tsset year_mon
eststo: newey equal_ret_cap_q1_q10 rm_rf , lag(12)
	estimates store f4


* Test the CAPM alpha for value-weighted monthly returns * 
gen vw_cap_q1q10_rf = value_ret_cap_q1_q10 - r_f
gen vw_cap_q1_rf = value_ret_cap_q1 - r_f
gen vw_cap_q10_rf = value_ret_cap_q10 - r_f

eststo: reg vw_cap_q1_rf rm_rf
	estimates store f5
eststo: reg vw_cap_q10_rf rm_rf
	estimates store f6
eststo: reg value_ret_cap_q1_q10 rm_rf
	estimates store f7

* Refine the regression with Newey-west standard errors *
eststo: newey value_ret_cap_q1_q10 rm_rf , lag(12)
	estimates store f8

*/
esttab f* using $path_to_data/case2_q1_capm.tex, label stats(r2 N, fmt(3 0) labels(`"\(R^{2}\)"' `"Observations"')) compress t nogap b(%6.3f) noomitted drop ( ) star(* 0.1 ** 0.05 *** 0.01)  nonote  title() obslast replace


