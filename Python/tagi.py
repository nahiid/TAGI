{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#729\n",
    "out_vectorized_4_delta = vectorized_4_delta(mw, caz, caxs, deltamloop, deltasloop)\n",
    "deltamzloop = out_vectorized_4_delta[0]\n",
    "deltaszloop = out_vectorized_4_delta[1]\n",
    "deltamzsloop = out_vectorized_4_delta[2]\n",
    "deltaszsloop = out_vectorized_4_delta[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1965\n",
    "out_vectorized_mean_var <- vectorized_mean_var(maloop, mw, saloop, sw)\n",
    "mzloop = out_vectorized_mean_var[0]\n",
    "szloop = out_vectorized_mean_var[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2008\n",
    "out_vectorized_mean_var <- vectorized_mean_var(ma, mw, Sa, Sw)\n",
    "mzloop = out_vectorized_mean_var[0]\n",
    "szloop = out_vectorized_mean_var[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2117\n",
    "out_vectorized_delta = vectorized_delta(cbz, deltamr, deltasr)\n",
    "deltaMrb = out_vectorized_delta[0]\n",
    "deltaSrb = out_vectorized_delta[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2285\n",
    "out_vectorized_delta = vectorized_delta(iszf, dmz, dsz)\n",
    "deltam = out_vectorized_delta[0]\n",
    "deltas = out_vectorized_delta[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2356\n",
    "out_two_plus = two_plus(mw, sw, deltamw, deltasw)\n",
    "mw = out_two_plus[0]\n",
    "sw = out_two_plus[1]\n",
    "out_two_plus = two_plus(mb, Sb, deltamb, deltasb)\n",
    "mb = out_two_plus[0]\n",
    "sb = out_two_plus[1]\n",
    "out_two_plus = two_plus(mwx, swx, deltamwx, deltaswx)\n",
    "mwx = out_two_plus[0]\n",
    "swx = out_two_plus[1]\n",
    "out_two_plus = two_plus(mbx, sbx, deltambx, deltasbx)\n",
    "mbx = out_two_plus[0]\n",
    "sbx = out_two_plus[1]"
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
