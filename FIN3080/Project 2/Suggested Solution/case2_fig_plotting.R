library(ggplot2)
library(lubridate)
library(plyr) 
library(extrafont)
library(readr)
library(data.table)
library(janitor)
library(dplyr)
library(latex2exp)
library(stringr)
library(readxl)
library(writexl)
library(haven)
library(reshape2)


my_fig_theme = theme(
  text = element_text(family = "Palatino"),
  axis.title.x = element_text(size = 20),
  axis.text.x = element_text(size = 16),
  axis.title.y = element_text(size = 20),
  axis.text.y = element_text(size = 16),
  legend.text = element_text(size =18),
  legend.title = element_text(size = 20),
  legend.position = c(0.835,0.85)
)

# Change the following workplace path to your folder #
setwd('/Users/sjwang222/Desktop/FIN3080/Solution/project2/data_code/')

dta_ls = c('case2_q1_data_for_plotting.dta', 'case2_q2_data_for_plotting.dta', 
           'case2_q3_data_for_plotting.dta' , 'case2_q4_data_for_plotting.dta')
Q <- function(x) paste('Q',toString(x), sep = '')
color_ls = c("Equal-weighted" = "#0e387a", "Value-weighted" = "#9fafca")
color_ls = c("Equal-weighted" = "#0f149a", "Value-weighted" = "#fd9b4d")

for (raw_dta in dta_ls){
    if (grepl("q4", raw_dta)){
      my_fig_theme$legend.position = c(0.2,0.85)
    }
    return_df = read_dta(raw_dta)
    return_df$date = as.Date(return_df$date, format = "%Y-%m-%d")
    ew_return_df = data.frame(Portfolio = return_df$group)
    ew_return_df$return = return_df$ew_ret
    ew_return_df$Weight = 'Equal-weighted'
    vw_return_df = data.frame(Portfolio = return_df$group)
    vw_return_df$return = return_df$vw_ret
    vw_return_df$Weight = 'Value-weighted'
    return_df = rbind(ew_return_df, vw_return_df)
    return_df$Portfolio = mapply(Q, return_df$Portfolio)
    return_df$Portfolio = factor(return_df$Portfolio, levels = c('Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10'))
    #hl_dc_df = rbind(high_dc_df, low_dc_df)
    return_plot = ggplot(data = return_df)+
      geom_bar(aes(x =Portfolio, y = return,  fill = Weight),
               position = "dodge",
               stat = "identity")+
      labs(
        x= "Portfolio",
        y = "Return",
        color = "Weight"
      )+
      scale_fill_manual(values = color_ls)+
      my_fig_theme
    save_name = str_replace(raw_dta, '\\.dta', '.pdf')
    save_name = str_replace(save_name, '_data_for_plotting', '_portfolio_return')
    ggsave(save_name, return_plot, width =10,height = 6.2,device = 'pdf')
   # break
  
}




