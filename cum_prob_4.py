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
    #while(1):
    for i in range(7):
        start=text.find('>')
        space1=text.find(' ')
        end=text.find('<',start+1)
        space2=text.find(' ',space1+1)
        if(start+1==len(text)):
            break
        if(start<space1):
            if(end<space1):
                s1=text[start+1:end]
            else:
                s1=text[start+1:space1]
                end=space1               
        else:
            if(end<space2):
                s1=text[space1+1:end]
            else:
                s1=text[space1+1:space2]
                end=space1                
        if(len(s1)>0):# and '\n' not in s1):
            list1.append(s1)
        text=text[end+1:]
    return list1


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

#print remove_tags('''<table cellpadding='3'>
#                     <tr><td>Hello</td><td>World!</td></tr>
#                     </table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

#print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']