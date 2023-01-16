def twoPlus(m, S, deltaM, deltaS):
    m = m + deltaM
    S = S + deltaS
    outputs = [m, S]
    return outputs

def vectorizedMeanVar(ma, mp, Sa, Sp):
    Sz = Sp*ma*ma + Sa*Sp + Sa*mp*mp
    mz = ma*mp
    outputs = [mz, Sz]
    return outputs

def vectorizedDelta(C, deltaM, deltaS):
    deltaM = C*deltaM
    deltaS = C*deltaS*C
    outputs = [deltaM, deltaS]
    return outputs

def vectorized4Delta(W, C1, C2, deltaM, deltaS):
    deltaM1 = W*C1*deltaM
    deltaS1 = W*C1*deltaS*W*C1
    deltaM2 = W*C2*deltaM
    deltaS2 = W*C2*deltaS*W*C2
    outputs = [deltaM1, deltaS1, deltaM2, deltaS2]
    return outputs
