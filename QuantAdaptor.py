#!/usr/bin/env python3
#coding=utf-8

'''
    TRG: Text-Reassamble Generator
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "MIT"
__version__ = "1.0"
__email__ = ""

import numpy as np
import pandas as pd

class QuantAdapter:
    def __init__(self, corpus, keypoint_num=5):
        '''
            corpus: training corpus; [(features, text), ...]
                features: {concept:value}
                concept: string; quantitative concept should start with '@'
                value: string; quantitative value should be able to convert to float32
            text: [string]
            keypoint_num: the default amount of each concept
        '''
        self.__keypoint_num = keypoint_num

        self._features = pd.DataFrame((fea for fea, _ in corpus))
        self._texts = pd.Series(txt for _, txt in corpus)

        quant_features = [col for col in self._features if col.startswith('@')]
        self._features[quant_features]=self._features[quant_features].astype(float)
        self.__keypoints = dict(map(lambda x: (x, self.__select_keypoint(self._features[x].tolist(),self.__is_circle(x)), quant_features)))

    def __is_circle(self,concept):
        '''
        Return whether the value belongs to a loop circle e.g. angles
            concept: string; the concept name
        '''
        return concept.startswith('@@')
        
    def __select_keypoint(self, values, iscircle = False):
        '''
        Select key-points for a given quantitative concept.
        Register the key-points to
            values: [float32]; all prossible value of the concept in training corpus
            iscircle: bool; whether the value belongs to a loop circle e.g. angles
        Return: [float32]; the selected key-points
        '''
        values.sort()
        minpoint = values[0]
        maxpoint = values[-1]
        keynum = self.__keypoint_num+1 if iscircle else self.__keypoint_num
        interval = (maxpoint-minpoint) * 1.0 / (keynum - 1)
        return [minpoint + (interval * i) for i in range(keynum)]

    def __vectorise(self, feature):
        pass

    def __toKeyPoints(self, value, key_points, iscircle = False):
        '''
        Represent a feature value by multple key-points
            value: float32; a value of a feature
            key_points: [float32]; the key-points of the concept of the value
            iscircle: bool; whether the value belongs to a loop circle e.g. angles
        Return
            numpy.ndarray<float32>; Weights on the key_points
        '''
        vec = [0.0] * len(key_points)
        id = next((i for i,v in enumerate(key_points) if value<=v), -1)
        if(id==0):
            vec[0] = 1.0
        elif(id==-1):
            vec[-1] = 1.0
        else:
            interval = key_points[id]-key_points[id-1]
            vec[id-1] = (key_points[id]-value) / interval
            vec[id] = (value-key_points[id-1]) / interval
        if(iscircle):
            vec[0]=vec[0]+vec[-1]
            vec = vec[:len(key_points)]
        return np.sqrt(vec)
