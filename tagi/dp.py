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
def denormalize(yn, syn, myntrain, syntrain):
    y = yn * syntrain + myntrain
    if syn!=None:
        sy = syntrain^2 * syn
    else:
        sy = None
    outputs = np.array(y, sy)
    return outputs