import pandas as pd
import os
import sys
from dataclasses import dataclass

from src.mlproject.logger import logging
from src.mlproject.exception import CustomException


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            
            df = pd.read_csv("notebook/data/student.csv")

            os.makedirs("artifacts", exist_ok=True)

            
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Data ingestion completed")

        except Exception as e:
            raise CustomException(e, sys)