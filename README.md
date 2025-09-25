# Student Performance Prediction Project

This project is a complete machine learning pipeline for predicting student math scores based on demographic and academic features. It includes data ingestion, preprocessing, model training, evaluation, and deployment using Flask.

---

## 📁 Project Structure

```
project_1/
│
├── src/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   └── pipeline/
│       ├── __init_.py
│       ├── predict_pipeline.py
│       └── training_pipeline.py
│
├── artifacts/                # Stores trained models, preprocessors, and datasets
├── notebook/                 # Jupyter notebooks for exploration (optional)
├── app.py                    # Flask app for model inference
└── README.md                 # Project documentation
```

---

## 🚀 Features

- **Data Ingestion:** Loads and splits raw data for training and testing.
- **Data Transformation:** Preprocesses data (encoding, scaling, etc.).
- **Model Training:** Trains multiple regression models and selects the best one.
- **Model Evaluation:** Evaluates models using R² score and other metrics.
- **Model Deployment:** Provides a Flask web interface for predictions.
- **Logging & Exception Handling:** Robust logging and custom exceptions for debugging.

---

## 🛠️ Setup & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/FAKER-112/project_1.git
   cd pfproject
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Training Pipeline**
   ```bash
   python -m src.pipeline.training_pipeline
   ```

4. **Start the Flask App**
   ```bash
   python app.py
   ```

5. **Access the Web Interface**
   - Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Model Details

- Models used: Linear Regression, Decision Tree, Random Forest, XGBoost, CatBoost, AdaBoost, KNN, etc.
- Best model and preprocessor are saved in the `artifacts/` directory.

---

## 📝 Author

Seaforth Zanthus


---

## 📬 Contributions

Feel free to open issues or submit pull requests for improvements!

---