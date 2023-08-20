*** This is the coding solution for Project 2 Case 1 Q1 (FIN 3080) ***

** This script clean and merge raw data and generate the final stage regression table corresponding to Case 1 Q1. The figures corresponding to the regression is given by case1_q1_plotting.R ** 

** Remark: this script requires the 'asreg' package. You may uncomment following lines to install them first (if not installed before) **
// ssc install asreg


*** 0. Set program options and specify raw data path ***

set more off  // Set this option off to enable consecutive screen outputs
set excelxlsxlargefile on // Set this option on to enable Stata to import large excel files

* Change the following path to your own path to raw data * 
global path_to_data ="/Users/sjwang222/Desktop/FIN3080/Solution/project2/data_code"


*** 1. Load & clean individual stock return data ***

* Import raw stock return data *

import delimited $path_to_data/case1_raw_stock_return.csv, stringcols(_all) encoding(UTF-8)  clear 
//save $path_to_data/case1_raw_stock_return, replace
//use $path_to_data/case1_raw_stock_return, clear

* Convert original dates to Year-Month format *
gen year_week = weekly(trdwnt, "YW")
format year_week %tw

* Rename and destring few variables of interest *
rename wretnd stock_ret
rename stkcd stock_code
rename markettype market
destring stock_ret, replace
keep stock_code year_week stock_ret market

* Keep stocks listed on main boards only *
keep if market == "1" |market == "4"

* Drop duplicated records *
drop if year_week == . | stock_ret ==.

* Save processed stock return data *
save $path_to_data/case1_processed_stock_return, replace


*** 2. Load market return data *** 

* Import raw market return data *

import delimited $path_to_data/case1_raw_index_return.csv, stringcols(_all) encoding(UTF-8)  clear 
//save $path_to_data/case1_raw_index_return, replace
//use $path_to_data/case1_raw_index_return, clear

* Keep SZ-SH aggregated market return only*
keep if markettype == "5"

* Format date (as year-week)*
gen year_week = weekly(trdwnt, "YW")
format year_week %tw

* Rename and desting vars *
rename cwretmdos market_ret
destring market_ret, replace
rename markettype market
drop if year_week == . | market_ret == .

* Save processed mrrket return data *
keep year_week market_ret
save $path_to_data/case1_processed_market_return, replace


*** 3. Load Shibor Rate ***

* Import raw shibor rate data *
import delimited $path_to_data/case1_raw_shibor.csv, stringcols(_all) encoding(UTF-8)  clear 
//save $path_to_data/case1_raw_shibor, replace
//use $path_to_data/case1_raw_shibor, clear

* Keep 7-day shibor rate only *
keep if term_en == "7 days"

* Format date (as year-week) and drop duplicates *
gen date = date(sgndate, "YMD")
format date %td
gen year_week = yw(year(date), week(date))
format year_week %tw
sort date
bysort year_week: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

* Scale shibor rate *
destring shibor, replace
replace shibor = shibor/50

* Save processed shibor rate *
keep year_week shibor
save $path_to_data/case1_processed_shibor, replace



*** 4. Merge all returns & rates data together ***

* Load processed return data *
use $path_to_data/case1_processed_stock_return, clear

* Merge market price to stock return data *
merge m:1 year_week using $path_to_data/case1_processed_market_return
keep if _merge == 3
drop _merge

* Merge Shibor rate to stock return data *
merge m:1 year_week using $path_to_data/case1_processed_shibor
keep if _merge == 3
drop _merge

* Generate r_f, r_m, (r_i-r_f) and (r_m-r_f)
gen r_f = shibor/100
gen r_i = stock_ret
gen r_m = market_ret
gen ri_rf = r_i - r_f
gen rm_rf = r_m - r_f

keep stock_code year_week r_f r_i r_m ri_rf rm_rf

* Save resulting data *
save $path_to_data/case1_merged_stock_return, replace



*** 5. Test the CAPM model following Chen et al (2019) ***

** Step 1. Estimate the individual beta using first-period data **

use $path_to_data/case1_merged_stock_return, clear

* Drop obs later than 2018w17 * 
keep if year_week <= weekly("2018-17","YW")

* Run individual level regression using [2017w1, 2018w17] data only *
bysort stock_code: asreg r_i r_m

rename _b_r_m beta_i
keep stock_code beta_i

bysort stock_code: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

* Generate beta_i's 10th quantiles and save quantiles *
egen beta_decile = xtile(beta_i), p(10(10)90)
save $path_to_data/case1_beta_quantile_p1, replace


** Step 2. Estimate the group beta using second-period data **

use $path_to_data/case1_merged_stock_return, clear

* Restrict sample to [2018w18, 2019w35]*
keep if year_week >= weekly("2018-18","YW")
keep if year_week <= weekly("2019-35", "YW")

* Merge beta quantiles from Step 1. to stock return data *
merge m:1 stock_code using $path_to_data/case1_beta_quantile_p1
keep if _merge == 3
drop _merge

* Calulate r_p as the mean of r_i within each beta quantile group *
bysort beta_decile year_week: egen r_p = mean(r_i)
sort stock_code year_week 
gen rp_rf = r_p - r_f
sort beta_decile year_week

* Zip data to (beta-) quantile-week level *
bysort beta_decile year_week: gen dup = cond(_N==1,0,_n)
drop if dup > 1

keep rp_rf rm_rf year_week beta_decile

* Estimate beta_p *
bysort beta_decile: asreg rp_rf rm_rf
rename _b_rm_rf beta_p

* Zip data to (beta-) quantile level *
bysort beta_decile: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

save $path_to_data/case1_beta_p_p2, replace


** Step 3. Run the cross-sectional regression with last period data **

use $path_to_data/case1_merged_stock_return, clear
keep if year_week >= weekly("2019-36","YW")

merge m:1 stock_code using $path_to_data/case1_beta_quantile_p1
keep if _merge == 3
drop _merge

bysort beta_decile year_week: egen r_p = mean(r_i)
gen rp_rf = r_p - r_f
bysort beta_decile: egen bar_rp_rf = mean(rp_rf)

* Zip data to (beta-) quantile level *
bysort beta_decile: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

* Merge beta_p estimated from Step 2 with current data *
merge m:1 beta_decile using $path_to_data/case1_beta_p_p2
keep if _merge == 3
drop _merge

drop if beta_decile == .

save $path_to_data/case1_last_reg, replace

* Regress rp - rf on beta_p *
reg bar_rp_rf beta_p

* Draw regression scatter plot *
twoway scatter bar_rp_rf beta_p || lfit bar_rp_rf beta_p
graph export $path_to_data/case1_regression.png, replace

