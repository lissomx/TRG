#!/usr/bin/env python3
#coding=utf-8

import SSA
import TRG
import VBLS
import VBREG as REG
import CorpusReader as cr
from MockupCorpus import *

# def SSAFragTriangle_ToFragemnts():
#     text1 = ['how','are','you','.']
#     frag1,col1 = SSA.FragTriangle._BuildTriangle(None,text1,' ')
#     print(frag1)
#     print(col1)
#     text2 = []
#     frag2,col2 = SSA.FragTriangle._BuildTriangle(None,text2,' ')
#     print(frag2)
#     print(col2)

# SSAFragTriangle_ToFragemnts()

# c = SSA.SSA(Furniture, ' ', 0.2)

# TRG.TRG(FurnitureEx)

# s = VBLS.VBLS(Furniture)
# w = s.Lex([
#         ('colour','red'),
#         ('type','sofa')
#     ])

# print([c for txt,fea in Furniture for c,v,w in fea])


ts,ds,ats = cr.LoadAlignedRegCorpus('Corpora/ETunaF-Aligned2.json')
reg = REG.VBREG(ts,ds,ats)
txt = reg.Generate([
        ('colour','red',1),
        ('type','sofa',1)
    ],[
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ])
    #   "targets": [
    #     "colour=grey;orientation=front;type=desk;size=large"
    #   ],
    #   "distractors": [
    #     "colour=blue;orientation=front;type=desk;size=large",
    #     "colour=red;orientation=back;type=desk;size=large",
    #     "colour=green;orientation=left;type=desk;size=small",
    #     "colour=blue;orientation=front;type=fan;size=large",
    #     "colour=red;orientation=back;type=fan;size=large",
    #     "colour=green;orientation=left;type=fan;size=small"
    #   ],
    

pass