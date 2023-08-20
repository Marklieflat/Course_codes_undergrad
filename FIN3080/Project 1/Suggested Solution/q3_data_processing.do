*** This is the coding solutions for question 3 of project 1 (FIN 3080) ***

** This script construct monthly cumulative equal-weighted and value-weighted returns for GEM and main boards. Figures are plotted with q3_fig_plotting.R**

** Remark: this script requires 'rangestat' package. You may uncomment the following two lines to install them first (if not installed before) **


*** 0. Set options and workplace path ***

set more off  // Set this option off to enable consecutive screen outputs
set excelxlsxlargefile on // Set this option on to enable Stata to import large excel files
* Set the following path to your own path to raw data * 
global path_to_data ="/Users/sjwang222/Desktop/FIN3080/Solution/project1/codes"

*** 1. Loan monthly stock return data ***


*** 1. Calculate equal-weighted stock returns by board *** 

* Load cleaned data *
use $path_to_data/monthly_market, clear
drop if market_cap ==. | stock_ret ==.

* Calculate equal weighted returns by board * 
gen market_mon = mofd(market_date)
bysort board market_date: egen ew_mean_ret =  mean(stock_ret)

* Zip data to board-month level *
bysort board market_date: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup
sort board market_mon

* Calculate monthly cumulative returns by board *
* (Note that there is no cumprod functions in raw Stata so that we use log operations and the sum function instead.) * 
by board: gen double sum_ln_ew_ret = sum(ln(1+ew_mean_ret)) 
gen double cum_ew_mean_ret = exp(sum_ln_ew_ret) - 1
keep board market_date cum_ew_mean_ret
save $path_to_data/ew_ret, replace


*** 2. Calculate value-weighted stock returns by board *** 
* Load cleaned data *
use $path_to_data/monthly_market, clear
drop if market_cap ==. | stock_ret ==.
gen market_mon = mofd(market_date)

* Claim the data as panel data (to enable lag operations) *
encode stock_code, gen (stock_id)
xtset stock_id market_mon
sort stock_id market_mon

* Generate lagged market cap *
gen l_market_cap = l.market_cap_tradable

* Calculate value-weighted stock returns
gen ret_cap = stock_ret * market_cap
bysort board market_mon: egen double total_ret_cap = total(ret_cap)
bysort board market_mon: egen double total_market_cap = total(market_cap)
gen vw_mean_ret = total_ret_cap/total_market_cap
bysort board market_date: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup
sort board market_mon

* Calculate monthly cumulative returns by board *
by board: gen sum_ln_vw_ret = sum(ln(1+vw_mean_ret))
gen double cum_vw_mean_ret = exp(sum_ln_vw_ret) - 1
keep board market_date cum_vw_mean_ret

save $path_to_data/vw_ret, replace

* Merge equal-weighted returns to this data set *
merge 1:1 board market_date using $path_to_data/ew_ret
drop _merge
save $path_to_data/mean_return, replace


* Output the results *
keep if board == "Main"
drop board
save $path_to_data/mean_return_main, replace
use $path_to_data/mean_return, clear
keep if board == "GEM"
drop board
save $path_to_data/mean_return_gem, replace

