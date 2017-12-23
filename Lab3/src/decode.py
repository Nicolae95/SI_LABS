# -*- coding: utf-8 -*-
from numpy import *
from string import maketrans

def translator(text,alphabet,key):
    trantab = maketrans(alphabet,key)
    return text.translate(trantab)

def caesar_decode(ciphertext,s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    return translator(ciphertext,alpha,alpha[-s:]+alpha[:-s])