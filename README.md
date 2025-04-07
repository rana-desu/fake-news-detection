# fake-news-detection (WIP!)
Implementation of detecting fake news on a Kaggle dataset.

## Algorithms/Libraries to utilise for the implementation:
1. TF-IDF (Term Frequency-Inverse Document Frequency)
2. CatBoost (Categorical Boosting)
3. XGBoost (eXtreme Gradient Boosting)

### TF-IDF
TF-IDF is used to vectorise the dataset features and provide with a numerical value for each respective feature. These TF-IDF values are then further used to train various *ensemble models*.

### What are Ensemble Models?
Ensemble models are a combination of multiple machine learning algorithms (example: Decision Trees). The combination is done to improve performance, robustness, and generalisation of the weaker individual ML algorithms.

- **Random Forest**: Trains models in parallel on random subsets of data; this reduces *variance*.
- **CatBoost** & **XGBoost**: Trains models sequentially, correcting errors from previous models; this reduces *bias*.

### What are Decision Trees? 
Supervised machine learning algorithm used in NLP for classification and regression tasks. They work by recursively splitting data into subsets based on *feature values*, forming a tree-like structure of *decisions*.

## TODO
- [x] Spacy for Preprocessing Text
- [ ] Vectorise features using TF-IDF
    - [x] Learn about how TF-IDF works
    - [x] classifier: Logistic Regression 
- [ ] Ensemble Models
    - [ ] Random Forest
    - [ ] CatBoost
    - [ ] XGBoost
- [ ] Comparison through visualisation of the trained models
- [ ] Jupyter notebook for presentation

OPTIONAL
- [ ] Build a functionality for custom user inputs (?)
