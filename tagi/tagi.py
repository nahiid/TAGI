# importing  all the
# functions defined in test.py
from vectorization import *

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
