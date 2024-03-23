
library(tidyverse)
library(caret)

car_sales <- read.csv("car_sales.csv", stringsAsFactors = FALSE)


car_sales <- na.omit(car_sales)

car_sales <- car_sales %>%
  mutate(Fuel_Type = factor(Fuel_Type),
         Seller_Type = factor(Seller_Type),
         Transmission = factor(Transmission))


summary(car_sales)

correlation_matrix <- cor(car_sales[, c("Selling_Price", "Year", "Kms_Driven", "Fuel_Type", "Seller_Type", "Transmission")])
print(correlation_matrix)

set.seed(123)
train_index <- createDataPartition(y = car_sales$Selling_Price, p = 0.8, list = FALSE)
train_data <- car_sales[train_index, ]
test_data <- car_sales[-train_index, ]

lm_model <- train(Selling_Price ~ ., data = train_data, method = "lm")

predictions <- predict(lm_model, newdata = test_data)


rmse <- sqrt(mean((predictions - test_data$Selling_Price)^2))
print(paste("Root Mean Squared Error:", rmse))

ggplot() +
  geom_point(data = data.frame(Predicted = predictions, Actual = test_data$Selling_Price), aes(x = Predicted, y = Actual), color = "blue") +
  geom_abline(intercept = 0, slope = 1, color = "red") +
  labs(title = "Predicted vs. Actual Selling Prices",
       x = "Predicted Price",
       y = "Actual Price")
