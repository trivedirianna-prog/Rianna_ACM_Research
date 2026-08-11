
import re
def transforms(text):
    text=text.replace("error","🚨ERROR🚨")
    text=text.replace("warning","⚠️WARNING⚠️")
    text=re.sub(r'[\w.-]+@[\w.-]+\.\w+', "[HIDDEN EMAIL]",text)
    text=re.sub(r'\d+\.\d+\.\d+\.\d+',"[HIDDEN IP]",text)
    text=re.sub(r'password\S*=\S*\S+',"password=[HIDDEN]",text)
    return text

s=input("Log: ")
ec=s.count("ERROR")
wc=s.count("WARNING")
print(transforms(s))
print("--LOG ANALYTICS--\nErrors counted: {}\nWarnings counted: {}".format(ec,wc))

"""
string manipulation and regex are used in multiple ways. 

the former is done using .replace function

the latter is done by importing re module and using re.sub(pattern,replacement,string)
emails,ip addresses and passwords are detected and redacted using regex

in patterns, \w means letters nos , \s means everything except white spaces , \d means digits
[\w.-] means letters nos and .-   while the plus sign indicates multiple of those things
 
in the end an analytics table with the frequency of warnings and errors is displayed
"""
