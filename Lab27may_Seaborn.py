
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(r'C:\Users\Arvind Kumar\Downloads\Student_Sample.csv')
# print(df1)

# sns.lineplot(df1,x='Science_Score',y='English_Score')
# plt.show()

# sns.set(style='dark')
# fmri= sns.load_dataset('fmri')
# fmri.head(5)


# fmri = sns.load_dataset('fmri')
# print(fmri.columns)  # This will print the actual column names

# sns.lineplot(x='timepoint',
# y='signal',
# hue='region',
# style='event',
# data = fmri)
# plt.show()

tips = sns.load_dataset('tips')
tips

sns.lineplot(x='tip',
y='total_bill',
hue='sex',
style='time',
data = tips)
plt.show()
