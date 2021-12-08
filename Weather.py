# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     print(data)
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

import pandas as pd
data = pd.read_csv("weather_data.csv")
data_dic = data.to_dict()
# print(data_dic)
# data_list = data["temp"].to_list()
# print(data_list)
# avg=sum(data_list)/len(data_list)
# print(f"Avg is: {avg}")
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)
#
# # get data from rows:
#
# print(data[data.day == 'Monday'])
# print(data[data.temp == max(data.temp)])
#
# print(max(data.temp))

monday = data[data.day == 'Monday']
new_temp = int(monday.temp)*9/5 + 32
print(f" Temp: {new_temp}")

# Create a  dataframe

data_dict = {
    "student": ['Sourav', 'Gaurav', "Rahul"],
    "score": [5,3,7]
}

data = pd.DataFrame(data_dict)
print(data)
# data.to_csv("data_exported")