#!/usr/bin/python
# -*- coding: utf-8 -*-
# from pandas.core.indexes import multi
from org.transcrypt.stubs.browser import *
import random
import numscrypt as num
# import pandas as pd
import math

array = []


def update_vals():
    """use this function"""

    vac = document.getElementById('vaccination_policy')
    vaccination_policy = vac.options[vac.selectedIndex].value
    test = document.getElementById('testing_policy')
    testing_policy = test.options[test.selectedIndex].value
    facial = document.getElementById('facial_coverings')
    facial_coverings = facial.options[facial.selectedIndex].value
    restriction = document.getElementById('restriction_gatherings')
    restriction_gatherings = restriction.options[restriction.selectedIndex].value
    arr = []
    arr.append(testing_policy)
    arr.append(vaccination_policy)
    arr.append(facial_coverings)
    arr.append(restriction_gatherings)
    print(arr)
    return arr

def prepare_feature(df_feature):
    print(df_feature.shape)
    num_feature = df_feature.reshape(-1, df_feature.shape[1])
    constants = num.ones(shape=(4, 1))
    print(num_feature)
    list_feature = list(num_feature)
    new = []
    new.append(list_feature)
    new.append(list(constants))
    # np_x = num.array(new)
    # return num.concatenate((constants, num_feature), axis=1)
    return new

def log_regression(beta, X):
    X_beta = X @ beta
    # den = 1 + num.exp(-X_beta)
    exp_beta = [math.pow(math.e, i) for i in -X_beta]
    den = 1 + num.array(exp_beta)
    return 1 / den

def predict_multiclass(df_features, multi_beta):
    preds = []
    for i in range(len(multi_beta)):
        beta = multi_beta[i]
        num_X = prepare_feature(df_features)
        probability = log_regression(num.array(beta), num.array(num_X))
        preds.append(probability)

    columns = num.argmax(preds, axis=0)
    return columns

def predict():
    """use this function 2"""

    arr = update_vals()
    testing_policy = arr[0]
    vaccination_policy = arr[1]
    facial_coverings = arr[2]
    restriction_gatherings = arr[3]
    # df = pd.DataFrame(arr)
    multi_beta = [[-0.79472992, 0.10544153, 0.23763321, -0.24923119, -0.75778749], [-0.86816833, 0.12075281, -0.01930381, -0.18233127, 0.12980541], [-0.65807991, -0.20576482, -0.17083554, 0.49237502, 0.62356364], [-2.33470857e+00, 1.10108957e-03, -5.20146082e-02, -5.05758208e-02, 1.77853267e-01]]
    y = predict_multiclass(num.array(arr), multi_beta)
    print(y)
    # beta0 = 1.10706528
    # beta1 = -0.07528005
    # beta2 = -0.10102505
    # beta3 = 0.12522986
    # beta4 = 0.34782008
    # y = beta0 + beta1*testing_policy + beta2*vaccination_policy + beta3*facial_coverings + beta4*restriction_gatherings

    yfloor = y // 1

    keyval = {
        0: 'No measures',
        1: 'Recommended not to leave the house',
        2: "Required not to leave the house with exceptions for daily exercise, grocery shopping, and 'essential' trips",
        3: 'Required to not leave the house with minimal exceptions (e.g. allowed to leave only once every few days, or only one person can leave at a time, etc.)',
        }

    result = keyval[yfloor]
    print(result)

    document.getElementById('predict').innerHTML = result


def update_vals_cases():
    """use this function"""

    vac = document.getElementById('vaccination__policy')
    vaccination_policy = vac.options[vac.selectedIndex].value
    test = document.getElementById('testing__policy')
    testing_policy = test.options[test.selectedIndex].value
    restriction = document.getElementById('restriction__gatherings')
    restriction_gatherings = \
        restriction.options[restriction.selectedIndex].value
    facial = document.getElementById('facial__coverings')
    facial_coverings = facial.options[facial.selectedIndex].value
    stayh = document.getElementById('stay__home')
    stay_home = stayh.options[stayh.selectedIndex].value
    arr = []
    arr.append(testing_policy)
    arr.append(vaccination_policy)
    arr.append(facial_coverings)
    arr.append(restriction_gatherings)
    arr.append(stay_home)
    print(arr)
    return arr


