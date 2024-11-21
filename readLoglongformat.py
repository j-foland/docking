import os
from pathlib import Path
import pandas as pd

#working dir
logdir=os.listdir(r"C:\Users\folan\Research\Aryl Hydrocarbon\Outputs\Logs")

fullArray = list()
for log in logdir:
    logpath="C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Outputs\\Logs\\" + log
    #the worst way of doing this tbh
    file=open(logpath)
    fline = file.readlines()

    values = fline[26:-1]
    # ok so this gives just the entire table but we only care about the second entry

    #getting only kj/mol entry from each row
    for line in values:
        nums = line.split()
        print((Path(log).stem,nums[1]))
        fullArray.append((Path(log).stem[:-3],nums[1]))
        print(fullArray)

    file.close()

df=pd.DataFrame(fullArray)
df.to_csv("C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Main\\"+"ABlong.csv")
    # im basically a cs student

