import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import glob as glob
import pandas as pd
from datetime import datetime

project_dir = ""
ofile = project_dir + datetime.strftime(datetime.now(),"%Y%m%d-%H%M%S") + ".png"

all_data = pd.concat([pd.read_csv(f) for f in glob.glob(project_dir + "logfiles/*.csv")], axis = 0)
all_data['adj_time'] = all_data['time_since_epoch'] - all_data['time_since_epoch'].min()

redgreen = ["#2ecc71","#e74c3c"]
sns.set_palette(redgreen)

#Plot results in seaborn
f, ax = plt.subplots(figsize=(11, 9))
sns_plot = sns.stripplot(x="adj_time", y="server", hue="result", data=all_data)
plt.savefig(ofile)
