#!/usr/bin/env python3
#coding=utf-8

'''
    
'''

__author__ = "Xiao Li"
__copyright__ = "Copyright 2018, Xiao Li"
__license__ = "GPL"
__version__ = "1.0"
__email__ = ""

Furniture = [
    ('the red sofa',[
        ('colour','red',1),
        ('type','sofa',1)
    ]),
    ('the blue fun',[
        ('colour','blue',1),
        ('type','fun',1),
    ]),
    ('the green desk',[
        ('colour','green',1),
        ('type','desk',1)
    ]),
    ('red fun',[
        ('colour','red',1),
        ('type','fun',1)
    ]),
    ('green sofa',[
        ('type','desk',1)
    ]),
    ('the desk',[
        ('type','desk',1)
    ])
]

FurnitureEx = [
    [ ('the',None),('red',[('colour','red',1)]),('sofa',[('type','sofa',1)]) ],
    [ ('the',None),('blue',[('colour','blue',1)]),('fun',[('type','fun',1)]) ],
    [ ('the',None),('green',[('colour','green',1)]),('desk',[('type','desk',1)]) ],
    [ ('red',[('colour','red',1)]),('fun',[('type','fun',1)]) ],
    [ ('green',[('colour','green',1)]),('sofa',[('type','sofa',1)]) ],
    [ ('the',None),('desk',[('type','desk',1)]) ]
]

FurnitureDistractors = [
    [
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ],
    [
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ],
    [
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ],
    [
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ],
    [
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ],
    [
        [('colour','red',1),('type','sofa',1)],
        [('type','desk',1),('colour','green',1)]
    ]

]