# . Here
from datetime import datetime

import numpy as np
from dp import *
from sklearn.model_selection import train_test_split

"""Regression problem
This function trains neural network models to solve a regression problem.
@param NN Lists the structure of the neural network
@param x Input data
@param y Response data
@param trainIdx Observations IDs that are assigned to the training set
@param testIdx Observations IDs that are assigned to the testing set
@return - Mean vector of parameters for each layer \eqn{\mu_{\theta}}
@return - Covariance matrix of parameters for each layer \eqn{\Sigma_{\theta}}
@return - RMSE and LL metrics for each network models created
@return - Training time of each neural network models created
@return - Mean of predicted responses
@return - Variance of the predicted responses
@export"""


def regression(NN, x, y, trainIdx, testIdx):
    # Initialization
    initsv = NN[sv]
    initmaxEpoch = NN[maxEpoch]
    NN[errorRateEval] = 0

    # Indices for each parameter group
    # Train net
    NN[trainMode] = 1
    NN[batchSize] = NN[batchSizeList[1]]
    NN = initialization_net(NN)
    NN = parameters(NN)
    NN = covariance(NN)

    # Validation net
    NNval = NN
    NNval[trainMode] = 0
    NNval[batchSize] = NN[batchSizeList[2]]
    NNval = parameters(NNval)
    NNval = covariance(NNval)

    # Test net
    NNtest = NN
    NNtest[trainMode] = 0
    NNtest[batchSize] = NN[batchSizeList[3]]
    NNtest = parameters(NNtest)
    NNtest = covariance(NNtest)

    # Loop
    Nsplit = NN[numSplits]
    RMSElist = np.repeat(0, Nsplit)
    LLlist = np.repeat(0, Nsplit)
    trainTimelist = np.repeat(0, Nsplit)
    permuteData = 0

    if trainIdx == None or testIdx == None:
        permuteData = 1

    for s in range(1, Nsplit):
        old = datetime.now()
        if permuteData == 1:
            out_split = split(x, y, NN[ratio])
            xtrain = out_split[0]
            ytrain = out_split[1]
            xtest = out_split[2]
            ytest = out_split[3]

        else:
            xtrain = x[
                trainIdx[s],
            ]
            ytrain = np.array(y[trainIdx[s]], ncol=NN[ny])
            xtest = x[
                testIdx[s],
            ]
            ytest = np.array(y[testIdx[s]], ncol=NN[ny])

    # Normalization
    out_normalize = normalize(xtrain, ytrain, xtest, ytest)
    xtrain = out_normalize[0]
    ytrain = out_normalize[1]
    xtest = out_normalize[2]
    mytrain = out_normalize[6]
    sytrain = out_normalize[7]


import time

from mt import *

# 114

# Evaluation
RMSElist[s] = computeError(ytest, ynTest)
LLlist[s] = loglik(ytest, ynTest, SynTest)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
new = current_time - old
trainTimelist[s] = new
