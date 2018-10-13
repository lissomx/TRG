#!/usr/bin/env python3
#coding=utf-8

'''
    SSA: Sequence-Set Aligner
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "GPL"
__version__ = "1.0"
__email__ = ""

from FragTriangle import *

def SSA(corpus, separator, threshold):
    '''
    Align the raw corpus
        corpus: [ (features, text), ... ]; a feature-text corpus 
        features: [ (concept,value,weight), ... ]
        text: string
    Return: aligned corpus: [ record, ... ]
        record: [ (text,features), ... ]
        text: string
        features: { concept:value }
    '''
    l=len(corpus)*1.0
    corpusEx = [__RecordExtend(feas,txt,separator) for txt,feas in corpus]
    allFragment = set(frag for _,_,_,x in corpusEx for frag in x)
    allFeature = set(fea for x,_,_,_ in corpusEx for fea in x)

    fragmentCount = dict((frag,0.0) for frag in allFragment)
    featureCount = dict((fea,0.0) for fea in allFeature)
    for features,_,_,fragments in corpusEx:
        for fea, weight in features.items():
            featureCount[fea] += weight
        for frag in fragments:
            fragmentCount[frag] += 1
    
    ExpressCoreBuff = {}
    def ExpressCore(fragment,feature):
        if (fragment,feature) in ExpressCoreBuff:
            return ExpressCoreBuff[(fragment,feature)]
        # Express(,)
        C_g_w = sum(fea[feature] for fea,_,_,frag in corpusEx if fragment in frag and feature in fea)
        P_g_w = C_g_w / fragmentCount[fragment] 
        P_g = featureCount[feature] / l
        express = (P_g_w - P_g) / (1 - P_g)
        # Core(,)
        P_w_g = C_g_w / featureCount[feature]
        val = express * P_w_g if express * P_w_g >0 else 0
        ExpressCoreBuff[(fragment,feature)] = val
        return val

    alignedCorpus = []
    for features,_,words,fragments in corpusEx:
        alignment = []
        triangle = FragTriangle(words,separator)
        for fea in features:
            align = triangle.GetAlignment(lambda frag: ExpressCore(frag,fea),threshold)
            # tri_weight = triangle._weight
            alignment.extend((fea,freg.split(separator),conf) for freg,conf in align)
        alignment.sort(key=lambda x: len(x[1]))

        aliwords = [None]*len(words)
        aliwordRange = [None]*len(words)
        for a in alignment: # a: ( (fea), [words], weight )
            fea,seg,weight = a
            ids = __findIndexs(words,seg) # 匹配的seg的起点id
            for i in ids:
                start = i
                end = i+len(seg)
                feaset = set([fea])
                for r in aliwordRange[i:i+len(seg)]:
                    # 方式1: 被完全包含则被忽略
                    # if r is not None and not (i<=r[0] and r[1]-r[0]<len(seg)):
                    # 方式2: 永远不被忽略（论文版本）
                    if r is not None:
                        # 对于每个没有完全包含在 (i,i+len(seg)) 之间的区段
                        start = min(start,r[0])
                        end = max(end,r[1])
                        feaset = feaset | aliwords[r[0]]
                for j in range(start,end):
                    aliwords[j] = feaset
                    aliwordRange[j] = (start,end)
        
        segments = []
        nod = None
        for i in range(len(aliwords)):
            n = aliwordRange[i]
            if n is None:
                segments.append((words[i],None))
            elif(aliwordRange[i]!=nod):
                nod = aliwordRange[i]
                ws = words[nod[0]:nod[1]]
                segments.append((separator.join(ws),dict(aliwords[i])))
        alignedCorpus.append(segments)
    return alignedCorpus
        
def __findIndexs(seq, subseq):
    l1 = len(seq)
    l2 = len(subseq)
    if l2>l1:
        return []
    ids = []
    for i in range(l1-l2+1):
        isTrue = True
        for j in range(l2):
            if seq[i+j] != subseq[j]:
                isTrue = False
                break
        if isTrue:
            ids.append(i)
    return ids

def __RecordExtend(features,text,separator):
    features = dict([((c,v),w) for c,v,w in features])
    words = text.split(separator)
    fragmentLists = ToMultiFragment(words,separator)
    fragments = set([frag for x in fragmentLists for frag in x]) # flaten
    return (features,text,words,fragments)
