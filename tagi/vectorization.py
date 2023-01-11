def two_plus(m, s, deltam, deltas):
    m = m + deltam
    s = s + deltas
    outputs =  [m, s]
    return outputs

def vectorized_mean_var(ma, mp, sa, sp):
    sz = sp*ma*ma + sa*sp + sa*mp*mp
    mz = ma*mp
    outputs = [mz, sz]
    return outputs

def vectorized_delta(c, deltam, deltas):
    deltam = c*deltam
    deltas = c*deltas*c
    outputs = [deltam, deltas]
    return outputs

def vectorized_4_delta(w,c1,c2, deltam, deltas):
    deltam1 = w*c1*deltam
    deltas1 = w*c1*deltas*w*c1
    deltam2 = w*c2*deltam
    deltas2 = w*c2*deltas*w*c2
    outputs = [deltam1, deltas1, deltam2, deltas2]
    return outputs