# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:03:26 2016

@author: ShubhankarP
"""

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            return entry[1].append(url)
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    word_list=content.split()
    for i in word_list:
        add_to_index(index,i,url)




add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


