import sys
import os
from src.Exception import customException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifact','preprocessor.pkl')
            model_path=os.path.join('artifact','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise customException(e,sys)
        
class CustomData:
    def __init__(self,
                 age:int,
                 workclass:str,
                 education_num:int,
                 marital_status:str,
                 occupation:int,
                 race:str,
                 sex:str,
                 capital_gain:int,
                 capital_loss:int,
                 hours_per_week:int,
                 native_country:int
                 ):
        
        self.age=age
        self.workclass=workclass
        self.education_num=education_num
        self.marital_status=marital_status	
        self.occupation=occupation
        self.race=race
        self.sex=sex
        self.capital_gain=capital_gain
        self.capital_loss=capital_loss
        self.hours_per_week=hours_per_week
        self.native_country=native_country
        
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'age':[self.age],
                'workclass':[self.workclass],
                'education_num':[self.education_num],
                'marital_status':[self.marital_status],
                'occupation':[self.occupation],
                'race':[self.race],
                'sex':[self.sex],
                'capital_gain':[self.capital_gain],
                'capital_loss':[self.capital_loss],
                'hours_per_week':[self.hours_per_week],
                'native_country':[self.native_country]
                
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customException(e,sys)
