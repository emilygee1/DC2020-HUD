library(readxl)
hud <- read_excel("~/Downloads/HUD/data/original/Data_Level2_HUD_HUDPrograms_2018.xlsx")

#drop columns with unique identifier, redundant variables, rounded values, and financial related variables
#leave only demographic variables
hud<-hud[, -c(1, 3, 5:12, 15:18, 25, 26, 28:30, 37:40)]

set.seed(12345)

#split into training and testing sets
index <- sample(1:nrow(hud), 0.7*nrow(hud))
train <- hud[index,]
test <- hud[-index,]

library(rpart)
library(rpart.plot)

#full classification tree with all predictors
ct <- rpart(pgm_type_edited ~ ., data=train, method="class", cp=0, minsplit=1)

#cross-validation procedure to find tree with lowest error
crossvalid_ct <- rpart(pgm_type_edited~., data=train, method="class", cp=0.00001)
plotcp(crossvalid_ct)

#prune the tree
pruned_ct <- prune(crossvalid_ct, cp=crossvalid_ct$cptable[which.min(crossvalid_ct$cptable[, 'xerror']), 'CP'])

print(pruned_ct)
prp(pruned_ct, type=1, extra=1, under=TRUE)

#make predictions on test set using pruned tree
library(prediction)
predicted_class <- predict(pruned_ct, test, type="class")

#confusion matrix and performance measures
library(MLmetrics)

ConfusionMatrix(predicted_class, test$pgm_type_edited)

Accuracy(predicted_class, test$pgm_type_edited)
acc <- format(round(acc, 3), nsmall = 3)
recall <- Sensitivity(test$pgm_type_edited, predicted_class)
recall <- format(round(recall, 3), nsmall = 3)
cat('Accuracy: ', acc, '\n', 'Recall: ', recall)