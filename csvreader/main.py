# import csv
import pandas

# # with open("weather_data.csv") as datafile:
# #     data=csv.reader(datafile)
# #     temparatures=[]
# #     count=0
# #     for row in data:
# #        if row[1].isdigit():
# #             temparatures.append(int(row[1]))
# #     print(temparatures)
    
    
# data=pandas.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list=data["temp"].to_list
# # avg=sum(temp_list)/len(temp_list)
# avgSame=data["temp"].mean()
# data_max=data["temp"].max()

# # row data
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# mondayF=monday.temp*9/5 +32
# print(mondayF)


# #create data frame from scratch

# data_dict={
#     "students":["any","james","angela"],
#     "scores":[76,56,65]
# }
# datanew=pandas.DataFrame(data_dict)
# print(datanew)
# datanew.to_csv("new_file.csv")



#Squarrel based on clolor

squarrel_dataframe=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(squarrel_dataframe[squarrel_dataframe.PrimaryFurColor=="10142018"])