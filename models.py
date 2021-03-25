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
        self.data_pool = None

    def _read_data_to_pool(self, sep):
        if isinstance(self.data, pd.DataFrame):
            return self.data
        with open(self.data_path, 'r') as file:
            self.data = pd.read_csv(file, sep=sep)
            cat_features = self.data.select_dtypes(exclude=[np.number]).columns
            self.data_pool = Pool(
                data=self.data.astype('str'), cat_features=cat_features
            )
        return self.data_pool

    def _predict(self):
        return self.classifier.predict(self.data_pool)

    def _predict_proba(self):
        probabilities = self.classifier.predict_proba(self.data_pool)
        return probabilities[:, 1]

    def get_forecast(self):
        if isinstance(self.data_pool, Pool):
            return self._predict()
        self._read_data_to_pool(sep=',')
        return self._predict()

    def get_probability(self):
        if isinstance(self.data_pool, Pool):
            return self._predict_proba()
        self._read_data_to_pool(sep=',')
        return self._predict_proba()


predictor = Predictor(MODEL_PATH, DATA_PATH)
