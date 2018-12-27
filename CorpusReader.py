#!/usr/bin/env python3
#coding=utf-8

'''
    Load corpors from json files
    For the version 1.x of the json corpus files
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "xiao [dot] li [at] abdn [dot] ac [dot] uk"

import json
import io

def LoadCorpus(path):
    js = json.load(io.open(path, 'r', encoding='utf-8-sig'))
    corpus = [(rs['text'],__parse_featuregroup(rs['concepts'])) for rs in js['data']]
    return corpus

def LoadAlignedRegCorpus(path):
    # cardinality = 1
    js = json.load(io.open(path, 'r', encoding='utf-8-sig'))
    data = [rs for rs in js['data'] if rs['cardinality']=='1']
    target = __read_targets_1(data)
    alignedTexts = __read_aligned_records(data)
    distractors = __read_distractors(data)
    return target,distractors,alignedTexts

def __read_targets_1(data):
    corpus = [__parse_featuregroup(r['targets'][0]) for r in data]
    return corpus

def __read_aligned_records(data):
    corpus = [ [ (a['word'],__parse_featuregroup(a['data'])) for a in r['alignment'] ] for r in data]
    return corpus

def __read_distractors(data):
    distractors = [ [ __parse_featuregroup(d) for d in r['distractors'] ] for r in data]
    return distractors
    
def __parse_featuregroup(fg_str):
    if fg_str == '':
        return None
    features = fg_str.split(';')
    fg = [__parse_feature(f) for f in features if f != '']
    return fg

def __parse_feature(f_str):
    f = f_str.split('=')
    concept = f[0]
    value = f[1] if len(f)>1 else '__'
    return (concept,value,1)