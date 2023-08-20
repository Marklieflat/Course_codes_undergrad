#设置工作目录
setwd("D:/【CUHKSZ】/AY21, T2/FIN3080/Project/Project 1/Code")

#加载需要的R包
library(tidyverse)
library(lubridate)

#读取csv文件
MoRet = read.csv("D:/【CUHKSZ】/AY21, T2/FIN3080/Project/Project 1/Code/TRD_Mont.csv")

#设置时间
Start= as.Date("2000/1/1")
Start2= as.Date("2009/11/1")
End= as.Date("2022/2/1")
Schedule = seq(from=Start, to=End, by="month")
Schedule2 = seq(from=Start2, to=End, by="month")


#筛选主板中小板，并转换时间为date对象
MainSME = MoRet %>%
  filter(锘縈arkettype==1 | 锘縈arkettype==4,na.rm=TRUE) %>%
  mutate(
    YYMM=ym(Trdmnt)
  ) %>%
  select(YYMM,Mretwdeq,Mretwdos)

#同理对创业板进行操作,剔除没有数据的第一个月
GEM_MoRet = MoRet %>%
  filter(锘縈arkettype==16,Mretwdos!=0,na.rm=TRUE) %>%
  mutate(
    YYMM=ym(Trdmnt)
  ) %>%
  select(YYMM,Mretwdeq,Mretwdos)

#合并上深主板中小板的月回报率，取mean作为代表
MainSME_MoRet= group_by(MainSME,YYMM) %>%
  summarize(Mretwdeq = mean(Mretwdeq, na.rm=TRUE),
            Mretwdos = mean(Mretwdos, na.rm=TRUE))

#处理累计回报率需要的函数
fun=function(a){
  1+a
}

MainSME_MoRet[,2:3]= apply(MainSME_MoRet[,2:3],2,fun)
GEM_MoRet[,2:3]= apply(GEM_MoRet[,2:3],2,fun)

MainSME_CmlMoRet = tibble(Month=Schedule,EqualWeighted = 0.1:266,CirMktValWeighted = 0.1:266)
GEM_CmlMoRet = tibble(Month=Schedule2,EqualWeighted = 0.1:148,CirMktValWeighted = 0.1:148)

#计算累计月回报率
for (j in 1:266){
  MainSME_CmlMoRet[j,2]=prod(MainSME_MoRet[1:j,2])
  MainSME_CmlMoRet[j,3]=prod(MainSME_MoRet[1:j,3])
  j=j+1
}

for (j in 1:148){
  GEM_CmlMoRet[j,2]=prod(GEM_MoRet[1:j,2])
  GEM_CmlMoRet[j,3]=prod(GEM_MoRet[1:j,3])
  j=j+1
}

#画主板中小板图
ggplot(data=MainSME_CmlMoRet) +
  geom_line(mapping=aes(x=Month, y=EqualWeighted,col="group"),col="red")+
  geom_line(mapping=aes(x=Month, y=CirMktValWeighted,col="group"))+
  geom_hline(yintercept=1,color="black",linetype="dashed")+
  scale_color_manual(name = "group",
                     values = c("c1" = 'red', "c2" = 'black'), 
                     labels = c('Equal weighted', 'Circulated market value weighted')) + 
  scale_linetype_manual(name = "group",
                        values = c("c1" = 0, "c2" = 1), 
                        labels = c('Equal weighted', 'Circulated market value weighted'))+
  labs(
    title=paste(
      "Main board and SME board cumulative monthly return from 2000/1 to 2022/2"),
    caption = "Data source:CSMAR",
    x="Year/Month",
    y="Cumulative monthly return"
  )+
  guides(group=guide_legend(title="none"))+
  theme(legend.position = c(.15,.9),
        legend.title=element_blank())

#画创业板图
ggplot(data=GEM_CmlMoRet) +
  geom_line(mapping=aes(x=Month, y=EqualWeighted,col="group"),col="red")+
  geom_line(mapping=aes(x=Month, y=CirMktValWeighted,col="group"))+
  geom_hline(yintercept=1,color="black",linetype="dashed")+
  scale_color_manual(name = "group",
                     values = c("c1" = 'red', "c2" = 'black'), 
                     labels = c('Equal weighted', 'Circulated market value weighted')) + 
  scale_linetype_manual(name = "group",
                        values = c("c1" = 0, "c2" = 1), 
                        labels = c('Equal weighted', 'Circulated market value weighted'))+
  labs(
    title=paste(
      "GEM board cumulative monthly return from 2009/11 to 2022/2"),
    caption = "Data source:CSMAR",
    x="Year/Month",
    y="Cumulative monthly return"
  )+
  guides(group=guide_legend(title="none"))+
  theme(legend.position = c(.15,.9),
        legend.title=element_blank())
