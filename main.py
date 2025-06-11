
from fastapi import FastAPI, Query
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("decision_tree_model.pkl")

@app.get("/predict")
def predict(
    Clump_Thickness: float = Query(...),
    Cell_Size_Uniformity: float = Query(...),
    Cell_Shape_Uniformity: float = Query(...),
    Marginal_Adhesion: float = Query(...),
    Single_Epi_Cell_Size: float = Query(...),
    Bare_Nuclei: float = Query(...),
    Bland_Chromatin: float = Query(...),
    Normal_Nucleoli: float = Query(...),
    Mitoses: float = Query(...)
):
    features = np.array([[
        Clump_Thickness, Cell_Size_Uniformity, Cell_Shape_Uniformity,
        Marginal_Adhesion, Single_Epi_Cell_Size, Bare_Nuclei,
        Bland_Chromatin, Normal_Nucleoli, Mitoses
    ]])
    prediction = model.predict(features)[0]
    result = "Malignant" if prediction == 1 else "Benign"
    return {"prediction": result}
