# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:26:20 2016

@author: shubhankar
"""

# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(text):
    freq=[0.0 for i in range(26)]
    ref_string='abcdefghijklmnopqrstuvwxyz'
    checked=[]
    for i in range(len(text)):
        counter=0
        index=i
        if(text[i] not in checked):    
            checked.append(text[i])
            while(1):    
                counter+=1
                inext=text.find(text[i],index+1)
                if(inext==-1):
                    freq[ref_string.find(text[i])]=counter*1.0/len(text)
                    #print freq[0]
                    break
                else:
                    index=inext                                
    return freq



#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
