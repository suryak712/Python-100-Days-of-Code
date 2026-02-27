import pandas as pd

# df = pd.read_csv("weather_data.csv")
# # temps = df["temp"].to_list()
# max_temp = df["temp"].max()
# monday = df[df["day"] == 'Monday']
# # print(df["temp"].mean())
#
# print(df[df["temp"] == max_temp])
# print(monday["temp"] * 9/5 + 32)

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = df["Primary Fur Color"].value_counts()
print(pd.DataFrame(fur_color))