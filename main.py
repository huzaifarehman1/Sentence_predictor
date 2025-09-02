import pyro
import os



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

def filter_data(data:str):      
    data = data.replace("\n","").replace("\t","")


def create_transition_dict(filtered_data:str):
    lis = []
    trans_dict = {}
    for i in range(len(filtered_data)):
        pass
           
    