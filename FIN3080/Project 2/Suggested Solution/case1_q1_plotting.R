library(ggplot2)
library(lubridate)
library(plyr) 
library(extrafont)
library(dplyr)
library(tidyr)
library(readxl)
library(writexl)
library(haven)
library(latex2exp)

# Set main plotting theme for ggplot2 #
my_fig_theme = theme(
  text = element_text(family = "Palatino"),
  axis.title.x = element_text(size = 24),
  axis.text.x = element_text(size = 20, angle = 45),
  axis.title.y = element_text(size = 22),
  axis.text.y = element_text(size = 20),
  #legend.text = element_text(size =20),
  #legend.title = element_text(size = 22),
  #legend.position = c(0.12,0.8),
  legend.position = "none",
  plot.title = element_text(size=28, margin=margin(0,0,20,0)),
  
)


# Change the following workplace path to your folder #
setwd('/Users/sjwang222/Desktop/FIN3080/Solution/project2/data_code/')

### 1. Load median PE/PB ratios ###
reg_df = read_dta('case1_last_reg.dta')



reg_plot = ggplot(reg_df, aes(x = beta_p, y = bar_rp_rf)) + 
  stat_smooth(method = "lm", col = "red", size =2)+
  geom_point(size = 5,col = 'blue', shape = 23, fill = 'blue') +
  xlab(TeX(r"($\beta_p$)"))+
  ylab(TeX(r"($\bar{r_p-r_f}$)"))+
  my_fig_theme

reg_plot
ggsave("q1_regression.pdf", reg_plot, width =10,height = 6.2,device = 'pdf')
