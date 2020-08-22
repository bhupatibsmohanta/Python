import json
from difflib import get_close_matches

with open('data.json') as file:
    data=json.load(file)
    
new=json.dumps(data,indent=2)

arr=list(data.keys())

def translate_word(word):
    words=[]
    upper=get_close_matches(word.upper(),arr,4,0.85)
    if(upper!= []):
        for i in upper:
            words.append(i)
    
    lower= get_close_matches(word.lower(),arr,4,0.85)
    if(lower!= []):
        for i in lower:
            words.append(i)
           
    title= get_close_matches(word.capitalize(),arr,4,0.85)
    if(title!= []):
        for i in title:
            words.append(i)
    words = list(set(words)) 
    
    if(word in words):
        print(word,"-> ",data[word])
        words.remove(str(word))
    else:
        print("There is No such word as",word)
    
    print()
    
    for i in words:
        print("Did You Mean :",end=" ")
        print(i,"-> ",data[i])
        print('')


while(True):
    print("Enter word to search in Dictionary : ",end=" ")        
    word=input()
    translate_word(word)
    print("Enter 'y' to exit : ",end=" ")
    end = input()
    if(end == 'y'):
        break