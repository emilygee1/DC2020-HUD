library(readxl)
hud <- read_excel("~/Downloads/HUD/data/original/Data_Level2_HUD_HUDPrograms_2018.xlsx")

#drop columns with unique identifier, redundant variables, and rounded values
hud <- hud[,-c(1, 6:12, 15:18, 25, 26, 37:40)]

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

#confusion matrix and accuracy
library(MLmetrics)
ConfusionMatrix(predicted_class, test$pgm_type_edited)
Accuracy(predicted_class, test$pgm_type_edited)
