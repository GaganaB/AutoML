# AutoML

Datasets generally do not provide this structure and hence, the onus is on the user to generate these files. While it simultaneously allows the user to incorporate feature engineering and training parameters into the process, it is also the user's responsibility to do so through the model definition structure optionally recording information about the pre-processing for each feature, and control use of encoder and decoder. The addition of new features, flexibility over model predictions, and training extensibility are reserved for expert users. 


h2o
allows implementations of multiple algorithms like gradient boosting, stacked ensembling, random forests, and deep learning networks which can be easily accessed through their API's which is also extensively documented with massive community support. But also most of the features are limiting in the sense that there are specific data strings that are expected for each sub-configuration and adding new features for the particular problem set usually requires forking the original code base. 


autoML GS generates raw Python code using Jinja templates and trains the statistical model in a subprocess using generated code by trying different hyperparameters to find the best model. It automatically infersfeature types and then uses a ETL strategy for features as determined by the hyperparameters to optimise frameworks.


While survey papers have evaluated multiple tools on multiple datasets and data types, there has not been nearly enough work to compare and comprehend how particular models of each of these tools compare to one another. For instance, there is not enough literature to compare, say, deep learning model of one tool to another on similar data, configurations and settings. Since there are innumerable combinations that are possible and evaluation on one dataset is by no means sufficient, 
