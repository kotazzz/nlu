# coding=utf8
#import test

import Libraries.nlu4 as nlulib4
nlu = nlulib4.NewLifeUtils(silent=True)

FGC = nlu.Color.FGC
nlu.BigPrint('Test', maxlinelength=10, begin = FGC.RED)
a = []
import random
for el in range(26):
    a.append(str(random.randrange(100000000, 999999999)))
print('\n'.join(a))
