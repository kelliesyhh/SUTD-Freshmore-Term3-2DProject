from org.transcrypt.stubs.browser import *
import pandas as pd
import numpy as np

# write down any library you need for the client
# this uses Transcrypt to create the javascript library
def normalize_z(df):
    """Takes a DataFrame, returns a DataFrame with normalized values using z-score normalization."""
    dfout = (df - df.mean(axis=0)) / df.std(axis=0)
    return dfout

def get_features_targets(df, feature_names, target_names):
    """Takes a DataFrame, a list of columns for the features, and a list of columns for the target, returns a DataFrame containing the features and a DataFrame containing the target."""
    df_feature = df.loc[:, feature_names]
    df_target = df.loc[:, target_names]
    return df_feature, df_target

def prepare_feature(df_feature):
    """Takes a DataFrame containing the features, convert it into a numpy array, change it to a column vector, and add a column of '1's in the first column, returns a numpy.array containing the features."""
    cols = len(df_feature.columns)
    np_feature = df_feature.to_numpy().reshape(-1, cols)
    constants = np.ones(shape=(np_feature.shape[0], 1))
    return np.concatenate((constants, np_feature), axis=1)

def prepare_target(df_target):
    """Takes a DataFrame containing the target, convert it into a numpy array, change it to a column vector, returns a Numpy array containing the target."""
    cols = len(df_target.columns)
    np_target = df_target.to_numpy().reshape(-1, cols)
    return np_target

def predict(df_feature, beta):
    """Takes a DataFrame and an array of beta values, returns the predicted y values after z-normalization and conversion to a Numpy array."""
    df_feature = normalize_z(df_feature)
    np_X = prepare_feature(df_feature)
    return predict_norm(np_X, beta)

def predict_norm(X, beta):
    """Takes a Numpy array and an array of beta values, returns the straight line equation after standardization and adding of column for constant 1."""
    y_pred = np.matmul(X, beta)
    return y_pred

def compute_cost(X, y, beta):
    """Takes a Numpy array containing the features, a Numpy array containing the target, and beta coefficients at the end of the iteration, returns an array of computed cost function values."""
    J = 0
    m = X.shape[0]
    y_hat = np.matmul(X, beta)
    J = np.sum((y_hat - y) ** 2)/(2*m)
    error = np.matmul(X, beta) - y
    J = np.matmul(error.T, error)
    J = J / (2*m)
    return J

def gradient_descent(X, y, beta, alpha, num_iters):
    """Takes a Numpy array containing the features, a Numpy array containing the target, an array of beta values, the learning rate, the number of iterations to perform, returns the beta coefficient at the end of the iteration, and an array storing the cost value at each iteration."""
    # m = number of data points
    m = X.shape[0]

    # cost function in each iteration
    J = np.zeros((num_iters, 1)) 
    k = 0
    
    while k < num_iters:        
        y_hat = np.matmul(X, beta)
        deriv = np.matmul(X.T, (y_hat - y)) 
        beta = beta - alpha/m * deriv
        J[k] = compute_cost(X, y, beta)
        k += 1
    return beta, J

def multiple_linear_regression(df_features_test):
    df = pd.read_csv("combined-w-cases.csv")
    df_features, df_target = get_features_targets(df, ["vaccination_policy", "testing_policy", "facial_coverings", "restriction_gatherings"], ["stay_home_requirements"])
    # Normalize the features using z normalization
    df_features_z = normalize_z(df_features)

    # Change the features and the target to numpy array using the prepare functions
    X = prepare_feature(df_features_z)
    target = prepare_target(df_target)

    iterations = 1500
    alpha = 0.1
    beta = np.zeros((X.shape[1], 1), dtype=float)

    # Call the gradient_descent function
    beta, J_storage = gradient_descent(X, target, beta, alpha, iterations)
    
    # call the predict() method
    pred = predict(df_features_test, beta)

    return pred

def save_data():
    """Returns a DataFrame with feature values obtained from the frontend."""
    vaccination_policy = document.getElementsByName("vaccination_policy")
    testing_policy = document.getElementsByName("testing_policy")
    facial_coverings = document.getElementsByName("facial_coverings")
    restriction_gatherings = document.getElementsByName("restriction_gatherings")
    arr = [vaccination_policy, testing_policy, facial_coverings, restriction_gatherings]
    return pd.DataFrame(arr, columns=["vaccination_policy", "testing_policy", "facial_coverings", "restriction_gatherings"])

def get_prediction():
    df_features = save_data()
    pred = multiple_linear_regression(df_features)
    
    document.getElementById("predicted_value").innerHTML = pred