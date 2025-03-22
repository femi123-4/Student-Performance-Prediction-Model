# Student Performance Prediction Model

## Project Overview

This project uses machine learning to predict student academic performance based on factors such as study habits, stress levels, and lifestyle choices. The model is built using **Linear Regression** and trained on a dataset of over **10,000 students**, achieving an **R-squared value of 0.94**. The model is deployed in a **Flask** web application, providing an interactive interface for users to input data and receive personalized performance predictions. This project is intended for educational purposes.

## Features

- **Predictive Model**: Predicts student performance based on study habits, stress levels, and other factors.
- **Machine Learning**: Built using **Linear Regression** with data preprocessing (one-hot encoding, normalization) for better accuracy.
- **Flask Web App**: An interactive web interface that allows users to input their data and get predictions.
- **Data Handling**: Processes over **10,000 records** from students to train the model.

## Technologies Used

- **Python**  
- **Scikit-learn** (for machine learning)  
- **Flask** (for web app development)  
- **Pandas** (for data manipulation)  
- **NumPy** (for numerical operations)  
- **Matplotlib/Seaborn** (for data visualization)  
- **HTML/CSS** (for front-end design)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/student-performance-prediction.git
   ```

2. Navigate into the project directory:

   ```bash
   cd student-performance-prediction
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask web application:

   ```bash
   python app.py
   ```

   The app will be accessible at `http://127.0.0.1:5000/`.

## Usage

1. Open the web app in your browser.
2. Input the required data (e.g., study hours, stress levels, etc.).
3. Click on "Predict" to get the estimated academic performance.

## Note

- This model is for educational purposes only and may not provide accurate predictions in real-world scenarios.
- The model was trained on a dataset of 10,000+ students and achieved an **R-squared value of 0.94**.
