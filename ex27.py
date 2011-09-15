
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#ex27 learn boolean expresion and logic

print 'True and True',True and True #1
print 'False and False',False and False #0
print '1 == 1 and 2 == 1',1 == 1 and 2 == 1 #0
print '"test" == "test"',"test" == "test" #1
print '1 == 1 or 2 != 1',1 == 1 or 2 != 1 #1
print 'True and 1==1',True and 1==1 #1
print 'False and 0!=0',False and 0!=0 #0
print 'True or 1==1',True or 1==1 #1
print '"test" == "testing"',"test" == "testing" #0
print '1!=0 and 2==1',1!=0 and 2==1 #0
print '"test" != "testing"',"test" != "testing" #1
print '"test" == 1',"test" == 1 #0
print 'not (True and False)',not (True and False) #1
print 'not (1==1 and 0!=1)',not (1==1 and 0!=1) #0
print 'not (10==1 or 1000==1000)',not (10==1 or 1000==1000) #0
print 'not (1!= 10 or 3==4)',not (1!= 10 or 3==4) #0
print 'not ("testing"=="testing" and "Zed"=="Cool Guy")',not ("testing"=="testing" and "Zed"=="Cool Guy") #1
print '1==1 and not ("testing" == 1 or 1==0)',1==1 and not ("testing" == 1 or 1==0) #1
print '"chunky" == "bacon" and not (3==4 or 3==3)',"chunky" == "bacon" and not (3==4 or 3==3) #0
print '3==3 and not ("testing" == "testing" or "Python"=="Fun")',3==3 and not ("testing" == "testing" or "Python"=="Fun") #0
