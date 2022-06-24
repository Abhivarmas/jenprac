"""#1. Write a Python program to read an entire text file.
f=open("D:\CDAC ARTIFICIAL INTELLIGIENCE\solve exercise\WORD.txt",mode="r")
print(f.read())
f.close()
"""
#2.Write a program that counts lines and characters in a file. With your favorite text editor, code a Python module called mymod.py, which exports three top-level names:
#a) A countLines(name) function that reads an input file and counts the number of lines in it 
#b) A countChars(name) function that reads an input file and counts the number of characters in it 
#c) A test(name) function that calls both counting functions with a given input file¬name.
"""a=input("enter your file location directory:")
import mymod
b=mymod.countlines(a)
c=mymod.countchars(a)
mymod.test(a)
print("countlines:",b,"\ncountchars:",c)"""
#3.Test your mymod module from Exercise 2 interactively, by using from to load the exports directly, first by name, then using the from* variant to fetch every¬thing
"""from mymod import countlines,countchars,test

a=input("enter your file location directory:")
m=countlines(a)
print(m)
k=countchars(a)
print(k)
test(a)"""
#4.Now, add a line in your mymod module that calls the test function automati¬cally only when the module is run as a script, not when it is imported The line you add will probably test the value of __name__ for the string "__main__", as shown in this unit. Try running your module from the sys¬tem command line; then, import the module and test its functions interactively. 
"""import mymod
print(__name__)
a=input("enter your file location directory:")
mymod.test(a)"""
#5.Write a second module, myclient.py, which imports mymod and tests its functions; run myclient from the system command line. If myclient uses from to fetch from mymod, will mymod’s functions be accessible from the top level of myclient? What if it imports with import instead? Try coding both variations in myclient and test interactively, by importing myclient .
"""
import myclient
"""
#from  myclient import test,countlines,countchars


"""
name="D:\CDAC ARTIFICIAL INTELLIGIENCE\solve exercise\WORD.txt"
myclient.mymod.test(name)
b=myclient.mymod.countlines(name)
c=myclient.mymod.countchars(name)
print(b,"and",c)

name="D:\CDAC ARTIFICIAL INTELLIGIENCE\solve exercise\WORD.txt"
test(name)
b=countlines(name)
c=countchars(name)
print(b,"and",c)"""





#6.Package imports. Finally, import your file from a package. Create a subdirectory called mypkg nested in a directory on your module import search path, move the mymod.py module file you created in exercises 2 or 4 into the new directory, and try to import it with a package import of the form: import mypkg.mymod.
"""import mypkg.mymod
a=input("enter your file location directory:")
mypkg.mymod.test(a)
b=mypkg.mymod.countlines(a)
c=mypkg.mymod.countchars(a)
print("countlines:",b,"\ncountchars:",c)"""

#7.Experiment with module reloads: perform the tests in the changer.py example, changing the called function’s message and/or behavior repeatedly
"""import test
m=test.add(4,5)
import importlib
importlib.reload(test)
b=test.min(11,15)
print(m ,"and",b)"""