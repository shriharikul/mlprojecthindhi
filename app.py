from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.model_trainer import ModelTrainer

import sys

if __name__ == "__main__":
    logging.info("Execution started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer()

    except Exception as e:
        raise CustomException(e, sys)