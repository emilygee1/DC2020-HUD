library(readxl)
hud<-read_excel("~/Downloads/HUD/data/original/Data_Level2_HUD_HUDPrograms_2018.xlsx")
#drop columns with unique identifier, redundant variables, rounded values, and financial related variables
#leave only demographic variables
hud<-hud[, -c(1, 3, 5:12, 15:18, 25, 26, 28:30, 37:40)]
names(hud)

set.seed(12345)

#split into training and testing sets
index<-sample(1:nrow(hud), 0.7*nrow(hud))
training<-hud[index,]
test<-hud[-index,]

library(nnet)

#multinomial logistic regression model
tmodel <- multinom(pgm_type_edited ~ ., data=training)
summary(tmodel)

z <- summary(tmodel)$coefficients/summary(tmodel)$standard.errors
# two-tailed Wald tests to test significance of coefficients
p <- (1 - pnorm(abs(z), 0, 1)) * 2
p

#make predictions on the test set about program type
predicted_scores<-predict(tmodel, test, "probs")
predicted_class<-predict(tmodel, test)

#confusion matrix and accuracy
library(MLmetrics)

ConfusionMatrix(predicted_class, test$pgm_type_edited)
Accuracy(predicted_class, test$pgm_type_edited)