import os
import sys
from src.logger import logging
from src.Exception import customException
import numpy as np 
import pandas as pd
from dataclasses import dataclass

@dataclass
class Datacleaningconfig:
    clean_data_path:str=os.path.join('artifact','clean.data.csv')

class Datacleaning:
    def __init__(self):
        self.cleaning_config = Datacleaningconfig()
        
    def data_cleaning_initiate(self):
        logging.info('Data cleaning method starts')
        try:
            df=pd.read_csv(os.path.join("artifact\Census_data.csv"))
            df.columns = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation",
                          "relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","income"]
            os.makedirs(os.path.dirname(self.cleaning_config.clean_data_path),exist_ok=True)
            df.to_csv(self.cleaning_config.clean_data_path,index=False)
            
            df[df==' ?']=np.nan
            df = df.dropna(axis=0)
            df = df.drop(labels=['fnlwgt','education','relationship'],axis=1)
            df['income'] = df['income'].replace({' <=50K':0,' >50K':1})
            df = df.rename(columns={'education-num':'education_num','capital-gain':'capital_gain','capital-loss':'capital_loss',
                                    'hours-per-week':'hours_per_week','native-country':'native_country','marital-status':'marital_status'})
            
            df['native_country'] = df['native_country'].replace({' United-States':1, ' Cuba':2, ' Jamaica':3, ' India':4, ' Mexico':5,
                                 ' Puerto-Rico':6, ' Honduras':7, ' England':8, ' Canada':9, ' Germany':10,
                                 ' Iran':11, ' Philippines':12, ' Poland':13, ' Columbia':14, ' Cambodia':15,
                                 ' Thailand':16, ' Ecuador':17, ' Laos':18, ' Taiwan':19, ' Haiti':20, ' Portugal':21,
                                 ' Dominican-Republic':22, ' El-Salvador':23, ' France':24, ' Guatemala':25,
                                 ' Italy':26, ' China':27, ' South':28, ' Japan':29, ' Yugoslavia':30, ' Peru':31,
                                 ' Outlying-US(Guam-USVI-etc)':32, ' Scotland':33, ' Trinadad&Tobago':34,
                                 ' Greece':35, ' Nicaragua':36, ' Vietnam':37, ' Hong':38, ' Ireland':39,
                                 ' Hungary':41, ' Holand-Netherlands':42})
            df['occupation'] = df['occupation'].replace({' Exec-managerial':1, ' Handlers-cleaners':2, ' Prof-specialty':3,
                                           ' Other-service':4, ' Adm-clerical':5, ' Sales':6, ' Transport-moving':7,
                                           ' Farming-fishing':8, ' Machine-op-inspct':9, ' Tech-support':10,
                                           ' Craft-repair':11, ' Protective-serv':12, ' Armed-Forces':13,' Priv-house-serv':14})
            
            os.makedirs(os.path.dirname(self.cleaning_config.clean_data_path),exist_ok=True)
            df.to_csv(self.cleaning_config.clean_data_path,index=False)
            
            logging.info('Data cleaning completed')
            
            return(
                self.cleaning_config.clean_data_path
                
            )
            
            
        except Exception as e:
            logging.info('Exception at Data Ingestion stage')
            raise customException(e,sys)
            
            
        
        