from sklearn.ensemble import RandomForestClassifier
import pickle


class Machine:

    def __init__(self, df):
        self.name = 'RandomForestClassifier'
        self.model = RandomForestClassifier()
        target = df['Rarity']
        features = df.drop(['Rarity'], axis=1)
        self.model.fit(features, target)

    def __call__(self, feature_basis):
        prediction, _ = self.model.predict(feature_basis)
        return prediction

    def save(self, filepath):
        return pickle.dump(self.model, open(filepath, 'wb'))

    @staticmethod
    def open(filepath):
        loaded_model = pickle.load(open(filepath, 'rb'))
        result = loaded_model.score()
        return result

    def info(self):
        pass
#joblib