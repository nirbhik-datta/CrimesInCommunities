import csv
import os
import pandas as pd
import numpy as np
import re

exception_dict = {"Twentynine Palms-Morongo Valle":"Morongo Valley"}
def func(s):
    sub = re.sub(r"(?<=\w)([A-Z])", r" \1", s)
    
    if sub.endswith('city') or sub.endswith('town'):
        sub = sub[:-4]
    elif sub.endswith('township') or sub.endswith('district') or sub.endswith('division'):
        sub = sub[:-8]
    elif sub.endswith('borough') or sub.endswith('village'):
        sub = sub[:-7]        
    else:
        pass
    
    if sub in exception_dict:
        sub = exception_dict[sub]
    return sub

if __name__ == "__main__":
    df = pd.read_csv('CommViolPredUnnormalizedData.txt')
    df = df.replace('?',np.NaN) # Replace '?' with NaN values to be preprocessed 
    df = df.set_index('communityname') # Use community name as our index
    r_dim, c_dim = df.shape

    for i in range(r_dim):
        df.rename(index = {df.index[i] : func(df.index[i])}, inplace=True)
        
    df.to_csv('communities.csv')  
    # for i in range
    # df.rename(index={'BerkeleyHeightstownship':'Berkeley Heights'},inplace=True)    # df.loc[:,"communityname"] = df.communityname.apply(lambda x : str.lower(x))
    # print(df.head)

    # file = open("CommViolPredUnnormalizedData.txt","r")
    # lines = file.readlines()

    # for i in range(len(lines)):
    #     # print(lines[i].split()[0])
    #     s = lines[i].split(',')[0]
    #     if s.endswith('town') or s.endswith('city'):
    #         print("Happened")
    #         print(s)
    #         print(s[:-4])
    #         lines[i].split(',')[0] = s[:-4]
    #         print(lines[i].split(','))
    #         assert False