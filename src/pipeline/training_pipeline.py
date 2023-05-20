import os
import sys
from src.logger import logging
from src.Exception import customException
import pandas as pd

from src.components.Data_cleaning import Datacleaning
from src.components.Data_Ingestion import DataIngestion
from src.components.Data_Transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    obj1=DataIngestion()
    obj2=Datacleaning()
    raw_data_path = obj1.data_ingestion_initiate()
    clean_data_path = obj2.data_cleaning_initiate()
    train_data_path,test_data_path=obj1.data_splitting_initiate()
    data_transformation = DataTransformation()
    train_arr,test_arr,_= data_transformation.initaite_data_transformation(train_data_path,test_data_path)
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)