def predictcases():
    arr = update_vals_cases()
    vaccination_policy = arr[1]
    testing_policy = arr[0]
    facial_coverings = arr[2]
    restriction_gatherings = arr[3]
    stay_home = arr[4]

    betalist = [
        [
            [30608.89458865247],
            [4022.245021206385],
            [22604.46143460738],
            [2038.5007539600358],
            [1724.5407032741266],
            [-2060.5702325792276],
            ],
        [
            [2126.1479976470573],
            [212.52682048321137],
            [64.0480564319336],
            [-349.29540328823316],
            [117.37342120853494],
            [4500.978535000691],
            ],
        [
            [1320.4341820330962],
            [334.22721511969655],
            [391.6756071595284],
            [215.01043623774277],
            [22.280078372985308],
            [-93.09602382005562],
            ],
        [
            [38873.75563744073],
            [-1147.6946164099293],
            [33974.17242920879],
            [-2148.796384008256],
            [298.92598082548784],
            [-2573.0287765229787],
            ],
        [
            [37030.64083058821],
            [13280.528034639903],
            [13136.973671756265],
            [13309.15002301045],
            [-6851.9265296863505],
            [2069.0495534135794],
            ],
        [
            [75472.12638242275],
            [8234.476260345102],
            [62100.52511675339],
            [-1634.3100943027575],
            [18802.55420846467],
            [-5646.598107441958],
            ],
        [
            [6296.601056737585],
            [863.4408567719405],
            [3622.3875962017114],
            [796.4649659250509],
            [-837.2814682504256],
            [69.74851053825321],
            ],
        [
            [42172.02809715637],
            [2074.190537910149],
            [29899.395908022507],
            [5776.860216972819],
            [4915.534560783575],
            [-2781.028280686621],
            ],
        [
            [38900.272849765235],
            [7885.005214425789],
            [28354.865509276267],
            [1087.7550346751173],
            [1625.7932935226736],
            [2085.1869376160275],
            ],
        [
            [4655.226177985945],
            [-314.79891651168606],
            [4895.715968317134],
            [-99.83761799585072],
            [335.39825242126807],
            [-124.55054187683751],
            ],
        [
            [16357.862070921981],
            [-3065.1812650722577],
            [13423.068095869934],
            [5157.465279930686],
            [-1461.724938814956],
            [5751.688908969529],
            ],
        [
            [12193.019330166266],
            [134.34690441338773],
            [5071.721303517931],
            [-15.510685066082946],
            [13.762416689871069],
            [-4107.787751291015],
            ],
        [
            [33343.22008490563],
            [-1435.041999988873],
            [31042.175570218857],
            [3224.6611837600344],
            [-918.0819644976933],
            [-1012.7760472564387],
            ],
        [
            [18181.944201405156],
            [-34849.24088364351],
            [15185.165273626724],
            [52821.63752963086],
            [-20545.14934380356],
            [-4981.458648573809],
            ],
        [
            [3029.0984481132064],
            [185.5162264695818],
            [1356.008466105423],
            [735.4361553061194],
            [-395.98349291407],
            [801.9790572568505],
            ],
        [
            [9388.391638297866],
            [-211.84656464931567],
            [2019.526734463459],
            [2229.5617117038805],
            [131.83733607128838],
            [-1153.8319541229132],
            ],
        [
            [78860.8234103773],
            [3707.4107474071325],
            [52740.124578820025],
            [12564.698996670346],
            [2258.15933273183],
            [5548.9796937166275],
            ],
        [
            [52493.28720952378],
            [8608.04621712186],
            [38029.41412043264],
            [5772.774724391252],
            [-1115.779283119614],
            [227.01595407833437],
            ],
        [
            [36802.43377068555],
            [6440.131898981612],
            [44157.52008344596],
            [-1358.1018368167172],
            [-4488.743283296551],
            [2798.146413457822],
            ],
        [
            [5072.177496453898],
            [869.1595483754767],
            [2806.9711160701204],
            [1182.9067770683241],
            [-732.3316114544484],
            [371.8501380158209],
            ],
        [
            [21327.6051965],
            [3755.24141949],
            [18513.43631444],
            [-1335.93848313],
            [3203.42058438],
            [-2556.16610382],
            ],
        ]

    countryn = document.getElementById('country')
    countryname = countryn.options[countryn.selectedIndex].value

    beta = betalist[countryname]
    print(beta)
    y = beta[0][0] + beta[1][0] * testing_policy + beta[2][0] \
        * vaccination_policy + beta[3][0] * facial_coverings \
        + beta[4][0] * restriction_gatherings + beta[5][0] * stay_home
    print(y)
    document.getElementById('predictcases').innerHTML = int(y)
