! pip install requests
! pip install tabulate
! pip install "colorama>=0.3.8"
! pip install future
! pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o


import h2o
from h2o.automl import H2OAutoML

h2o.init()

# Import a sample binary outcome train/test set into H2O
train = h2o.import_file("train_1.csv")
test = h2o.import_file("test.csv")

# Identify predictors and response
x = train.columns
y = "Class"
x.remove(y)

# For binary classification, response should be a factor
train[y] = train[y].asfactor()
#test[y] = test[y].asfactor()

# Run AutoML for 20 base models (limited to 1 hour max runtime by default)
aml = H2OAutoML(max_models=20, seed=1)
aml.train(x=x, y=y, training_frame=train)

lb = aml.leaderboard
preds = aml.leader.predict(test)
print(preds)

h2o.export_file(preds,"file.csv") 
