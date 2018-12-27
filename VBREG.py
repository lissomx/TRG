#!/usr/bin/env python3
#coding=utf-8

'''
    Vector-Based REG driven by Text-Reassamble Generator (TRG)
    VB-REG is implemented based on the paper: 
        "Statistical NLG for Generating the Content and Form of Referring Expressions"
        X Li, K van Deemter, C Lin, 2018
        http://www.aclweb.org/anthology/W18-6561
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "xiao [dot] li [at] abdn [dot] ac [dot] uk"

from functools import reduce
import TRG

class VBREG:
    def __init__(self, targets,distractors,alignedTexts,separator=' ',strict=False):
        # corpusEx = []
        _targetsEx = []
        _alignedTexts = []
        allConcept = [c for r in alignedTexts for _,fg in r if fg is not None for c,_,_ in fg]
        self.allConcept = set(allConcept)
        for target,record,distr in zip(targets,alignedTexts,distractors):
            # record e.g.: [ ('the',None),('red',[('colour','red',1)]),('sofa',[('type','sofa',1)]) ]
            notemptyfgs = [d[1] for d in record if d[1] is not None]
            if len(notemptyfgs)==0:
                continue #skip the texts which express none feature
            # allFea = reduce(lambda a,b: a+b, notemptyfgs)
            # diff = self.__Difference(allFea,distr)
            diff = self.__Difference(target,distr)
            _targetsEx.append(target+diff)
            _alignedTexts.append(record)
            # recordEx = [(w,None) if fg is None else (w,fg+diff) for w,fg in record]
            # corpusEx.append(recordEx)
        self.Generator = TRG.TRG(_alignedTexts,_targetsEx,separator,strict)
    
    def Generate(self, target, distractors):
        '''
        target: the feature group of the target object: 
            e.g.: ('colour','blue',1),('type','sofa',1)
        distractors: a list of feature group of distractors: 
            e.g.: [('colour','blue',1),('type','sofa',1), ('colour','green',1),('type','desk',1), ...]
        '''
        diff = self.__Difference(target, distractors)
        text = self.Generator.Generate(target+diff)
        return text

    def __Difference(self, targetFeatures, distractors):
        # target features e.g.: [('colour','red',1),('type','sofa',1)]
        # distractors e.g.: [ [('colour','red',1),('type','sofa',1)], [('type','desk',1),('colour','green',1)] , ...]
        # difference vector总是包含所有target可能出现的concept。
        # 这是为了保证每个schema和每个pleaceholder都会包含相同的difference vector，以减少不同的placeholder和schema的数量
        leng = len(distractors)*1.0
        features = reduce(lambda a,b: a+b, [d for d in distractors])
        diff = dict(('[diff]'+c,0.0) for c in self.allConcept)
        for fea in targetFeatures:
            apperence = 1 - (sum(x[2] for x in features if x[0]==fea[0] and x[1]==fea[1])/leng)
            apperence = fea[2]*apperence
            diff['[diff]'+fea[0]] = apperence
        return [(c,'',w) for c,w in diff.items()]
        
