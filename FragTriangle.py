#!/usr/bin/env python3
#coding=utf-8

'''
    Fragment Triagle (only) for SSA algorithm
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "GPL"
__version__ = "1.0"
__email__ = ""

class FragTriangle:
    def __init__(self, words, separator):
        self._words = words
        self._separator = separator
        self._triangle = ToMultiFragment(words,separator)
        # self._weight = self._MarkWeight(weightReader, self._triangle)
        # self._maximia = self._GetMaximia(self._weight)
        # self.Maximiatop = self._GetMaximiaTops(self._maximia)
    
    def GetAlignment(self, weightReader, threshold):
        self._weight = self._MarkWeight(weightReader, self._triangle)
        self._maximia = self._GetMaximia(self._weight,threshold)
        self._maximiatop = self._GetMaximiaTops(self._maximia)
        selected = [(self._triangle[j][i],self._weight[j][i]) for j,i in self._maximiatop]
        return selected

    def _MarkWeight(self, weightReader, triangle):
        '''
        标记所有权重。
        '''
        weight = [[0]*len(y) for y in triangle]
        l = len(triangle)
        for j in range(l):
            for i in range(l-j):
                value = weightReader(triangle[j][i])
                weight[j][i] = value
        return weight
        
    def _GetMaximia(self, weightTriangle, threshold):
        '''
        返回每个非零节点的覆盖。
        '''
        flag = [[0]*len(y) for y in weightTriangle]
        l = len(flag)
        # 填充法标记极大值
        for j in range(l):
            for i in range(l-j):
                if flag[j][i] == 0: # 找的未处理的节点
                    isMaxima = True
                    val = weightTriangle[j][i] # 寻找和val相同值得所有邻接节点
                    col = [(j,i)]
                    flag[j][i] = 1
                    queue = self.__Neighbour(l,j,i)
                    while len(queue)>0:
                        jj, ii = queue.pop(0)
                        # if flag[jj][ii] != 0: # 0是未处理（初始化）值
                        #     continue # 跳过已处理过的节点
                        vv = weightTriangle[jj][ii]
                        if vv == val and flag[jj][ii] == 0:
                            queue.extend(self.__Neighbour(l,jj,ii))
                            col.append((jj,ii))
                            flag[jj][ii] = 1
                        elif vv > val:
                            isMaxima = False
                    if val<threshold or not isMaxima:
                        for jj, ii in col:
                            flag[jj][ii] = -1
        return flag
        
    def _GetMaximiaTops(self, maximia):
        l = len(maximia)
        for j in range(l-1):
            for i in range(l-j):
                # 如果父节点标记为1,则取消子节点标记
                if i<l-j-1 and maximia[j+1][i] == 1:
                    maximia[j][i] = -1
                if i>0 and maximia[j+1][i-1] == 1:
                    maximia[j][i] = -1
        # print(maximia)
        maximiaTop = []
        for j in range(l):
            for i in range(l-j):
                if maximia[j][i] == 1:
                    maximiaTop.append((j,i))
        # print(maximiaTop)
        return maximiaTop
    
    def __Neighbour(self, l, j, i):
        node4 = [] # 求(j,i)的邻接节点
        if j>0: # 不是底层
            node4.append((j-1,i))
            node4.append((j-1,i+1))
        if j<l: # 不是顶层
            if i<l-j-1:
                node4.append((j+1,i))
            if i>0:
                node4.append((j+1,i-1))
        return node4

def ToMultiFragment(txt, separator):
    '''
    Build the fragment triangle for the given text.
        txt: [string]; text
    Return:
        [[string]]; the fragment triangle with each fragemnt
            triangle:[layer]; layer:[fragment]
    '''
    l=len(txt)+1
    layer = lambda x: [separator.join(txt[s:s+x]) for s in range(l-x)]
    tri = [list(layer(y)) for y in range(1, l)]
    return tri