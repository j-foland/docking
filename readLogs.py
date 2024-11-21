import os
import pathlib
import pandas as pd

#working dir
logdir=os.listdir(r"C:\Users\folan\Research\Aryl Hydrocarbon\Outputs\Logs")

fullArray = {}
for log in logdir:
    logpath="C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Outputs\\Logs\\" + log
    #the worst way of doing this tbh
    file=open(logpath)
    fline = file.readlines()

    values = fline[26:-1]
    # ok so this gives just the entire table but we only care about the second entry

    bindval = list()
    for line in values:
        nums = line.split()
        bindval.append(nums[1])
    fullArray.update({log:bindval})
    print(bindval)
print("-----------------------------------------------------")
df = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in fullArray.items()]))
df.to_csv("C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Main\\"+"ABwide.csv")

    # im basically a cs student
file.close()
