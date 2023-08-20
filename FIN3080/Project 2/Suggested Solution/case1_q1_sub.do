*** This is the coding solution for Project 2 Case 1 Q1 (FIN 3080) ***

** This script supplements the case_q1_sub.do by reporting frist-stage and second regression results ** 

** Remark: this script requires the 'asreg' package. You may uncomment following lines to install them first (if not installed before) **
// ssc install asreg

*** 0. Set program options and specify raw data path ***

set more off  // Set this option off to enable consecutive screen outputs
set excelxlsxlargefile on // Set this option on to enable Stata to import large excel files

* Change the following path to your own path to raw data * 
global path_to_data ="/Users/sjwang222/Desktop/FIN3080/Solution/project2/data_code"

*** 5. Test the CAPM model following Chen et al (2019) ***


** Step 1. Estimate the individual beta using first-period data **

use $path_to_data/case1_merged_stock_return, clear

* Drop obs later than 2018w17 * 
keep if year_week <= weekly("2018-17","YW")

* Run individual level regression using [2017w1, 2018w17] data only *

est clear 
	local i = 0
	eststo: reg r_i r_m if stock_code == "002767"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "002371"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "000717"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "601390"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "600497"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "600223"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "002522"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "000607"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "600353"
		local i = `i' + 1
		estimates store f`i'
	eststo: reg r_i r_m if stock_code == "601021"
		local i = `i' + 1
		estimates store f`i'
	
	esttab f* using $path_to_data/case1_reg1.tex, label stats(r2 N, fmt(3 0) labels(`"\(R^{2}\)"' `"Observations"')) compress t nogap b(%6.3f) noomitted drop ( ) star(* 0.1 ** 0.05 *** 0.01)  nonote  title() obslast replace



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
est clear 
	local i = 0
forvalue v = 1/10{
	eststo: reg rp_rf rm_rf if beta_decile == `v'
		local i = `i' + 1
		estimates store f`i'
}
	esttab f* using $path_to_data/case1_reg2.tex, label stats(r2 N, fmt(3 0) labels(`"\(R^{2}\)"' `"Observations"')) compress t nogap b(%6.3f) noomitted drop ( ) star(* 0.1 ** 0.05 *** 0.01)  nonote  title() obslast replace

