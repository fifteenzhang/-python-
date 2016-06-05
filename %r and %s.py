text = "I am %d years old." % 22
print "I said: %s." % text
print "I said: %r." % text

#result:
#I said: I am 22 years old..
#I said: 'I am 22 years old.'.


import datetime
d = datetime.date.today()
print "%s" % d
print "%r" % d

#result 
#2016-06-05
#datetime.date(2016, 6, 5)
