!pip3 install atm

from atm import ATM

atm = ATM()

!unzip test.zip

from atm import ATM
import pandas as pd
atm = ATM()
train = pd.read_csv("train_1.csv")
test = pd.read_csv("test.csv")
results = atm.run(train_path="train_1.csv",class_column="Class")


results.describe()

results.get_best_classifier()
results.export_best_classifier('model.pkl')
from atm import Model

model = Model.load('model.pkl')
predictions = model.predict(test)
df = pd.DataFrame(predictions)
df.to_csv ('dataframe.csv', index = False, header=True)
from google.colab import files
files.download('dataframe.csv') 
