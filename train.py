import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data.csv")

X = df[["length", "proto"]]
y = df["label"]

model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully!")
