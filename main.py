import pyro
import os
import re


def taking_data_input():
    with open("path_input.txt") as f:
        path_ = f.read()
        
    if not(path_):
        raise Exception("NO PATH FOUND")
    if not(os.path.isfile(path_)):
        raise Exception(f"NOT a file!!") 
    
    with open(path_) as f:
        data = f.read() 
    return data

def filter_data(data: str):
    # Convert to lowercase
    data = data.lower()
    # Keep only letters, numbers, spaces, and dots
    data = re.sub(r"[^a-z0-9., ]", " ", data)
    # Split into words

    words = data.split()
    
    temp = []
    for word in words:
        if len(word) > 1 and (word.endswith(".") or word.endswith(",")):
            temp.append(word[:-1])   # word without punctuation
            temp.append(word[-1])    # punctuation itself
        else:
            temp.append(word)

    return temp


def create_transition_dict(filtered_data:list):
    trans_dict = {}#store count only
    for i in range(1,len(filtered_data)):
        prev = filtered_data[i-1]
        if prev not in trans_dict:
            trans_dict[prev] = {}
        
        if filtered_data[i] not in trans_dict[prev]:
            trans_dict[prev][filtered_data[i]] = 1
        else:
            trans_dict[prev][filtered_data[i]] += 1
            
    return trans_dict        


def make_sentences(number = 5):
    count = 0
    string = ""
    while count<5:
        pass
        
    
if __name__=="__main__":
    data = taking_data_input()
    fil_data = filter_data(data)
    transition_model = create_transition_dict(fil_data)
    make_sentences(3)        
           
    