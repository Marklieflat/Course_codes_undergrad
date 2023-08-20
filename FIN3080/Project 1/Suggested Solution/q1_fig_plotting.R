library(ggplot2)
library(lubridate)
library(plyr) 
library(extrafont)
library(dplyr)
library(tidyr)
library(readxl)
library(writexl)
library(haven)

# Set main plotting theme for ggplot2 #
my_fig_theme = theme(
  text = element_text(family = "Palatino"),
  axis.title.x = element_text(size = 24),
  axis.text.x = element_text(size = 20, angle = 45),
  axis.title.y = element_text(size = 22),
  axis.text.y = element_text(size = 20),
  legend.text = element_text(size =20),
  legend.title = element_text(size = 22),
  legend.position = c(0.12,0.8),
  plot.title = element_text(size=28, margin=margin(0,0,20,0)),
  
)


# Change the following workplace path to your folder #
setwd('/Users/sjwang222/Desktop/FIN3080/Solution/project1/codes/')

### 1. Load median PE/PB ratios ###
ratio_df = read_dta('median_pbpe.dta')

### 2. Plot PE ratios ###
ratio_df$market_date = as.Date(ratio_df$market_date, format = "%Y-%m-%d")
ratio_df$board <- factor(ratio_df$board, levels = c('Main', 'GEM'))
ratio_df$Board <- ratio_df$board
pe_plot = ggplot(ratio_df, aes(x = market_date, y = median_pe, color = Board))+geom_line(lwd=0.6) +
  geom_point(size = 1,aes(shape = Board))+
  scale_x_date(date_breaks = '2 year', date_labels = '%Y') +
  xlab("Date")+
  ylab("Median PE Ratio (by board)")+
  my_fig_theme+
  scale_color_manual(values = c('red','blue'))
pe_plot
ggsave("q1_pe_ratio.pdf", pe_plot, width =10,height = 6.2,device = 'pdf')



### 3. Plot PB ratios ###
ratio_df$market_date = as.Date(ratio_df$market_date, format = "%Y-%m-%d")
pb_plot = ggplot(ratio_df, aes(x = market_date, y = median_pb, color = Board))+geom_line(lwd=0.6) +
  geom_point(size = 1,aes(shape = Board))+
  scale_x_date(date_breaks = '2 year', date_labels = '%Y') +
  xlab("Date")+
  ylab("Median PB Ratio (by board)")+
  my_fig_theme+
  scale_color_manual(values = c('red','blue'))
pb_plot
ggsave("q1_pb_ratio.pdf", pb_plot, width =10,height = 6.2,device = 'pdf')



