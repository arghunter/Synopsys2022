import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# dataset = [[16564, 14804, 15178, 14149, 13807], [16478, 15026, 16129, 15916, 15911], [14408, 16185, 16119, 15163, 18791]]
dataset = [[38380, 19194], [38694, 17952], [39729, 17427]]
# dataset = np.random.default_rng().uniform(60,95,(20,4))
print(dataset)
df = pd.DataFrame(dataset, columns=['Uncontained','RPGA'])
df.head()


vals, names, xs = [],[],[]
for i, col in enumerate(df.columns):
    vals.append(df[col].values)
    names.append(col)
    xs.append(np.random.normal(i + 1, 0.04, df[col].values.shape[0]))  # adds jitter to the data points - can be adjusted

plt.boxplot(vals, labels=names, whis = 9999)
palette = ['r', 'g', 'b']
for x, val, c in zip(xs, vals, palette):
    plt.scatter(x, val, alpha=0.4, color=c)

##### Set style options here #####
sns.set_style("darkgrid")  # "white","dark","darkgrid","ticks"
boxprops = dict(linestyle='-', linewidth=1.5, color='#000000')
flierprops = dict(marker='o', markersize=1,
                  linestyle='none')
whiskerprops = dict(color='#000000')
capprops = dict(color='#000000')
medianprops = dict(linewidth=1.5, linestyle='-', color='#33ce10')

palette = ['r', 'g', 'b']
plt.boxplot(vals, labels=names, notch=False, boxprops=boxprops, whiskerprops=whiskerprops,autorange=True,capprops=capprops, flierprops=flierprops, medianprops=medianprops,showmeans=False,manage_ticks=True)


plt.xlabel("RPGA Results", fontweight='normal', fontsize=14)
plt.ylabel("Simulated Burnt Value (Acres)", fontweight='normal', fontsize=14)
# sns.despine(bottom=True) # removes right and top axis lines
plt.axhline(y=19244, color='#ff3300', linestyle='--', linewidth=1, label='Actual Burnt Value (Acres)')
plt.legend(bbox_to_anchor=(0.31, 1.06), loc=2, borderaxespad=0., framealpha=1, facecolor ='white', frameon=True)

plt.show()