from pyro.distributions import Categorical
import os
import re
import random
from torch import tensor
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


def create_transition_dict(filtered_data:list,order = 1): #order for markov chain
    trans_dict = {}#store count only
    prev = [0]*order
    
    for i in range(order):
        prev[i] = filtered_data[i]
    
    l_pointer = 0 #inclusive
    r_pointer = order  #exclusive  
    starting_values = set()# for . have (order length) tuple
    
    for i in range(order,len(filtered_data)):
        temp = prev[l_pointer:r_pointer]
        
        if "." in temp and (temp[0]=="."):
            prev.append(filtered_data[i])
            l_pointer += 1
            r_pointer += 1
            value = prev[l_pointer:r_pointer]
            starting_values.add(value)  
                
            
            continue
        
        if "." in temp and (temp[-1]!="."):
            prev.append(filtered_data[i])
            l_pointer += 1
            r_pointer += 1
            continue
            
        hashable_prev = tuple(temp)
    
        if hashable_prev not in trans_dict:
            trans_dict[hashable_prev] = {}
        
        if filtered_data[i] not in trans_dict[hashable_prev]:
            trans_dict[hashable_prev][filtered_data[i]] = 1
        else:
            trans_dict[hashable_prev][filtered_data[i]] += 1
    
        prev.append(filtered_data[i])
        l_pointer += 1
        r_pointer += 1         
    return trans_dict,starting_values        


def make_sentences(transition:dict,starting_values,order,number = 5):
    for k,v in transition.items():
        s = sum(v.values())
        for k2,v2 in v.items():
            transition[k][k2] = round(v2/s,4) 
            
    count = 0
    string = ""
    seen = {}
    curr = random.choice(starting_values)
    while count<number:
        
        if curr not in seen:
            possibilities = []
            probabilities = []
        
            for k,v in transition[curr].items():
                probabilities.append(v)
                possibilities.append(k)
            seen[curr] = (probabilities,possibilities) # important
        
        P,states = seen[curr]
        
        index = (Categorical(tensor(P))).sample().item()        
        word = states[index]
        
        if word not in [".",","]:
            string += " "
        string += word 
        curr = word 
        
        if word == ".":
            count += 1
            curr = random.choice(starting_values)
            
    return string          
    
if __name__=="__main__":
    ORDER = 2
    data = taking_data_input()
    fil_data = filter_data(data)
    transition_model,start = create_transition_dict(fil_data,ORDER)
    print(make_sentences(transition_model,start,ORDER,3))        
           
    