# -*- coding: utf-8 -*-
"""
Translator V0.2
Created on Tue Jul 14 14:58:29 2020

@author: player-three

Description: translates mandarin text to english using Google Translate,
displays english translation, pinyin, and also translations for each
individual input character.

Usage: run program as function input
Syntax: trans("TEXT TO BE TRANSLATED")

Example:

trans("想要學會聽懂別人説的中文")
想要學會聽懂別人説的中文  ->  I want to learn to understand Chinese
(pinyin)  Xiǎng yào xuéhuì tīng dǒng biérén shuō de zhōngwén 

想  ->  Xiǎng  ->  miss you
要  ->  Yào  ->  want
學  ->  Xué  ->  learn
會  ->  Huì  ->  meeting
聽  ->  Tīng  ->  listen
懂  ->  Dǒng  ->  understand
別  ->  Bié  ->  Another
人  ->  Rén  ->  people
説  ->  Lǐlùn  ->  Theory
的  ->  De  ->  of
中  ->  Zhōng  ->  in
文  ->  Wén  ->  Text

(mistake in the translation, I know. Will look into a fix in future versions)

    
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

