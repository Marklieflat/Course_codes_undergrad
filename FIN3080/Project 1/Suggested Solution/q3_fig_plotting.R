library(ggplot2)
library(lubridate)
library(plyr) 
library(extrafont)
library(dplyr)
library(tidyr)
library(readxl)
library(writexl)
library(haven)
library(reshape2)

# Set main plotting theme for ggplot2 #
my_fig_theme = theme(
  text = element_text(family = "Palatino"),
  axis.title.x = element_text(size = 24),
  axis.text.x = element_text(size = 20, angle = 45),
  axis.title.y = element_text(size = 22),
  axis.text.y = element_text(size = 20),
  legend.text = element_text(size =20),
  legend.title = element_text(size = 22),
  legend.position = c(0.2,0.8),
  plot.title = element_text(size=28, margin=margin(0,0,20,0)),
)

# Change the following workplace path to your folder #
setwd('/Users/sjwang222/Desktop/FIN3080/Solution/project1/codes/')

### 1. Plot weighted returns for main board ###
return_df = read_dta('mean_return_main.dta')
return_df$market_date = as.Date(return_df$market_date, format = "%Y-%m-%d")
return_df = melt(return_df, id = c('market_date'))
return_df$Return = return_df$variable
return_df = return_df %>% mutate(
  Return = case_when(
    Return == 'cum_ew_mean_ret' ~ 'Equal-weighted',
    Return == 'cum_vw_mean_ret' ~ "Value-weighted"
  )
)
main_plot = ggplot(return_df, aes(x = market_date, y = value, color = Return))+geom_line(lwd=0.6) +
  geom_point(size = 1,aes(shape = Return))+
  scale_x_date(date_breaks = '2 year', date_labels = '%Y') +
  xlab("Date")+
  ylab("Cumulative Stock Return")+
  my_fig_theme+
  scale_color_manual(values = c('red','blue'))

main_plot
ggsave("q3_main_return.pdf", main_plot, width =10,height = 6.2,device = 'pdf')

### 2. Plot weighted returns for GEM board ###
return_df = read_dta('mean_return_gem.dta')
return_df$market_date = as.Date(return_df$market_date, format = "%Y-%m-%d")
return_df = melt(return_df, id = c('market_date'))
return_df$Return = return_df$variable
return_df = return_df %>% mutate(
  Return = case_when(
    Return == 'cum_ew_mean_ret' ~ 'Equal-weighted',
    Return == 'cum_vw_mean_ret' ~ "Value-weighted"
  )
)
gem_plot = ggplot(return_df, aes(x = market_date, y = value, color = Return))+geom_line(lwd=0.6) +
  geom_point(size = 1,aes(shape = Return))+
  scale_x_date(date_breaks = '2 year', date_labels = '%Y') +
  xlab("Date")+
  ylab("Cumulative Stock Return")+
  my_fig_theme+
  scale_color_manual(values = c('red','blue'))
gem_plot
ggsave("q3_gem_return.pdf", gem_plot, width =10,height = 6.2,device = 'pdf')

