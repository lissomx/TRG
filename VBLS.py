#!/usr/bin/env python3
#coding=utf-8

'''
    VBLS: Vector-Based Lexical Selector
    VBLS is implemented based on the paper: 
        "Statistics-Based Lexical Choice for NLG from Quantitative Information"
        X Li, K van Deemter, C Lin, 2016
        http://www.aclweb.org/anthology/W16-6618
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "xiao [dot] li [at] abdn [dot] ac [dot] uk"

import numpy as np

class VBLS:
    def __init__(self, texts, data):
        '''
        Init the selector with a small training corpus
            corpus: [(features, text), ...]; a feature-text corpus 
            features: (key,value,weight)
            text: string
        '''
        self.FeatureMap, self.featureCount = self._VectorBuilder((c,v) for fg in data for c,v,_ in fg)
        self.WordMap, self.wordCount = self._VectorBuilder(freg for freg in texts)
        self.WordMapT = dict(zip(self.WordMap.values(),self.WordMap.keys()))
        recordFeas = (([self.FeatureMap[(c,v)] for c,v,_ in fg],[w for _,_,w in fg]) for fg in data)
        A = np.array(list(self._OneHot(fea,self.featureCount,w) for fea,w in recordFeas))
        W = np.array(list(self._OneHot([self.WordMap[freg]],self.wordCount) for freg in texts))
        self.B = self._Solver(A,W)
    
    def Lex(self, features, threshold=0.2):
        '''
        Select word(s) for the given data
            features: [(concept,value), ...] and concepts and values are strings
            threshold: the min weight to output
        Return: 
            [(word,weight), ...]
        '''
        feaIdsWeights = [(self.FeatureMap[(c,v)],w) for c,v,w in features if (c,v) in self.FeatureMap]
        feaVec = self._OneHot([x for x,_ in feaIdsWeights],self.featureCount,[x for _,x in feaIdsWeights])
        wordVec = np.dot(np.array(feaVec),self.B)
        wordIds = sorted(zip(wordVec,range(len(wordVec))), key=lambda x:-x[0])
        words = [(self.WordMapT[x],w) for w,x in wordIds if w>threshold]
        return words
    
    def Lex2(self, features, threshold=0.2):
        '''
        select words without considering word frequence in training corpus
        '''
        # todo
        pass

    def _VectorBuilder(self, items):
        allitem = set(items)
        dic = dict(zip(allitem,range(len(allitem))))
        return (dic, len(allitem))
    
    def _OneHot(self, vs, l, ws=None):
        if ws is None:
            ws = [1.0]*len(vs)
        else:
            pass
        v = [0.0]*l
        for i,w in zip(vs,ws):
            v[i] = w
        return v
    
    def _Solver(self,A,W):
        p = np.linalg.pinv(A)
        B = np.dot(p,W)
        return B