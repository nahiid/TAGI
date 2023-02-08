# Completed
import numpy as np

"""Denormalize data
This function denormalizes response data processed by the neural network.
@param yn Predicted responses
@param syn Variance of the predicted responses
@param myntrain Mean vector of responses from training set
@param syntrain Variance vector of responses from training set
@return - Mean of denormalized predicted responses
@return - Variance of denormalized predicted responses
@export"""


def normalize(xtrain, ytrain, xtest, ytest):
    mxtrain = xtrain.mean(axis=0)
    sxtrain = xtrain.std(axis=0)
    mytrain = ytrain.mean(axis=0)
    sytrain = ytrain.std(axis=0)
    xntrain = (xtrain - mxtrain) / sxtrain
    yntrain = (ytrain - mytrain) / sytrain
    xntest = (xtest - mxtrain) / sxtrain
    yntest = ytest
    outputs = np.array(
        xntrain, yntrain, xntest, yntest, mxtrain, sxtrain, mytrain, sytrain
    )
    return outputs


"""Split data
This function splits data into training and test sets.
@param x Input data
@param y Response data
@param ratio Training ratio
@return - Training set of input variables
@return - Training set of responses
@return - Testing set of input variables
@return - Testing set of responses
@export"""


def split(x, y, ratio):
    numObs = x.shape[0]
    idxobs = np.random.permutation(numObs)
    idxTrainEnd = int(ratio * numObs)
    idxTrain = idxobs[:idxTrainEnd]
    idxTest = idxobs[idxTrainEnd:]
    xtrain = x[idxTrain, :]
    ytrain = y[idxTrain, :]
    xtest = x[idxTest, :]
    ytest = y[idxTest, :]
    outputs = np.array(xtrain, ytrain, xtest, ytest)
    return outputs


"""Denormalize data
This function denormalizes response data processed by the neural network.
@param yn Predicted responses
@param syn Variance of the predicted responses
@param myntrain Mean vector of responses from training set
@param syntrain Variance vector of responses from training set
@return - Mean of denormalized predicted responses
@return - Variance of denormalized predicted responses
@export"""


def denormalize(yn, syn, myntrain, syntrain):
    y = yn * syntrain + myntrain
    if syn is not None:
        sy = syntrain ^ 2 * syn
    else:
        sy = None
    outputs = np.array(y, sy)
    return outputs
