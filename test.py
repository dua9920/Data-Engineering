import pandas as pd

# df = pd.DataFrame({'시간': {'a':2.0, 'b':3.0, 'c':1.2}})
df = pd.DataFrame({'시간': {'a': '2018-03 14:00', 'b': '2018-03 12:00', 'c': '2018-03 13:00'}})
print(df)
df = df.sort_values(by='시간')
print(df)