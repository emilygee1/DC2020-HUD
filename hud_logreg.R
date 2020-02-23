library(readxl)
hud<-read_excel("~/Downloads/HUD/data/Data_Level2_HUD_HUDPrograms_2018.xlsx")
hud<-hud[,-1]
attach(hud)

set.seed(12345)
index<-sample(1:nrow(hud), 0.7*nrow(hud))
training<-hud[index,]
test<-hud[-index,]

library(nnet)
#multinomial logistic regression model with chosen predictors
tmodel<-multinom(pgm_type_edited ~ 
                   HSHD_MBR_TOTAL_CNT+
                   TOTAL_DPNDNT_CNT+
                   TOTAL_ANNL_INCM_AMNT+
                   HEAD_GNDR_CD+
                   HEAD_AGE_YR_CNT+
                   HEAD_ELDLY_INDR+
                   HEAD_RACE_CD+
                   HEAD_ETHNCY_CD+
                   DSBLD_CHLDRN_CNT+
                   CHLDRN_MBR_CNT+
                   GROSS_RENT_AMNT+
                   TOTAL_FMLY_CRBTN_AMNT+
                   PVRTY_PRCNT+
                   MNRTY_PRCNT+
                   BLACK_PRCNT+
                   HISPANIC_PRCNT+
                   WHITE_PRCNT
                 , data=training)
summary(tmodel)

z <- summary(tmodel)$coefficients/summary(tmodel)$standard.errors
# two-tailed Wald tests to test significance of coefficients
p <- (1 - pnorm(abs(z), 0, 1)) * 2
p

predicted_scores<-predict(tmodel, test, "probs")
predicted_class<-predict(tmodel, test)

#confusion matrix and accuracy
library(MLmetrics)

ConfusionMatrix(predicted_class, test$pgm_type_edited)
Accuracy(predicted_class, test$pgm_type_edited)