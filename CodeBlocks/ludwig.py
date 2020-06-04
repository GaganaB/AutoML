!pip install ludwig

!ludwig experiment --data_csv train_1.csv --model_definition_file convertcsv.yaml

!zip -r results.zip results_0

from google.colab import files
files.download('results.zip')  
