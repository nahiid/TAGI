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



from mt import *
import time
#114

# Evaluation
RMSElist[s] = computeError(ytest, ynTest)
LLlist[s] = loglik(ytest, ynTest, SynTest)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
new = current_time - old
trainTimelist[s] = new