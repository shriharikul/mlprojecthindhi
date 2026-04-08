import pandas as pd
import os
import sys
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from src.mlproject.logger import logging
from src.mlproject.exception import CustomException


@dataclass
class ModelTrainerConfig:
    model_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def initiate_model_trainer(self):
        try:
            logging.info("Model training started")

            df = pd.read_csv("artifacts/data.csv")

            # Drop ID
            df = df.drop(columns=["Student_ID"])

            # Encode categorical
            le = LabelEncoder()
            for col in df.columns:
                df[col] = le.fit_transform(df[col].astype(str))

            # Split
            X = df.drop(columns=["Grade"])
            y = df["Grade"]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            # Train model
            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            score = model.score(X_test, y_test)

            print("Model Training Completed")
            print(" Accuracy:", score)

            logging.info(f"Model accuracy: {score}")

        except Exception as e:
            raise CustomException(e, sys)