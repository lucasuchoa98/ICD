import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

file = pd.read_csv("ign.csv")
#fig = plt.figure()


x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()

#ax = fig.add_subplot(111)
#ax.plot(


#teste
#file[file["platform"] == "Xbox One"]["score"].plot(kind="hist")

 
