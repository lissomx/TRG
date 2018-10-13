#!/usr/bin/env python3
#coding=utf-8

import SSA
import TRG
import VBLS
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

trg = TRG.TRG(FurnitureEx)
txt = trg.Generate(
    [
        ('colour','red'),
        ('type','desk')
    ])

pass