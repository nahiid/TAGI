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

def regression(nn, x, y, train_idx, test_idx):
    # Initialization
    initsv = nn[sv]
    initmax_epoch = nn[max_epoch]
    nn[error_rate_eval] = 0

  # Indices for each parameter group
  # Train net
    nn[train_mode] = 1
    nn[batch_size] = nn[batch_size_list[1]]
    nn = initialization_net(nn)
    nn = parameters(nn)
    nn = covariance(nn)    

    # Validation net
    nn_val = nn
    nn_val[train_mode] = 0
    nn_val[batch_size] = nn[batch_size_list[2]]
    nn_val = parameters(nn_val)
    nn_val = covariance(nn_val)

    # Test net
    nn_test = nn
    nn_test[train_mode] = 0
    nn_test[batch_size] = nn[batch_size_list[3]]
    nn_test = parameters(nn_test)
    nn_test = covariance(nn_test)



from mt import *
import time
#114

# Evaluation
rmse_list[s] = compute_error(ytest, yntest)
ll_list[s] = log_lik(ytest, yntest, syntest)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
new = current_time - old
train_time_list[s] = new