# -*- coding: utf-8 -*-
"""
Translator V0.1
Created on Tue Jul 14 14:58:29 2020

@author: player-three
"""
#%%
def trans(a):
    from googletrans import Translator
    translator = Translator()
    translations = translator.translate([a], dest='en')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)
        
    translations = translator.translate([a], dest='zh-tw')
    for translation in translations:
        print('(pinyin) ',translation.pronunciation, '\n')
        
        
    
    for elem in a:
        print(elem, ' -> ', translator.translate(elem, dest='zh-tw').pronunciation, ' -> ', translator.translate(elem).text)

