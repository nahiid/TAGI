# importing  all the
# functions defined in test.py
import numpy as np
from vectorization import *


# 2929
def extractParameters(theta):
    """Extract parameters from list of parameters.
    Args:
        theta: List of parameters
    Returns:
        Mean vector of weights for the current layer
        Covariance vector of weights for the current layer
        Mean vector of biases for the current layer
        Covariance vector of biases for the current layer
    """
    mw = theta[0, 0]
    Sw = theta[1, 0]
    mb = theta[2, 0]
    Sb = theta[3, 0]
    mwx = theta[4, 0]
    Swx = theta[5, 0]
    mbx = theta[6, 0]
    Sbx = theta[7, 0]
    outputs = [mw, Sw, mb, Sb, mwx, Swx, mbx, Sbx]
    return outputs


# 135
def feedForwardPass(NN, theta, states):
    """Forward uncertainty propagation for derivative calculation
    This function feeds the neural network forward from input data to
    responses and considers components required for derivative calculations.
    Args:
        NN: Lists the structure of the neural network
        theta" List of parameters
        states" List of states
    Returns:
        Updated states
        Mean vectors of activation units' first derivative
        Covariance matrices of activation units' first derivative
        Mean vectors of activation units' second derivative
        Covariance matrices of activation units' second derivative
    """
    # Initialization
    out_extractParameters = extractParameters(theta)
    mw = out_extractParameters[0]
    Sw = out_extractParameters[1]
    mb = out_extractParameters[2]
    Sb = out_extractParameters[3]
    out_extractStates = extractParameters(states)
    mz = out_extractStates[0]
    Sz = out_extractStates[1]
    ma = out_extractStates[2]
    Sa = out_extractStates[3]
    J = out_extractStates[4]
    mdxs = out_extractStates[5]
    Sdxs = out_extractStates[6]
    mxs = out_extractStates[7]
    Sxs = out_extractStates[8]
    numLayers = len(NN[nodes])
    actFunIdx = NN[actFunIdx]
    actBound = NN[actBound]
    b = NN[batchSize]
    rb = NN[repBatchSize]
    nodes = NN[nodes]
    numParamsPerLayer_2 = NN[numParamsPerLayer_2]

    # derivative
    mda = np.empty((numLayers, 1))
    Sda = np.empty((numLayers, 1))
    mdda = np.empty((numLayers, 1))
    Sdda = np.empty((numLayers, 1))
    mda = np.empty((numLayers, 1))


# 729
out_vectorized4delta = vectorized4Delta(mw, Caz, Caxs, deltaMloop, deltaSloop)
deltaMzloop = out_vectorized4delta[0]
deltaSzloop = out_vectorized4delta[1]
deltaMzsloop = out_vectorized4delta[2]
deltaSzsloop = out_vectorized4delta[3]

# 1965
out_vectorizedMeanVar = vectorizedMeanVar(maloop, mw, Saloop, Sw)
mzloop = out_vectorizedMeanVar[0]
Szloop = out_vectorizedMeanVar[1]

# 2008
out_vectorizedMeanVar = vectorizedMeanVar(ma, mw, Sa, Sw)
mzloop = out_vectorizedMeanVar[0]
Szloop = out_vectorizedMeanVar[1]

# 2117
out_vectorizedDelta = vectorizedDelta(Cbz, deltaMr, deltaSr)
deltaMrb = out_vectorizedDelta[0]
deltaSrb = out_vectorizedDelta[1]

# 2285
out_vectorizedDelta = vectorizedDelta(iSzF, dMz, dSz)
deltaM = out_vectorizedDelta[0]
deltaS = out_vectorizedDelta[1]

# 2356
out_twoPlus = twoPlus(mw, Sw, deltaMw, deltaSw)
mw = out_twoPlus[0]
Sw = out_twoPlus[1]
out_twoPlus = twoPlus(mb, Sb, deltaMb, deltaSb)
mb = out_twoPlus[0]
Sb = out_twoPlus[1]
out_twoPlus = twoPlus(mwx, Swx, deltaMwx, deltaSwx)
mwx = out_twoPlus[0]
Swx = out_twoPlus[1]
out_twoPlus = twoPlus(mbx, Sbx, deltaMbx, deltaSbx)
mbx = out_twoPlus[0]
Sbx = out_twoPlus[1]
