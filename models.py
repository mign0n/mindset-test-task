from catboost import CatBoostClassifier, Pool
import numpy as np
import pandas as pd

MODEL_PATH = 'mlmodel/catboost_model'
DATA_PATH = 'data/data_to_predict.csv'


class Predictor:
    def __init__(self, model_path, data_path):
        self.classifier = CatBoostClassifier()
        self.classifier.load_model(model_path)
        self.data_path = data_path
        self.data = None

    def _predict(self):
        cat_features = self.data.select_dtypes(exclude=[np.number]).columns
        data_pool = Pool(data=self.data.astype('str'), cat_features=cat_features)
        return self.classifier.predict(data_pool)

    def _read_data(self, sep):
        with open(self.data_path, 'r') as file:
            self.data = pd.read_csv(file, sep=sep)
        return self.data

    def get_forecast(self):
        self._read_data(sep=',')
        return self._predict()


predictor = Predictor(MODEL_PATH, DATA_PATH)
