# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:50:08 2016

@author: shubhankar
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:11:27 2016

@author: shubhankar
"""

# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(text):
    list1=[]
    if(text[0]!='<'):
        while(1):
            start=0
            if(len(text)==0):
                break
            end=text.find(' ')
            if(end+1==0):
                end=len(text)
            s1=text[start:end]
            if(len(s1)>0 and s1[0]!='\n'):
                if(s1[-1]=='\n'):
                    #list1.append(s1[0:-1])
                    list1+=remove_tags(s1[0:-1])
                else:
                    list1+=remove_tags(s1)
            text=text[end+1:]
            #print text
        return list1
    else:
        while(1):
        #for i in range(5):
            start=text.find('>')
            if(len(text)==0):
                break
            end=text.find('<',start+1)
            if(end+1==0):
                break
            s1=text[start+1:end]
            if(len(s1)>0 and s1[0]!='\n'):
                #list1.append(s1)
                list1+=remove_tags(s1)
            text=text[end+1:]
        return list1
        
    


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

#print remove_tags('''<table cellpadding='3'>
#                    <tr><td>Hello</td><td>World!</td></tr>
#                     </table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

#print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
print remove_tags('This is in <i>italics</i>')