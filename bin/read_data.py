import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# get all the csv files
file_list = []
for path, subdirs, files in os.walk("../input/"):
    for name in files:
        file_list.append(os.path.join(path, name))

#print(file_list[0])

# read each csv file into a list
data = []
for file in file_list:
    df = pd.read_csv(file)
    file_meta = str(os.path.splitext(os.path.basename(file))[0])
    x = file_meta.split("_")
    df["epitope"] = x[0]
    df["chain"] = x[1]
    df["donor"] = x[2]
    df["length"] = df['AA. Seq. CDR3'].str.len()
    data.append(df)

#print(data[3])
fig, ax = plt.subplots(8,7)
# Numpy ravel needed
ax = ax.ravel()
for idx in range(50):
    ax[idx].hist(data[idx]["length"], bins=6)
    #print(idx)

plt.tight_layout()
plt.show()
