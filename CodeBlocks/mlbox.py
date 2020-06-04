!pip install mlbox
from IPython.core.display import display, HTML
display(HTML('<style>.prompt{width: 0px; min-width: 0px; visibility: collapse}</style>'))

import warnings
warnings.filterwarnings("ignore")

from mlbox.preprocessing.reader import Reader
from mlbox.preprocessing.drift_thresholder import Drift_thresholder
from mlbox.optimisation.optimiser import Optimiser 
from mlbox.prediction.predictor import Predictor
#from mlbox.encoding import Categorical_encoder
from mlbox.model.classification import StackingClassifier, Classifier
import pandas as pd 

paths = ["train_1.csv", "test.csv"]
target_name = "Class"

rd = Reader(sep=",")
df = rd.train_test_split(paths, target_name)
print(df["train"].head())

dft = Drift_thresholder()
df = dft.fit_transform(df)

opt = Optimiser()
warnings.filterwarnings('ignore', category=DeprecationWarning)
score = opt.evaluate(None, df)

space = {
        'ne__numerical_strategy':{"search":"choice",
                                 "space":[0, "mean"]},
        'ce__strategy':{"search":"choice",
                        "space":["label_encoding", "random_projection", "entity_embedding"]}, 
        'fs__threshold':{"search":"uniform",
                        "space":[0.001, 0.2]}, 
        'est__strategy':{"search":"choice", 
                         "space":["RandomForest", "ExtraTrees", "LightGBM"]},
        'est__max_depth':{"search":"choice", 
                          "space":[8, 9, 10, 11, 12, 13]}
        }
"""
#Clf_feature_selector(strategy='l1', threshold=0.3)
#Categorical_encoder(strategy = "")
StackingClassifier([Classifier(strategy="AdaBoost"), Classifier(strategy="AdaBoost"),Classifier(strategy="AdaBoost")]) 
space = {     'fs__strategy':{"search":"choice","space":["variance","rf_feature_importance"]},'est__colsample_bytree':{"search":"uniform", "space":[0.3,0.7]}}
"""
params = opt.optimise(space, df, 15)
#print(opt.evaluate(params, df))
prd = Predictor()
y_predproba = prd.fit_predict(params, df)

""" download file from left hand panel """
