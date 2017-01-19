# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(a):
    # Your code here
	i=0
	j=0
	if(len(a)!=len(a[0])):
		return False
	while i<len(a):
		while j<len(a[0]):
			num=a[i][j]
			#if(num/len(a)!=0 and num/len(a)!=1 or num>len(a)):
			#		return False
			if(num==a[j][i]):
				pass
			else:
				return False		
			j=j+1
		j=0
		i=i+1
	return True


print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
