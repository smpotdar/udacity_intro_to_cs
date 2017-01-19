# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:03:41 2016

@author: shubhankar
"""

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list1):
    if(len(list1)):
        prev=list1[0]
        big=0
        biggest=0
        element_big=list1[0]
        for i in range(1,len(list1)):
            if(list1[i]==prev):
                big+=1
            else:
                big=0
            if(big>biggest):
                biggest=big
                element_big=list1[i]
            prev=list1[i]
        return element_big                
    return None



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

