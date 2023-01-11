# importing  all the
# functions defined in test.py
import numpy as np
from vectorization import *


# 2929
def extract_parameters(theta):
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
    sw = theta[1, 0]
    mb = theta[2, 0]
    sb = theta[3, 0]
    mwx = theta[4, 0]
    swx = theta[5, 0]
    mbx = theta[6, 0]
    sbx = theta[7, 0]
    outputs = [mw, sw, mb, sb, mwx, swx, mbx, sbx]
    return outputs


# 135
def feed_forward_pass(nn, theta, states):
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
    out_extract_parameters = extract_parameters(theta)
    mw = out_extract_parameters[0]
    sw = out_extract_parameters[1]
    mb = out_extract_parameters[2]
    sb = out_extract_parameters[3]
    out_extract_states = extract_parameters(states)
    mz = out_extract_states[0]
    sz = out_extract_states[1]
    ma = out_extract_states[2]
    sa = out_extract_states[3]
    j = out_extract_states[4]
    mdxs = out_extract_states[5]
    sdxs = out_extract_states[6]
    mxs = out_extract_states[7]
    sxs = out_extract_states[8]
    num_layers = len(nn[nodes])
    act_fun_idx = nn[act_fun_idx]
    act_bound = nn[act_bound]
    b = nn[batch_size]
    rb = nn[rep_batch_size]
    nodes = nn[npdes]
    num_parms_perlevel_2 = nn[num_parms_perlevel_2]

    # derivative
    mda = np.empty((num_layers, 1))
    sda = np.empty((num_layers, 1))
    mdda = np.empty((num_layers, 1))
    sdda = np.empty((num_layers, 1))
    mda = np.empty((num_layers, 1))


# 729
out_vectorized_4_delta = vectorized_4_delta(mw, caz, caxs, deltamloop, deltasloop)
deltamzloop = out_vectorized_4_delta[0]
deltaszloop = out_vectorized_4_delta[1]
deltamzsloop = out_vectorized_4_delta[2]
deltaszsloop = out_vectorized_4_delta[3]

# 1965
out_vectorized_mean_var = vectorized_mean_var(maloop, mw, saloop, sw)
mzloop = out_vectorized_mean_var[0]
szloop = out_vectorized_mean_var[1]

# 2008
out_vectorized_mean_var = vectorized_mean_var(ma, mw, Sa, Sw)
mzloop = out_vectorized_mean_var[0]
szloop = out_vectorized_mean_var[1]

# 2117
out_vectorized_delta = vectorized_delta(cbz, deltamr, deltasr)
deltaMrb = out_vectorized_delta[0]
deltaSrb = out_vectorized_delta[1]

# 2285
out_vectorized_delta = vectorized_delta(iszf, dmz, dsz)
deltam = out_vectorized_delta[0]
deltas = out_vectorized_delta[1]

# 2356
out_two_plus = two_plus(mw, sw, deltamw, deltasw)
mw = out_two_plus[0]
sw = out_two_plus[1]
out_two_plus = two_plus(mb, Sb, deltamb, deltasb)
mb = out_two_plus[0]
sb = out_two_plus[1]
out_two_plus = two_plus(mwx, swx, deltamwx, deltaswx)
mwx = out_two_plus[0]
swx = out_two_plus[1]
out_two_plus = two_plus(mbx, sbx, deltambx, deltasbx)
mbx = out_two_plus[0]
sbx = out_two_plus[1]
