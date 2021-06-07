from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.linear_model import LogisticRegression, LinearRegression

def knnimputer(scaler, regression):
    '''Builds a basic ML pipeline with KNNImputer and scaler and regression of choice'''
    if scaler == 'min_max':
        scaler = MinMaxScaler()
    elif scaler == 'standard':
        scaler = StandardScaler()
    elif scaler == 'robust':
        scaler == RobustScaler()
    else:
        print('Wrong scaler input')
        return None
    if regression == 'linear':
        regression = LinearRegression()
    elif regression == 'logistic':
        regression = LogisticRegression()
    else:
        print('Wrong regression input')
        return None
    
    preprocessor = Pipeline([
    ('imputer', KNNImputer()),
    ('scaler', scaler)
    ])
    final_pipe = Pipeline([
        ('preprocessing', preprocessor),
        ('logistic_regression', regression)])
    
    return final_pipe