# Gold Price Prediction 📈

## Project Overview
Gold Price Prediction is a machine learning project aimed at forecasting the future price of gold using historical data. The primary objective is to help investors and stakeholders make informed decisions by leveraging predictive analytics. The project applies regression techniques to understand trends and patterns in gold prices over time.

## Objectives
- Predict the future price of gold based on historical data.
- Evaluate different regression models to identify the best-performing approach.
- Deploy the model via a user-friendly web application for easy accessibility.

## Methodology
1. **Data Collection & Preprocessing**  
   Historical gold price data was collected and cleaned to remove inconsistencies and missing values. Features were engineered to capture time-series patterns, including lag features and rolling statistics.

2. **Exploratory Data Analysis (EDA)**  
   Visualizations were created to understand trends, seasonality, and correlations between features. This helped in identifying important predictors for the model.

3. **Model Development**  
   Multiple regression models were trained, including:
   - Linear Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor  

   Model performance was evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score.

4. **Hyperparameter Tuning**  
   Grid Search and Cross-Validation were applied to optimize model parameters and improve prediction accuracy.

5. **Deployment**  
   The final model was deployed as a web application using Streamlit, allowing users to input parameters and receive real-time gold price predictions.

## Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit  
- **IDE/Environment:** Jupyter Notebook  
- **Deployment:** Streamlit  

## Deployment
Access the interactive web application here: 

## How to Run Locally
Follow these steps to run the project on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Gold-Price-Prediction.git
   cd Gold-Price-Prediction

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate


3. **Install dependencies**
    ```bash
    pip install -r requirements.txt


4. **Run the Streamlit app**
    ```bash
    streamlit run app.py

5. **Open the app**
    Open the provided local URL in your browser to interact with the gold price prediction tool.

## Results and Conclusion
The deployed model effectively predicts gold prices with strong accuracy, providing valuable insights for investors and stakeholders.  

Ensemble regression models, such as Random Forest and Gradient Boosting, outperformed simple Linear Regression, demonstrating their strength in capturing complex patterns.  

Overall, this project highlights the successful integration of data preprocessing, feature engineering, model evaluation, and deployment, resulting in a practical and accessible predictive solution.

## Screenshots
<img width="1919" height="986" alt="Screenshot 2025-10-24 180513" src="https://github.com/user-attachments/assets/047a675a-4060-4ec2-a5bd-7652be56f02a" />


   git clone https://github.com/yourusername/Gold-Price-Prediction.git
   cd Gold-Price-Prediction
