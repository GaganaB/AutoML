!pip install --upgrade mxnet-cu100
!pip install autogluon

import pandas as pd
import numpy as np
from autogluon import TabularPrediction as task
from autogluon.utils.tabular.metrics import roc_auc

label_column = 'Class' # name of target variable to predict in this competition
eval_metric = 'roc_auc' # Optional: specify that competition evaluation metric is AUC

train = pd.read_csv('train_1.csv')
test = pd.read_csv('test.csv')
train_data = task.Dataset(df = train) 
predictor = task.fit(train_data=train_data, label=label_column, eval_metric=eval_metric, verbosity=3, auto_stack=True, time_limits=3600)
test_data = task.Dataset(df = test)
y_predproba = predictor.predict_proba(test_data)
submission = pd.read_csv('submission_example.csv')
submission['Class'] = y_predproba
submission.head()
submission.to_csv('my_submission.csv', index=False)

from google.colab import files
files.download('my_submission.csv') 
