#!/usr/bin/env python3
#coding=utf-8

'''
    VBLS: Vector-Based Lexical Selector
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "GPL"
__version__ = "1.0"
__email__ = ""

import numpy as np

class VBLS:
    def __init__(self, corpus):
        '''
        Init the selector with a small training corpus
            corpus: [(features, text), ...]; a feature-text corpus 
            features: (key,value,weight)
            text: string
        '''
        self.FeatureMap, self.featureCount = self._VectorBuilder((c,v) for _,fg in corpus for c,v,_ in fg)
        self.WordMap, self.wordCount = self._VectorBuilder(freg for freg,_ in corpus)
        self.WordMapT = dict(zip(self.WordMap.values(),self.WordMap.keys()))
        recordFeas = (([self.FeatureMap[(c,v)] for c,v,_ in fg],[w for _,_,w in fg]) for _,fg in corpus)
        A = np.array(list(self._OneHot(fea,self.featureCount,w) for fea,w in recordFeas))
        W = np.array(list(self._OneHot([self.WordMap[freg]],self.wordCount) for freg,_ in corpus))
        self.B = self._Solver(A,W)
    
    def Lex(self, features, threshold=0.2):
        '''
        Select word(s) for the given data
            features: [(concept,value), ...] and concepts and values are strings
            threshold: the min weight to output
        Return: 
            [(word,weight), ...]
        '''
        feaVec = self._OneHot([self.FeatureMap[x] for x in features if x in self.FeatureMap],self.featureCount)
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
        v = [0.0]*l
        for i,w in zip(vs,ws):
            v[i] = w
        return v
    
    def _Solver(self,A,W):
        p = np.linalg.pinv(A)
        B = np.dot(p,W)
        return B