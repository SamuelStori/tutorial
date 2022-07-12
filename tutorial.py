"""#!/usr/bin/env python I Have no idea what this does but it was already there so I will keep it for now??? I hope we? """
import pandas as pd
#import matplotlib.pyplot as plt
# from pathlib import Path
from numpy import *
from ipdb import set_trace

data = pd.read_csv('/Users/samuelnavarro/Documents/tutorial/data/train.csv')

#print(data.loc[data.Survived == 1])

# TODO: Hardcoded for now but will fix later
# print(data.iloc[1, 3:])



def age_band(age):
    for i in range(1, 10):
        if age < i*10 :
            if i==3:
                return f'{(i-1)*10 + 3} ~ {i*10-1}'
            if i==4:
                return f'{(i-1)*10 + 4} ~ {i*10-1}'
            return f'{(i-1)*10} ~ {i*10-1}'


if __name__=="__main__":
    set_trace()
    for i in range(len(data)):
        if i == 3:
            print("Here somethings wrong!! Please help!!!")

        data["age_band"] = data["Age"].apply(age_band)

        print(data.iloc[i])

