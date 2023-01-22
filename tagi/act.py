import math
from scipy import stats
from scipy.stats import norm
import numpy as np

""" Assign ID to activation functions
This function assigns an ID number depending on the type of activation function.
@param funName Type of activation function: "tanh", "sigm", "cdf", "relu" or
"softplus"
@return An ID number which corresponds to:
@return - 1 if \code{funName} is "tanh"
@return - 2 if \code{funName} is "sigm"
@return - 3 if \code{funName} is "cdf"
@return - 4 if \code{funName} is "relu"
@return - 5 if \code{funName} is "softplus"
@export """

def activationFunIndex(funName):
    if funName == "tanh":
        funIdx = 1
    elif funName == "sigm":
        funIdx = 2
    elif funName == "cdf":
        funIdx = 3
    elif funName == "relu":
        funIdx = 4
    elif funName == "softplus":
        funIdx = 5
    return funIdx

"""Calculate mean of activated units
This function uses lineratization to estimate the activation units mean vector
\eqn{\mu_{A}} and the Jacobian matrix evaluated at \eqn{\mu_{Z}}.
@param z Vector of units for the current layer
@param mz Mean vector of units for the current layer \eqn{\mu_{Z}}
@param funIdx Activation function index defined by \code{\link{activationFunIndex}}
@return A list which contains the activation units mean vector \eqn{\mu_{A}} and the Jacobian
matrix evaluated at \eqn{\mu_{Z}}
@export"""

def meanA(z, mz, funIdx):
    if funIdx == 1:
        # tanh
        def dtanhf(x):
            print(1 - math.tanh(x) ^ 2)
        s = dtanhf(mz) * (z - mz) + math.tanh(mz)
        J = dtanhf(z)
    elif funIdx == 2:
        # sigmoid
        def sigmoid(x):
            print(1 / (1 + math.exp(-x)))
        def dsigmoid(x):
            print(sigmoid(x) * (1 - sigmoid(x)))
        s = sigmoid(mz)
        J = dsigmoid(z)
    elif funIdx == 3:
        # cdf
        #. In r this "stats::pnorm(0)" results "0.5" and in Python  "norm.cdf(0)" results "0.5"
        #. Therefor norm.cdf in Python is equivalent with pnorm function in R
        #. In r this "stats::dnorm(0)" results "0.3989" and in Python  "norm.pdf(0)" results "0.3989"
        #. Therefor norm.pdf in Python is equivalent with dnorm function in R
        s = norm.pdf(mz) * (z - mz) + norm.cdf(mz)
        J = norm.pdf(z)
    elif funIdx == 4:
        #relu
        #. numpys maximum() function in Python Equivalent pmax() in R
        s = np.maximum(mz,0)
        #. len(matrix) : length of rows
        #. len(matrix[0]) length of the first row to get the no. of columns
        nrow, ncol = len(z), len(z[0])
        J = np.zeros((nrow, ncol), dtype=int)
        J[z > 0] = 1
    elif funIdx == 5:
        #softplus
        alpha = 10
        nrow, ncol = len(mz), len(mz[0])
        k = np.zeros((nrow, ncol), dtype=int)
        k[alpha * mz < 30] = 1
        s = 1 + math.exp (alpha * mz * k)
        s = (math.log(s) + mz * (1-k)) / alpha
        J = k * math.exp(alpha * mz * k) / (1 + math.exp(alpha * mz * k)) + (1 - k) / alpha

    outputs = np.array(s, J)
    return(outputs)

"""Calculate variance of activated units
This function uses lineratization to estimate the covariance matrix of activation units \eqn{\Sigma_{A}}.
@param J Jacobian matrix evaluated at \eqn{\mu_{Z}}
@param Sz Covariance matrix of units for the current layer \eqn{\Sigma_{Z}}
@return The activation units covariance matrix \eqn{\Sigma_{A}}
@export"""
def covarianceSa(J, Sz):
    Sa = J * Sz * J
    return(Sa)

"""Mean, Jacobian and variance of activated units
This function returns mean vector \eqn{\mu_{A}}, Jacobian matrix evaluated at
\eqn{\mu_{Z}} and covariance matrix of activation units \eqn{\Sigma_{A}}.
@param z Vector of units for the current layer
@param mz Mean vector of units for the current layer \eqn{\mu_{Z}}
@param Sz Covariance matrix of units for the current layer \eqn{\Sigma_{Z}}
@param funIdx Activation function index defined by \code{\link{activationFunIndex}}
@return - Mean vector of activation units for the current layer \eqn{\mu_{A}}
@return - Covariance matrix activation units for the current layer \eqn{\Sigma_{A}}
@return - Jacobian matrix evaluated at \eqn{\mu_{Z}}
@export"""
def meanVar(z, mz, Sz, funIdx):
  out_meanA = meanA(z, mz, funIdx)
  m = out_meanA[0]
  J = out_meanA[1]
  S = covarianceSa(J, Sz)
  outputs = list(m, S, J)
  return(outputs)

"""Mean and variance of activated units for derivatives
This function calculates mean vector and covariance matrix of activation units'
derivatives.
@param mz Mean vector of units for the current layer \eqn{\mu_{Z}}
@param Sz Covariance matrix of units for the current layer \eqn{\Sigma_{Z}}
@param funIdx Activation function index defined by \code{\link{activationFunIndex}}
@param bound If layer is bound
@return - Mean vector of activation units' first derivative
@return - Covariance matrix of activation units' first derivative
@return - Mean vector activation units' second derivative
@return - Covariance matrix activation units' second derivative
@export"""


    


