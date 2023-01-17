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

def regression(NN, x, y, train_idx, test_idx):
    # Initialization
    initsv = NN[sv]
    initmax_epoch = NN[max_epoch]
    NN[error_rate_eval] = 0

  # Indices for each parameter group
  # Train net
    NN[train_mode] = 1
    NN[batchSize] = NN[batch_size_list[1]]
    NN = initialization_net(NN)
    NN = parameters(NN)
    NN = covariance(NN)    

    # Validation net
    nn_val = NN
    nn_val[train_mode] = 0
    nn_val[batchSize] = NN[batch_size_list[2]]
    nn_val = parameters(nn_val)
    nn_val = covariance(nn_val)

    # Test net
    nn_test = NN
    nn_test[train_mode] = 0
    nn_test[batchSize] = NN[batch_size_list[3]]
    nn_test = parameters(nn_test)
    nn_test = covariance(nn_test)



from mt import *
import time
#114

# Evaluation
rmse_list[s] = computeError(ytest, yntest)
ll_list[s] = loglik(ytest, yntest, syntest)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
new = current_time - old
train_time_list[s] = new