# -*- coding: utf-8 -*-
from numpy import *
from decode import *
from freq import *
from lang.ro import _TEXT_RO


class Frequency_analysis:
    def __init__(self, ciphertext, cor):
        self.cor=cor
        self.ciphertext=ciphertext.lower()
        self.frequency()
        self.min_error()
        self.key=self.minimum[0]
        self.result=caesar_decode(self.ciphertext,self.minimum[0])

    def frequency(self):
        self.arr=zeros(len(self.cor),float64)
        for l in self.ciphertext:
            x=ord(l)
            if (x>=97 and x<=122):
                self.arr[x-97]+=1.0
        self.arr = self.arr/max(self.arr)

    def error(self):
        e=0
        for i in range(0,len(self.arr)):
            e+=abs(self.arr[i]-self.cor[i])**2
        return e

    def min_error(self):
        self.minimum=[0,10000]
        for rot in range(0,25):
            e=self.error()
            print rot,e
            if e<self.minimum[1]:
                self.minimum[1]=e
                self.minimum[0]=rot
            x=self.arr[-1]
            del self.cor[-1]
            self.cor.insert(0,x)

ciphertext="WKHSWEC: WI XKWO SC WKHSWEC NOMSWEC WOBSNSEC, MYWWKXNOB YP DRO KBWSOC YP DRO XYBDR, QOXOBKV YP DRO POVSH VOQSYXC, VYIKV COBFKXD DY DRO DBEO OWZOBYB, WKBMEC KEBOVSEC. PKDROB DY K WEBNOBON CYX, RECLKXN DY K WEBNOBON GSPO. KXN S GSVV RKFO WI FOXQOKXMO, SX DRSC VSPO YB DRO XOHD"
flist = [0.64297,0.11746,0.21902,0.33483,1.00000,0.17541,
        0.15864,0.47977,0.54842,0.01205,0.06078,0.31688,0.18942,
        0.53133,0.59101,0.15187,0.00748,0.47134,0.49811,0.71296,
        0.21713,0.07700,0.18580,0.01181,0.15541,0.00583]

FA=Frequency_analysis(ciphertext, flist)
print FA.result
print FA.key

# print '--- ro ---'

# citext = 'țfmfgpo'
# print freq_analysis(_TEXT_RO), sum(freq_analysis(_TEXT_RO))
# fa_ro = Frequency_analysis(citext, freq_analysis(_TEXT_RO))
# print fa_ro.result
# print fa_ro.key