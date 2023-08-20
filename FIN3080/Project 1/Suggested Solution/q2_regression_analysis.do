*** This is the coding solutions for question 2 of project 1 (FIN 3080) ***

** This script constructs beta, ROE, and std of past-6-month returns and justifies their effects on PB ratio with firm-month panel regressions **

** Remark: this script requires 'rangestat' and 'reghdfe' packages. You may uncomment the following two lines to install them first (if not installed before). **

// ssc install rangestat
// ssc install reghdfe

*** 0. Set options and raw data path ***

set more off  // Set this option off to enable consecutive screen outputs
set excelxlsxlargefile on // Set this option on to enable Stata to import large excel files
* Change the following path to your own path to raw data *
global path_to_data ="/Users/sjwang222/Desktop/FIN3080/Solution/project1/codes" 


*** 1. Load and merge market beta into this data set ***
* Import raw beta data *
import excel $path_to_data/monthly_beta.xlsx, firstrow clear
save $path_to_data/raw_monthly_beta, replace
//use $path_to_data/raw_monthly_beta, clear



* Format date *
gen market_date = date(TradingMonth, "YM")
format market_date %td
gen market_mon = mofd(market_date)


* Rename necessary variables *
rename StockCode stock_code
rename MonthlyBetaValueofComposite beta


* Drop duplicated records *
bysort stock_code market_date: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

* Output results *
keep stock_code market_date beta
save $path_to_data/monthly_beta, replace

* Merge beta to the previous data set *
use $path_to_data/market_with_fundamental, clear
merge 1:1 stock_code market_date using $path_to_data/monthly_beta
drop if _merge == 2
drop _merge
save $path_to_data/market_with_fundamental, replace


*** 2. Construct variables of interest ***
gen roe = net_profit_past_4q/total_shareholder_equity
gen market_mon = mofd(market_date)
gen market_year = year(market_date)
encode stock_code, gen(stock_id)
gen pe = market_cap/net_profit_past_4q
gen pb = market_cap/book_value
* Calculate the std of stock returns over past six months *
rangestat (count) stock_ret (sd) stock_ret, by(stock_code) interval(market_mon -5 0)
* Claim the data as panel data (to enable lag operations)* 
xtset stock_id market_mon
*  Generate lagged ROE *
gen l_roe = l.roe

* Drop extreme values (<1% and >99%) *
egen p1 = pctile(net_profit_past_4q), p(1)
egen p99 = pctile(net_profit_past_4q), p(99)
keep if inrange(net_profit_past_4q, p1, p99)



*** 3. Regression analysis ***

* Scale the ROE to adjust the coefficient *
replace l_roe = 0.01*l_roe
* Generate double cluster *
egen double_cluster=group(stock_id market_year)

est clear
local i = 0
eststo: reg pb l_roe
	estadd local FIRMFE "No" 
	estadd local YEARFE "No"
	estadd local CLUSTER "No"
	local i = `i' + 1
	estimates store f`i'
eststo: reg pb beta
	estadd local FIRMFE "No" 
	estadd local YEARFE "No"
	estadd local CLUSTER "No"
	local i = `i' + 1
	estimates store f`i'
eststo: reg pb stock_ret_sd
	estadd local FIRMFE "No" 
	estadd local YEARFE "No"
	estadd local CLUSTER "No"
	local i = `i' + 1
	estimates store f`i'
eststo: reg pb l_roe beta stock_ret_sd
	estadd local FIRMFE "No" 
	estadd local YEARFE "No"
	estadd local CLUSTER "No"
	local i = `i' + 1
	estimates store f`i'
eststo: reghdfe pb l_roe beta stock_ret_sd ,absorb(stock_id market_year)
	estadd local FIRMFE "Yes" 
	estadd local YEARFE "Yes"
	estadd local CLUSTER "No"
	local i = `i' + 1
	estimates store f`i'
eststo: reghdfe pb l_roe beta stock_ret_sd ,absorb(stock_id market_year) vce(cluster stock_id)
	estadd local FIRMFE "Yes" 
	estadd local YEARFE "Yes"
	estadd local CLUSTER "Firm level"
	local i = `i' + 1
	estimates store f`i'
eststo: reghdfe pb l_roe beta stock_ret_sd ,absorb(stock_id market_year) vce(cluster double_cluster)
	estadd local FIRMFE "Yes" 
	estadd local YEARFE "Yes"
	estadd local CLUSTER "Firm-year level"
	local i = `i' + 1
	estimates store f`i'
	
esttab f* using $path_to_data/q2_reg.tex, label stats(FIRMFE YEARFE CLUSTER r2 N, fmt(0 0 0 3 0) labels(`"Firm FE"'  `"Year FE"' `"Clustered SE"' `"\(R^{2}\)"' `"Observations"')) compress t nogap b(%6.3f) noomitted drop ( ) star(* 0.1 ** 0.05 *** 0.01)  nonote  title() obslast replace

