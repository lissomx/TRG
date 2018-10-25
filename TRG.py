#!/usr/bin/env python3
#coding=utf-8

'''
    TRG: Text-Reassamble Generator (TRG)
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "MIT"
__version__ = "1.0"
__email__ = ""

import VBLS

class TRG:
    def __init__(self, AlignedCorpus, separator=' ', strict=True):
        '''
        '''
        self.Strict = strict
        self.separator = separator
        schemas = [(s,s.Features) for s in (self.Schema(r) for r in AlignedCorpus)]
        self.schemaSelector = VBLS.VBLS(schemas)
        smallCorpora = [x for s,_ in schemas for x in s.GetPlaceholderData(self.Strict)]
        dataDic = {}
        for tag,word,fg in smallCorpora:
            if tag in dataDic:
                dataDic[tag].append((word,fg))
            else:
                dataDic[tag] = [(word,fg)]
        self.lexSelectors = dict([(key,VBLS.VBLS(val)) for key,val in dataDic.items()])

    def Generate(self,features,threshold=0.2):
        '''
        Generate most suitable text for the given data
            features: [(concept,value), ...] and concepts and values are strings
            threshold: the min weight to output
        Return: 
            (text,weight)
        '''
        best = ('<no suitable text>', threshold)
        for schema,weight in self.schemaSelector.Lex(features):
            sweight = weight
            for tag,word,_ in schema.GetPlaceholderData(self.Strict):
                words = self.lexSelectors[tag].Lex(features)
                word, wweight = words[0] if len(words)>0 else ('<UNKNOW>',0)
                sweight = min(sweight,wweight)
                schema.Fill(tag,word,self.Strict)
            if sweight>best[1]:
                best = (schema.GetText(self.separator),sweight)
        return best
            

    class Schema:
        def __init__(self, sentence):
            self.Text = sentence
            self.FillInfo = {}
            self.Seq = [self.__GetPlaceholderTag(word,fg) for word,fg in sentence]
            self.Features = [(c,v,w) for _,fg in sentence if fg is not None for c,v,w in fg]
            self.__Tag = repr(self.Seq)

        def GetPlaceholderData(self,strict):
            if strict:
                return [((self.__Tag,i),inf[0],[(c,v,w) for c,v,w in inf[1]]) 
                for i,inf in enumerate(self.Text) if inf[1] is not None]
            else:
                return [(self.__GetPlaceholderTag(inf[0],inf[1]),inf[0],[(c,v,w) for c,v,w in inf[1]]) 
                for i,inf in enumerate(self.Text) if inf[1] is not None]
        
        def Fill(self,tag,word,strict):
            if strict:
                _,i = tag
                self.FillInfo[i]=word
            else:
                ids = [i for i,x in enumerate(self.Seq) if x==tag]
                for i in ids:
                    self.FillInfo[i]=word
                pass
        
        def GetText(self,separator):
            temp = [(w if i not in self.FillInfo else self.FillInfo[i]) for i,w in enumerate(self.Seq)]
            return separator.join(temp)
        
        def __GetPlaceholderTag(self, word, feature):
            if feature is None:
                return word
            else:
                concepts = sorted(c for c,_,_ in feature)
                return repr(concepts)

        def __hash__(self):
            return hash(self.__Tag)
    
        def __eq__(self, other):
            return self.__Tag == other.__Tag
