
AUTOGLUON


Selected class <--> label mapping:  class 1 = 1, class 0 = 0
Feature Generator processed 86 data points with 789 features
Original Features:
	int features: 1
	float features: 788
Generated Features:
	int features: 0
All Features:
	int features: 1
	float features: 788
	Data preprocessing and feature engineering runtime = 1.95s ...
AutoGluon will gauge predictive performance using evaluation metric: accuracy
To change this, specify the eval_metric argument of fit()
AutoGluon will early stop models using evaluation metric: accuracy
/usr/lib/python3.7/imp.py:342: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
  return _load(spec)
Fitting model: RandomForestClassifierGini ...
	0.7778	 = Validation accuracy score
	1.04s	 = Training runtime
	0.26s	 = Validation runtime
Fitting model: RandomForestClassifierEntr ...
	0.7778	 = Validation accuracy score
	1.02s	 = Training runtime
	0.26s	 = Validation runtime
Fitting model: ExtraTreesClassifierGini ...
	0.7222	 = Validation accuracy score
	0.81s	 = Training runtime
	0.26s	 = Validation runtime
Fitting model: ExtraTreesClassifierEntr ...
	0.8333	 = Validation accuracy score
	0.81s	 = Training runtime
	0.26s	 = Validation runtime
Fitting model: KNeighborsClassifierUnif ...
	0.5556	 = Validation accuracy score
	0.3s	 = Training runtime
	0.41s	 = Validation runtime
Fitting model: KNeighborsClassifierDist ...
	0.3333	 = Validation accuracy score
	0.3s	 = Training runtime
	0.4s	 = Validation runtime
Fitting model: LightGBMClassifier ...
	0.8333	 = Validation accuracy score
	0.65s	 = Training runtime
	0.15s	 = Validation runtime
Fitting model: CatboostClassifier ...
	0.8889	 = Validation accuracy score
	7.27s	 = Training runtime
	0.17s	 = Validation runtime
Fitting model: NeuralNetClassifier ...
	0.8333	 = Validation accuracy score
	1.53s	 = Training runtime
	0.13s	 = Validation runtime
Fitting model: LightGBMClassifierCustom ...
	0.6111	 = Validation accuracy score
	1.18s	 = Training runtime
	0.15s	 = Validation runtime
Fitting model: weighted_ensemble_k0_l1 ...
	0.9444	 = Validation accuracy score
	0.57s	 = Training runtime
	0.0s	 = Validation runtime
AutoGluon training complete, total runtime = 22.77s ...


