from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re;
import string;
import random;
import os;

global dataStructure
dataStructure={}
conditions={'gt':'>','gte':'>=','lt':'<','lte':'<=','eq':'==','neq':'!=','or':'||','and':'&&'}
def action(data):
    if 'print' in data.split(" "):
        return printdata(re.findall(r"'(.*?)'", data, re.DOTALL)[0])

    if 'for' in data.split(" ") or 'times' in data.split(" "):
        for key in data.split(" "):
            if key.isdigit():
                times=key;
        return forloop(times)
    if 'if' in data.split(" ") or 'elif' in data.split(" "):
        data1=re.findall(r"'(.*?)'", data, re.DOTALL)[0]
        for key  in data1.split(" "):
            if key in conditions.keys():
                data1=data1.replace(key,conditions[key])
            for keyword in dataStructure.keys():
                if keyword in key:
                    data1=data1.replace(key,(dataStructure[keyword])[int(key[-1])-1])
        if 'if' in data.split(" "):
            return ifCondition(data1)
        else:
            return elseifCondition(data1)

    if 'else' in data.split(" "):
        return elseCondition()

def printdata(data):
    statement = 'System.out.println("'+data+'");'
    return statement



def ifCondition(data):
    statement="if ("+data+"){"
    text=input()
    while 'End if' not in text:
        statement+=action(text)
        text=input()
    return statement+"}"

def elseifCondition(data):
    statement= "else if ("+data+") {"
    text=input()
    while 'End elif' not in text:
        statement+=action(text)
        text=input()
    return statement+"}"

def elseCondition():
    statement="else {"
    data = input()
    while 'End else' not in data:
        statement+=action(data)
        data= input()
    return statement+'}'

def forloop(times):
    if 'for' not in dataStructure.keys():
        dataStructure['for']=[]
    character = ''.join(random.choice(string.ascii_uppercase ) for _ in range(1))
    dataStructure['for'].append(character);
    statement = " for( int "+character+"=0;"+character+"<"+times+";"+character+"++) {"
    data = input()
    while 'End for' not in data:
        statement+=action(data)
        data=input()
    statement+="}"
    return statement

# stopwordlist=set(stopwords.words('english'))
# keywords=list(set([w for w in word_tokenize(text) if w not in stopwordlist]))
# stopwordsFound=list(set([w for w in word_tokenize(text) if w  in stopwordlist]))
# print("keywords")
# print(keywords)
# print(stopwordsFound)
# for w in stopwordsFound:
#     text=text.replace(w,"",1);
# print(text)


global program
filename= input("enter the file name")
program = "public class "+filename+""" {

    public static void main(String[] args) {""";



print("enter the code\n")
data=input()
while 'End' not in data:
    program+=action(data)
    data=input()
program+="""}
         }"""
print(program)
f = open(filename+".java", "w")
f.write(program)
f.close()

os.system("javac  "+filename+".java")
os.system("java "+filename)