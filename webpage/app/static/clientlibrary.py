from org.transcrypt.stubs.browser import *
from app.serverlibrary import multiple_linear_regression

# write down any library you need for the client
# this uses Transcrypt to create the javascript library

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
