import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)
#print(data["Primary Fur Color"])

Cinnamon_squirrels = len(data[data["Primary Fur Color"] == 'Cinnamon'])
Gray_squirrels = len(data[data["Primary Fur Color"] == 'Gray'])
Black_squirrels = len(data[data["Primary Fur Color"] == 'Black'])
print(Cinnamon_squirrels)
print(Gray_squirrels)
print(Black_squirrels)

data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "count":[Cinnamon_squirrels, Gray_squirrels, Black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
