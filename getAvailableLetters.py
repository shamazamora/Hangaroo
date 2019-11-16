# -*- coding: utf-8 -*-
import string
alphabet = string.ascii_lowercase

def getAvailableLetters(lettersGuessed): 
    remain = []
    for i in alphabet:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
