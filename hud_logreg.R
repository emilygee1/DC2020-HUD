library(readxl)
hud<-read_excel("~/Downloads/HUD/data/Data_Level2_HUD_HUDPrograms_2018.xlsx")
hud<-hud[,-1]
attach(hud)

set.seed(12345)
index<-sample(1:nrow(hud), 0.7*nrow(hud))
training<-hud[index,]
test<-hud[-index,]

library(nnet)
#multinomial logistic regression model with all predictors
tmodel<-multinom(pgm_type_edited ~ ., data=training)
summary(tmodel)

z <- summary(tmodel)$coefficients/summary(tmodel)$standard.errors
# two-tailed Wald tests to test significance of coefficients
p <- (1 - pnorm(abs(z), 0, 1)) * 2
p

predicted_scores<-predict(tmodel, test, "probs")
predicted_class<-predict(tmodel, test)

#confusion matrix
table(actual=test$pgm_type_edited, predicted=predicted_class)
