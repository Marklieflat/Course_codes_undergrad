*** This is the coding solutions for question 1 of project 1 (FIN 3080) ***

** This script load raw fundamental & stock market data and then cleans the data to construct monthly median PB/PE ratios. Figures are plotted with q1_fig_plotting.R**

** Remark: this script requires 'rangestat' package. You may uncomment the following two lines to install them first (if not installed before) **
// ssc install rangestat

*** 0. Set options and raw data path ***

set more off  // Set this option off to enable consecutive screen outputs
set excelxlsxlargefile on // Set this option on to enable Stata to import large excel files
* Change the following path to your own path to raw data * 
global path_to_data ="/Users/sjwang222/Desktop/FIN3080/Solution/project1/codes"

*** 1. Load & clean income statement data ***

* Import raw income statement data *
import excel using $path_to_data/quarterly_income.xlsx, firstrow clear
save $path_to_data/raw_quarterly_income, replace
// use $path_to_data/raw_quarterly_income, clear

* Convert original dates to Year-Quarter format *
gen fiscal_date = date(EndingDateofFiscalYear, "YMD")
gen fiscal_yq = qofd(fiscal_date)
format fiscal_yq %tq

* Rename few variables of interest *
rename NetProfit net_profit
rename StockCode stock_code
keep stock_code fiscal_yq net_profit

* Drop duplicated records *
bysort stock_code fiscal_yq: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

* Rollingly calculate the summation of net profit over past 4 quarters *
rangestat (sum) net_profit_past_4q = net_profit, by(stock_code) interval(fiscal_yq -3 0)

* Drop data piror to 2000 *
drop if fiscal_yq < yq(2000,1)

* Save the output data *
save $path_to_data/quarterly_income, replace


*** 2. Supplement income data with balance data ***

* Import raw balance data *
import excel using $path_to_data/quarterly_balance.xlsx, firstrow clear
save $path_to_data/raw_quarterly_balance, replace 
//use $path_to_data/raw_quarterly_balance, replace 

* Convert original dates to Year-Quarter format *
gen fiscal_date = date(EndingDateofFiscalYear, "YMD")
gen fiscal_yq = qofd(fiscal_date)
format fiscal_yq %tq

* Construct variables of interest *
gen book_value = TotalAssets - TotalLiabilities

* Rename few variables *
rename StockCode stock_code
rename TotalShareholdersEquity total_shareholder_equity

* Keep necessary variables *
keep stock_code fiscal_yq book_value total_shareholder_equity

* Drop duplicated records *
bysort stock_code fiscal_yq: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup
save $path_to_data/quarterly_balance, replace

* Merge income data to this data set *
merge 1:1 stock_code fiscal_yq using $path_to_data/quarterly_income
keep if _merge == 3
drop _merge

save $path_to_data/quarterly_fundamental, replace



*** 3. Merge fundamental data to stock market data ***

* Import raw monthly stock data *
import excel using $path_to_data/monthly_stock.xlsx, firstrow clear
save $path_to_data/raw_monthly_stock, replace
//use $path_to_data/raw_monthly_stock,clear



* Format date *
gen market_date = date(TradingMonth, "YM")
gen market_yq = qofd(market_date)
format market_yq %tq
format market_date %td

* Generate fiscal date *
gen fiscal_yq = market_yq - 1
format fiscal_yq %tq

* Keep firms listed on main and GEM boards *
keep if MarketType == 1 | MarketType == 4 |MarketType == 16
gen board = "Main"
replace board = "GEM" if MarketType == 16

* Generate and rename variables of interest *
rename StockCode stock_code
rename MonthlyClosingPrice price
rename MonthlyReturnWithCashDividen stock_ret
rename TotalMarketValue market_cap
rename MarketValueofTradableShares market_cap_tradable

keep stock_code market_date price stock_ret market_yq fiscal_yq board market_cap market_cap_tradable
save $path_to_data/monthly_market, replace

merge m:1 stock_code fiscal_yq using $path_to_data/quarterly_fundamental
keep if _merge == 3
drop _merge 

save $path_to_data/market_with_fundamental, replace


** 4. Calculate monthly static PE, PB ratios by board **

* Load merged data *
use $path_to_data/market_with_fundamental, clear

* Generate firm-level PB and PE ratios *
gen pe = market_cap/net_profit_past_4q
gen pb = market_cap/book_value

* Generate board-level median PB and PE ratios *
bysort board market_date: egen median_pe = median(pe)
bysort board market_date: egen median_pb = median(pb)

* Zip data to board-month level *
bysort board market_date: gen dup = cond(_N==1,0,_n)
drop if dup > 1
drop dup

* Output results *
keep board market_date median_pe median_pb
save $path_to_data/median_pbpe, replace



