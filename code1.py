import pandas as pd
import glob
import time

start = time.time()
        
path = "../data/"
all files = glob.glob(path + "/*.csv")
l = []

for filename in all_files:
  df = pd.read_csv(filename, index_col=None, header=0)
  l.append(df)

frame = pd.concat(l, axis=0, ignore_index=True)
frame.to.csv("output.csv", index=False)

end = time.time()
print(end - start)
