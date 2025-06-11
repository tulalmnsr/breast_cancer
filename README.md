# breast_cancer
# Breast Cancer Prediction API

This project builds a Decision Tree model to predict whether a patient has benign or malignant breast cancer based on diagnostic attributes. It includes:

- 10-Fold Cross Validation
- Entropy and Information Gain Calculation
- Model Training
- FastAPI-based GET endpoint for predictions

## 📁 Files Included

- `breast_cancer_clean.csv`: Cleaned dataset.
- `decision_tree_model.pkl`: Trained decision tree model.
- `entropy_gain.py`: Script to calculate entropy and information gain.
- `main.py`: FastAPI app to serve predictions.
- `requirements.txt`: Dependencies to run the project.

## 📊 Accuracy

- Mean Accuracy: ~94.1%
- Std. Deviation: ±2.95%

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the API server:
   ```bash
   uvicorn main:app --reload
   ```

3. Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

## 📥 Example API Call

```bash
GET /predict?Clump_Thickness=5&Cell_Size_Uniformity=1&Cell_Shape_Uniformity=1&Marginal_Adhesion=1&Single_Epi_Cell_Size=2&Bare_Nuclei=1&Bland_Chromatin=3&Normal_Nucleoli=1&Mitoses=1
```

Returns:
```json
{"prediction": "Benign"}
```

---

Made for educational purposes. Assignment complete ✅
