# -*- coding: utf-8 -*-
from lang.ro import _TEXT_RO


def ord_utf8(ch):
    return ord(ch.decode('utf-8'))


def freq_analysis(message):
    alphabet = ['a', 'ă', 'â', 'b', 'c','d','e','f','g','h','i','î','j','k','l','m',
                'n','o','p','q','r','s','ș','t','ț','u','v','w','x','y','z']
    count_list = [0]*len(alphabet)
    array = []
    for i in message.decode('utf8'):
        array.append(i.lower())
    n = len(array) + 0.0

    # print array

    # counts occurences of each letter
    for x in array:
        i = 0
        while i < len(alphabet):
            if x == alphabet[i].decode('utf8'):
                count_list[i] += 1
            i += 1

    # normalizes frequencies
    freq_list = []
    for x in count_list:
        freq_list.append(x/n)
    return freq_list


print freq_analysis(_TEXT_RO)
