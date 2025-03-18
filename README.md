# ML-Driven Shipment Delay Probability Prediction for Logistics
## Overview
This project focuses on developing a delay prediction for shipments. The goal is to predict whether a shipment will be delay using machine learning models, considering factors like traffic congestion level, warehouse inventory level, weather condition severity, supplier reliability score, route risk level, etc.

## Data Description
The dataset captures a comprehensive set of logistics and supply chain operations, specifically collected from a logistics network in Southern California. The data spans from January 2021 to January 2024, encompassing various aspects of transportation, warehouse management, route planning, and real-time monitoring. It includes detailed hourly records of logistics activities, reflecting conditions in urban areas and transport corridors known for high traffic and dynamic operational challenges.

The dataset is collected from various sources, such as GPS tracking systems, IoT sensors, warehouse management systems, and external data providers. It covers different transportation modes, including trucks, drones, and rail, providing insights into operational efficiency, risk factors, and service reliability. The data has been anonymized and processed to ensure privacy while preserving the information needed for analysis.

## Features Overview
The dataset includes a variety of features that represent different aspects of logistics operations:

- Timestamp: The date and time when the data was recorded (hourly resolution).
- Vehicle GPS Latitude: The latitude coordinate indicating the location of the vehicle.
- Vehicle GPS Longitude: The longitude coordinate indicating the location of the vehicle.
- Fuel Consumption Rate: The rate of fuel consumption recorded for the vehicle in liters per hour.
- ETA Variation (hours): The difference between the estimated and actual arrival times.
- Traffic Congestion Level: The level of traffic congestion affecting the logistics route (scale 0-10).
- Warehouse Inventory Level: The current inventory levels at the warehouse (units).
- Loading/Unloading Time: The time taken for loading or unloading operations in hours.
- Handling Equipment Availability: Availability status of equipment like forklifts (0 = unavailable, 1 = available).
- Order Fulfillment Status: Status indicating whether the order was fulfilled on time (0 = not fulfilled, 1 = fulfilled).
- Weather Condition Severity: The severity of weather conditions affecting operations (scale 0-1).
- Port Congestion Level: The level of congestion at the port (scale 0-10).
- Shipping Costs: The costs associated with the shipping operations in USD.
- Supplier Reliability Score: A score indicating the reliability of the supplier (scale 0-1).
- Lead Time (days): The average time taken for a supplier to deliver materials.
- Historical Demand: The historical demand for logistics services (units).
- IoT Temperature: The temperature recorded by IoT sensors in degrees Celsius.
- Cargo Condition Status: Condition status of the cargo based on IoT monitoring (0 = poor, 1 = good).
- Route Risk Level: The risk level associated with a particular logistics route (scale 0-10).
- Customs Clearance Time: The time required to clear customs for shipments.
- Driver Behavior Score: An indicator of the driver's behavior based on driving patterns (scale 0-1).
- Fatigue Monitoring Score: A score indicating the level of driver fatigue (scale 0-1).
- Disruption Likelihood Score: A score predicting the likelihood of a disruption occurring (scale 0-1).
- Delay Probability: The probability of a shipment being delayed (scale 0-1).
- Risk Classification: A categorical classification indicating the level of risk (Low Risk, Moderate Risk, High Risk).
- Delivery Time Deviation: The deviation in hours from the expected delivery time.

## Exploratory Data Analysis (EDA)
The first phase of the project involved Exploratory Data Analysis (EDA) to understand the dataset, identify patterns, and check for any inconsistencies or anomalies. Key steps included:

- Analyzing the distribution of key variables.
- Performing correlation analysis to explore relationships between variables.
- Handling and outliers.
- Visualizing data using matplotlib and seaborn for better insights.

## Feature Engineering
During the feature engineering phase, several transformations were applied to improve the model's performance:
- Standard Scaler: Standardising is important when we compare different attributes that have very different units.
- Power Transformer: Automates the decision of square root/cube root/log transformation by introducing a parameter lambda and finds the best value of lambda based on Box-Cox transformation or Yeo-Johnson transformation.

## Machine Learning Models
This project utilizes several machine learning models for delay probability prediction:

- RandomForestRegressor: An ensemble method that builds multiple decision trees and averages their predictions.
- PolynomialRegression: A linear approach to modeling the relationship where only due to the non-linear relationship between dependent and independent variables.
- DecisionTreeRegressor: A decision tree algorithm for regression tasks.
- XGBRegressor: A gradient boosting method, optimized for speed and performance in regression tasks.

## Variables
In this project, the dependent variable (target) and independent variables (features) have been defined as follows:

### Dependent Variable
- Delay Probability: The target variable that we are trying to predict. It represents the probability of a shipment being delayed (scale 0-1).
### Independent Variables
The following features are used as independent variables to predict the Base_Price:

- Fuel Consumption Rate: The rate of fuel consumption recorded for the vehicle in liters per hour.
- ETA Variation (hours): The difference between the estimated and actual arrival times.
- Traffic Congestion Level: The level of traffic congestion affecting the logistics route (scale 0-10).
- Warehouse Inventory Level: The current inventory levels at the warehouse (units).
- Loading/Unloading Time: The time taken for loading or unloading operations in hours.
- Handling Equipment Availability: Availability status of equipment like forklifts (0 = unavailable, 1 = available).
- Order Fulfillment Status: Status indicating whether the order was fulfilled on time (0 = not fulfilled, 1 = fulfilled).
- Weather Condition Severity: The severity of weather conditions affecting operations (scale 0-1).
- Port Congestion Level: The level of congestion at the port (scale 0-10).
- Shipping Costs: The costs associated with the shipping operations in USD.
- Supplier Reliability Score: A score indicating the reliability of the supplier (scale 0-1).
- Lead Time (days): The average time taken for a supplier to deliver materials.
- Historical Demand: The historical demand for logistics services (units).
- IoT Temperature: The temperature recorded by IoT sensors in degrees Celsius.
- Cargo Condition Status: Condition status of the cargo based on IoT monitoring (0 = poor, 1 = good).
- Route Risk Level: The risk level associated with a particular logistics route (scale 0-10).
- Customs Clearance Time: The time required to clear customs for shipments.
- Driver Behavior Score: An indicator of the driver's behavior based on driving patterns (scale 0-1).
- Fatigue Monitoring Score: A score indicating the level of driver fatigue (scale 0-1).

## Technologies Used
This project utilizes the following libraries and tools:

### Programming and Data Analysis
- pandas: Data manipulation and analysis.
- numpy: Numerical computations.
### Visualization
- matplotlib: Plotting and chart creation.
### Machine Learning
- scikit-learn: Model building and evaluation.
- xgboost: Gradient boosting for demand prediction.
### Serialization
- dill: Enhanced serialization of Python objects.
### Development Tools
- Jupyter Notebook: Code editing and debugging.
  
## Results
### Model Performance
The models were evaluated using key performance metrics, including R² Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE). 

| Model                      | MAE      | MSE      | RMSE     | R²       |
|----------------------------|----------|----------|----------|----------|
| Polynomial Regression      | 0.281022 | 0.106741 | 0.326712 | -0.000635 |
| Decision Tree Regression   | 0.281117 | 0.106907 | 0.326967 | -0.002194 |
| Random Forest Regression   | 0.281028 | 0.106758 | 0.326738 | -0.000792 |
| XGBoost Regression        | 0.281637 | 0.107447 | 0.327791 | -0.007254 |

Regarding the evaluation results of the four models, it is evident that the models fail to predict the delay probability of orders.
