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
For a detailed breakdown of the EDA process, including the code, visualizations, and specific steps taken, please refer to the eda.ipynb file located in the project directory.

## Feature Engineering
During the feature engineering phase, several transformations were applied to improve the model's performance:

Creating new features to better capture market dynamics.
Standard Scaling was applied to continuous variables to standardize them. This transformation removes the mean and scales the data to unit variance.
The detailed feature engineering steps and code for these transformations are available in the eda.ipynb file. Please refer to it for a comprehensive view of the process.

## Machine Learning Models
This project utilizes several machine learning models for demand prediction and price optimization:

- AdaBoostRegressor: A boosting algorithm that combines weak models to create a strong model.
- GradientBoostingRegressor: A machine learning technique for regression tasks using an ensemble of decision trees.
- RandomForestRegressor: An ensemble method that builds multiple decision trees and averages their predictions.
- LinearRegression: A linear approach to modeling the relationship between the target variable and one or more features.
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
- These independent variables are used in conjunction to build and train the machine learning models for predicting the Base_Price.

## Technologies Used
This project utilizes the following libraries and tools:

### Programming and Data Analysis
- pandas: Data manipulation and analysis.
- numpy: Numerical computations.
### Visualization
- seaborn: Statistical data visualization.
- matplotlib: Plotting and chart creation.
### Machine Learning
- scikit-learn: Model building and evaluation.
- xgboost: Gradient boosting for demand prediction.
- catboost: Handling categorical features in machine learning.
### Serialization
- dill: Enhanced serialization of Python objects.
### Development Tools
- Jupyter Notebook: Code editing and debugging.

## File Organization
This project follows an end-to-end approach, including data ingestion, data transformation, model training, logging, and exception handling. Below is a description of the key files and their functions:

- data_ingestion.py: Handles the process of loading and ingesting raw data into the system, preparing it for further analysis.
- data_transformation.py: Contains functions for cleaning and transforming the data, such as handling missing values, feature encoding, and scaling.
- model_trainer.py: Defines and trains machine learning models, evaluates their performance, and saves the trained models for future use.
- exception.py: Custom exception handling file that ensures errors during the process are caught and logged effectively.
- logger.py: Manages logging to track the flow of the application, making it easier to debug and monitor.
- utils.py: Includes helper functions used throughout the project, such as loading configuration settings, saving models, and making predictions.
- app.py: The main script that ties all the components together, running the data ingestion, transformation, model training, and predictions in a sequential manner.
- 
## Results
### Model Performance
The models were evaluated using key performance metrics, including R² Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE). 
