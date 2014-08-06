import re, string
def namelist():
    with open('./Downloads/names.txt') as data:
        namelist=list(data)
    namelist=namelist[0].split(',')
    for i in xrange(len(namelist)):
        namelist[i]=namelist[i].strip('"')
    namelist.sort()
    return namelist
    
def alphabet_values():
    alphabet={}
    value=1
    for i in string.ascii_uppercase:
        alphabet[i]=value
        value+=1
    return alphabet

def name_scores():
    values=alphabet_values()
    names=namelist()
    total=0
    for name in names:
        total+=sum([values[char]for char in name])*(names.index(name)+1) 
    print total
  
name_scores()

