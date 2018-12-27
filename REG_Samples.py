#!/usr/bin/env python3
#coding=utf-8

import os
import VBREG as REG
import CorpusReader as cr

os.system('clear')

print('Training starts - Tuna-Furniture')
ts,ds,ats = cr.LoadAlignedRegCorpus('Corpora/ETunaF-Aligned2.json')
reg = REG.VBREG(ts,ds,ats)
print('Training completes')

#   "targets": [
#     "colour=grey;orientation=front;type=desk;size=large"
#   ],
#   "distractors": [
#     "colour=blue;orientation=front;type=desk;size=large",
#     "colour=red;orientation=back;type=desk;size=large",
#     "colour=green;orientation=left;type=desk;size=small",
#     "colour=blue;orientation=front;type=fan;size=large",
#     "colour=red;orientation=back;type=fan;size=large",
#     "colour=green;orientation=left;type=fan;size=small"
#   ],
txt1 = reg.Generate([
        ('colour','grey',1),('orientation','front',1),('type','desk',1),('size','large',1)
    ],[
        [('colour','blue',1),('orientation','front',1),('type','desk',1),('size','large',1)],
        [('colour','red',1),('orientation','back',1),('type','desk',1),('size','large',1)],
        [('colour','green',1),('orientation','left',1),('type','desk',1),('size','small',1)],
        [('colour','blue',1),('orientation','front',1),('type','fan',1),('size','large',1)],
        [('colour','red',1),('orientation','back',1),('type','fan',1),('size','large',1)],
        [('colour','green',1),('orientation','left',1),('type','fan',1),('size','small',1)],
    ])
print('task1:',txt1)
print('corpus text: grey frontal table')
print('')

#   "targets": [
#     "colour=red;orientation=right;type=chair;size=small"
#   ],
#   "distractors": [
#     "colour=red;orientation=left;type=chair;size=small",
#     "colour=blue;orientation=back;type=chair;size=small",
#     "colour=grey;orientation=front;type=chair;size=large",
#     "colour=red;orientation=left;type=sofa;size=small",
#     "colour=blue;orientation=back;type=sofa;size=small",
#     "colour=grey;orientation=front;type=sofa;size=large"
#   ],
txt2 = reg.Generate([
        ('colour','red',1),('orientation','right',1),('type','chair',1),('size','small',1)
    ],[
        [('colour','red',1),('orientation','left',1),('type','chair',1),('size','small',1)],
        [('colour','blue',1),('orientation','back',1),('type','chair',1),('size','small',1)],
        [('colour','grey',1),('orientation','front',1),('type','chair',1),('size','large',1)],
        [('colour','red',1),('orientation','left',1),('type','sofa',1),('size','small',1)],
        [('colour','blue',1),('orientation','back',1),('type','sofa',1),('size','small',1)],
        [('colour','grey',1),('orientation','front',1),('type','sofa',1),('size','large',1)],
    ])
print('task2:',txt2)
print('corpus text: red large chair')
print('')

print('Training starts - Tuna-People')
ts,ds,ats = cr.LoadAlignedRegCorpus('Corpora/ETunaP-Aligned2.json')
reg = REG.VBREG(ts,ds,ats)
print('Training completes')
#   "targets": [
#     "age=old;orientation=front;hairColour=light;hasSuit=1;hasShirt=1;hasTie=1;hasBeard=1;hasGlasses=1;hasHair=1"
#   ],
#   "distractors": [
#     "age=old;orientation=left;hairColour=light;hasSuit=0;hasShirt=1;hasTie=0;hasBeard=0;hasGlasses=1;hasHair=1",
#     "age=young;orientation=front;hairColour=dark;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=1;hasHair=1",
#     "age=old;orientation=front;hairColour=light;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=1;hasHair=1",
#     "age=young;orientation=front;hairColour=dark;hasSuit=0;hasShirt=0;hasTie=0;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=young;orientation=front;hairColour=dark;hasSuit=0;hasShirt=1;hasTie=0;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=old;orientation=front;hairColour=light;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=0;hasHair=1"
#   ],
txt1 = reg.Generate([
        ('age','old',1),('orientation','front',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','1',1),('hasTie','1',1),('hasBeard','1',1),('hasGlasses','1',1),('hasHair','1',1)
    ],[
        [('age','old',1),('orientation','left',1),('hairColour','light',1),('hasSuit','0',1),('hasShirt','1',1),('hasTie','0',1),('hasBeard','0',1),('hasGlasses','1',1),('hasHair','1',1)],
        [('age','young',1),('orientation','front',1),('hairColour','dark',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','1',1),('hasHair','1',1)],
        [('age','old',1),('orientation','front',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','1',1),('hasHair','1',1)],
        [('age','young',1),('orientation','front',1),('hairColour','dark',1),('hasSuit','0',1),('hasShirt','0',1),('hasTie','0',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','young',1),('orientation','front',1),('hairColour','dark',1),('hasSuit','0',1),('hasShirt','1',1),('hasTie','0',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','old',1),('orientation','front',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
    ])
print('task1:',txt1)
print('corpus text: beard, glasses, old')
print('')
#   "targets": [
#     "age=young;orientation=front;hairColour=dark;hasSuit=0;hasShirt=1;hasTie=0;hasBeard=1;hasGlasses=0;hasHair=1"
#   ],
#   "distractors": [
#     "age=young;orientation=front;hairColour=light;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=young;orientation=front;hairColour=dark;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=young;orientation=right;hairColour=dark;hasSuit=0;hasShirt=1;hasTie=0;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=old;orientation=front;hairColour=light;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=old;orientation=front;hairColour=light;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=0;hasHair=1",
#     "age=old;orientation=right;hairColour=light;hasSuit=1;hasShirt=0;hasTie=1;hasBeard=0;hasGlasses=0;hasHair=1"
#   ],
txt2 = reg.Generate([
        ('age','young',1),('orientation','front',1),('hairColour','dark',1),('hasSuit','0',1),('hasShirt','1',1),('hasTie','0',1),('hasBeard','1',1),('hasGlasses','0',1),('hasHair','1',1)
    ],[
        [('age','young',1),('orientation','front',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','young',1),('orientation','front',1),('hairColour','dark',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','young',1),('orientation','right',1),('hairColour','dark',1),('hasSuit','0',1),('hasShirt','1',1),('hasTie','0',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','old',1),('orientation','front',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','old',1),('orientation','front',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
        [('age','old',1),('orientation','right',1),('hairColour','light',1),('hasSuit','1',1),('hasShirt','0',1),('hasTie','1',1),('hasBeard','0',1),('hasGlasses','0',1),('hasHair','1',1)],
    ])
print('task1:',txt2)
print('corpus text: guy with barb')
print('')