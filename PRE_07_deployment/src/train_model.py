import os
import pickle

import pandas as pd  # type: ignore
from sklearn.linear_model import LinearRegression  # type: ignore

FOLDER = "PRE_07_deployment"

df = pd.read_csv(f"{FOLDER}/data/input/house_data.csv")

features = df[
    [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "waterfront",
        "condition",
    ]
]

target = df[["price"]]

estimator = LinearRegression()
estimator.fit(features, target)

if not os.path.exists(f"{FOLDER}/data/output"):
    os.makedirs(f"{FOLDER}/data/output")

with open(f"{FOLDER}/data/output/house_predictor.pkl", "wb") as file:
    pickle.dump(estimator, file)
