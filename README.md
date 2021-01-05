# MULTIMODAL CLASSIFICATION OF SCHIZOPHRENIA USING AUTOMATED DEEP LEARNING CONFIGURATIONS

# Introduction
Schizophrenia is a heterogeneous cognitive disorder where clinical classification is challenging because of:
1. Lack of well-established, non-invasive diagnoses biomarkers despite the condition, with its elusive pathophysiology is surprisingly common. 

2. Overlapping symptomatic factors

3. Diverse internal clinical manifestations

4. Complex diagnostic process leading to delayed treatment.

Thus, experimentation with automated machine learning architectural frameworks (AutoML) is presented in order to handle multimodal Functional Network Connectivity(FNC) and Source Based Morphometry(SBM) features based on functional magnetic resonance imaging(fMRI) and structural magnetic resonance imaging(sMRI) components respectively. 

# Process

The comparison of various AutoML frameworks and configurations is often tricky because: 

(a) Blackbox systems in the background differ in their optimization methodologies, pipeline generation techniques, internal architectures and processing procedures while operating on similar data. The results may also vary on other parameters including training time, memory and computational resources. 

(b) Reruns of the same configurations on data often yield different results. This tends to affect result reproducibility and complicate evaluation process. 

(c) Some frameworks automate the entire pipeline seamlessly while others tend to rely on external engineering techniques. In the latter case, performance evaluation is not a wholesome indicator of the framework's capabilities. Across the machine learning pipeline, most of the AutoML tools have fairly similar processes with respect to data cleaning, data coding, metric selections but differ in their algorithm selection, parameter optimisation and post processing abilities.  

# Download and run
```
git clone https://github.com/GaganaB/AutoML.git
```
For ATM:

Run the colab notebook [here](https://colab.research.google.com/drive/1DJay_uazBgZD99t5rlvybR9vEMRUdgE7?usp=sharing) 

For AutoGluon:
```
python3 autogluon.py
```
For H2O:
```
python3 h2o.py
```
For Ludwig:
```
python3 ludwig.py
```
For mlbox:
```
python3 mlbox.py
```


# Results
On evaluating the resultant AutoML models with respect to approximately 280 machine learning architectures on the Overall AUC metric, the former outperforms the latter despite remarkable limitations including complex high dimensional feature space with very little data. 
