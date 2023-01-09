{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def two_plus(m, s, deltam, deltas):\n",
    "    m = m + deltam\n",
    "    s = s + deltas\n",
    "    outputs =  [m, s]\n",
    "    return outputs\n",
    "\n",
    "def vectorized_mean_var(ma, mp, sa, sp):\n",
    "    sz = sp*ma*ma + sa*sp + sa*mp*mp\n",
    "    mz = ma*mp\n",
    "    outputs = [mz, sz]\n",
    "    return outputs\n",
    "\n",
    "def vectorized_delta(c, deltam, deltas):\n",
    "    deltam = c*deltam\n",
    "    deltas = c*deltas*c\n",
    "    outputs = [deltam, deltas]\n",
    "    return outputs\n",
    "\n",
    "def vectorized_4_delta(w,c1,c2, deltam, deltas):\n",
    "    deltam1 = w*c1*deltam\n",
    "    deltas1 = w*c1*deltas*w*c1\n",
    "    deltam2 = w*c2*deltam\n",
    "    deltas2 = w*c2*deltas*w*c2\n",
    "    outputs = [deltam1, deltas1, deltam2, deltas2]\n",
    "    return outputs\n"
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
