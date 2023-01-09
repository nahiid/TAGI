#14
def activation_func_index(funcname):
    if(funcname == 'tanh'):
        func_idx = 1
    elif(funcname == 'sigm'):
        func_idx = 2
    elif(funcname == 'cdf'):
        func_idx = 3
    elif(funcname == 'relu'):
        func_idx = 4
    elif(funcname == 'softplus'):
        func_idx = 5
    return func_idx
    
#40
def mean_a(z, mz, func_idx):
    if(func_idx == 1):
        def dtanhf(x):
            print (1-tanh(x)^2)
        s = dtanhf(mz) * (z-mz) + tanh(mz)
        j = dtanhf(z)
    elif(func_idx == 2):
        def sigmoid(x):
            print(1/(1+exp(-x)))
        def dsigmoid(x):
            print(sigmoid(x)*(1-sigmoid(x)))
        s = sigmoid(mz)
        j = dsigmoid(z)