# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonths_leap= [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year1):
    year1_is_leap=False
    if(year1%4!=0):
	year1_is_leap=False
    elif(year1%100!=0):
	year1_is_leap=True
    elif(year1%400!=0):
	year1_is_leap=False
    else:
	year1_is_leap=True
    return year1_is_leap
	
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ndays1=0
    if(is_leap(year1)):
    	for i in range(month1-1):
    	    ndays1=ndays1+daysOfMonths_leap[i]
    else:
	for i in range(month1-1):
    	    ndays1=ndays1+daysOfMonths[i]

    ndays1=year1*365+(year1/4)+ndays1+day1
   
    ndays2=0
    if(is_leap(year1)):
    	for i in range(month2-1):
    	    ndays2=ndays2+daysOfMonths_leap[i]
    else:
	for i in range(month2-1):
    	    ndays2=ndays2+daysOfMonths[i]
    ndays2=year2*365+(year2/4)+ndays2+day2
    #print ndays2,ndays1	
    return ndays2-ndays1
    
    


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
		  #((2012,6,29,2012,6,30), 1),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
	print 'Given:',answer,'Result:',result
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

