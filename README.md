# Football Player Performance Prediction Using FIFA Database and Recurrent Neural Networks

## Overview
This project presents a model for predicting the performance of football players over time using Recurrent Neural Networks (RNN) and historical data from the FIFA video game series. The model applies advanced data preprocessing techniques to capture the evolution of player performance and aims to provide accurate predictions based on past performance.

## Features
- **Data Source**: FIFA player attribute data from 2005 to 2021.
- **Preprocessing**: Data cleaning, feature selection, temporal sequence generation.
- **Models Used**: Initial regression models (Ridge, Lasso, Bayesian Ridge, SVR, Random Forest) and a custom RNN model.
- **Evaluation Metrics**: Mean Squared Error (MSE), Mean Absolute Error (MAE), Coefficient of Determination (R²).
- **Results**: The custom RNN model achieved an MSE of 3.70, an MAE of 1.42, and an R² of 0.90, showcasing strong predictive capabilities for high-performing players.

## Project Structure
- **data/**: Contains raw and cleaned datasets (not included in this repository due to size).
- **notebooks/**: Jupyter notebooks for data exploration, preprocessing, and model training.
- **scripts/**: Python scripts for data preprocessing and feature engineering.
- **models/**: Saved models and configurations.
- **results/**: Visualizations and evaluation metrics for model performance.
- **README.md**: Project documentation.

## Methodology
1. **Data Collection**: We use FIFA player attributes from 2005 to 2021, sourced from Kaggle.
2. **Data Preprocessing**:
   - Concatenation of yearly data files.
   - Cleaning (removal of null values, duplicate records, and irrelevant columns).
   - Standardization and feature selection.
   - Generation of 5-year temporal sequences to capture performance trends.
3. **Model Selection**:
   - Several regression and machine learning models were evaluated initially, which presented overfitting issues.
   - A Recurrent Neural Network (RNN) model was developed to better capture the temporal relationships in player data.
4. **Evaluation**: The model was evaluated using MSE, MAE, and R², with comparisons against a Gradient Boosting model.

## Results
The RNN model, specifically the optimized \textit{RNN\_Ponderado}, demonstrated an effective balance of accuracy and generalization, with:
- **MSE**: 3.70
- **MAE**: 1.42
- **R²**: 0.90

## Future Improvements
- **Integration with Real Player Data**: Incorporating real-world player performance data for enhanced applicability.
- **Architecture Optimization**: Exploring hybrid models such as Transformers for capturing long-term trends.
- **Feature Expansion**: Including additional features, like physical and psychological metrics, to improve model accuracy.
## Dataset
The dataset used for this project is derived from FIFA player statistics. Due to size constraints and licensing, it is not included directly in this repository. You can access and download the dataset from the following link:

- [FIFA-Derived Football Player Data (2005-2021)](URL_DEL_ENLACE)

Please make sure to download the dataset and place it in the `data/` directory of the project before running the code.


