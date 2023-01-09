{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#14\n",
    "def activation_func_index(funcname):\n",
    "    if(funcname == 'tanh'):\n",
    "        func_idx = 1\n",
    "    elif(funcname == 'sigm'):\n",
    "        func_idx = 2\n",
    "    elif(funcname == 'cdf'):\n",
    "        func_idx = 3\n",
    "    elif(funcname == 'relu'):\n",
    "        func_idx = 4\n",
    "    elif(funcname == 'softplus'):\n",
    "        func_idx = 5\n",
    "    return func_idx\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#40\n",
    "def mean_a(z, mz, func_idx):\n",
    "    if(func_idx == 1):\n",
    "        def dtanhf(x):\n",
    "            print (1-tanh(x)^2)\n",
    "        s = dtanhf(mz) * (z-mz) + tanh(mz)\n",
    "        j = dtanhf(z)\n",
    "    elif(func_idx == 2):\n",
    "        def sigmoid(x):\n",
    "            print(1/(1+exp(-x)))\n",
    "        def dsigmoid(x):\n",
    "            print(sigmoid(x)*(1-sigmoid(x)))\n",
    "        s = sigmoid(mz)\n",
    "        j = dsigmoid(z)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)]"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "438727c8858bc46e257ba69863512eb04c8e9f5db9a1c7102296af502b4092eb"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
