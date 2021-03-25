from catboost import CatBoostClassifier, Pool
import numpy as np
import pandas as pd

from webapp.settings import DATA_PATH, MODEL_PATH


class Predictor:
    def __init__(self, model_path, data_path):
        self.classifier = CatBoostClassifier()
        self.classifier.load_model(model_path)
        self.data_path = data_path
        self.data = None
        self.data_pool = None
        self.policy_id = None

    def _read_data(self, sep=','):
        if isinstance(self.data, pd.DataFrame) and isinstance(self.policy_id, np.ndarray):
            return self.data, self.policy_id
        with open(self.data_path, 'r') as file:
            self.data = pd.read_csv(file, sep=sep, index_col='POLICY_ID')
            data_ = self.data.reset_index()
            self.policy_id = data_['POLICY_ID'].to_numpy()
        return self.data, self.policy_id

    def _conv_data_to_pool(self):
        if not isinstance(self.data, pd.DataFrame):
            self._read_data()
        cat_features = self.data.select_dtypes(exclude=[np.number]).columns
        self.data_pool = Pool(data=self.data.astype('str'), cat_features=cat_features)
        return self.data_pool

    def _predict(self):
        return self.classifier.predict(self.data_pool)

    def _predict_proba(self):
        probabilities = self.classifier.predict_proba(self.data_pool)
        return probabilities[:, 1]

    def get_forecast(self):
        if isinstance(self.data_pool, Pool):
            return self._predict()
        self._conv_data_to_pool()
        return self._predict()

    def get_probability(self):
        if isinstance(self.data_pool, Pool):
            return self._predict_proba()
        self._conv_data_to_pool()
        return self._predict_proba()


predictor = Predictor(MODEL_PATH, DATA_PATH)
