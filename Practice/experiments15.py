# learning about standard modules

import glob

myfiles = glob.glob("../files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())


import csv

with open("../Bonus/weather.csv", 'r') as file:
    data =  list(csv.reader(file))          #iterator

print(data)

city = input("Enter a city: ")

for row in data[1:]:            #after the labels
    if row[0] == city:
        print(row[1])


import shutil  #(shell utilities)
shutil.make_archive("output","zip", "../files")


import webbrowser

user_term = input("Enter a search term: ").replace(" ","+")

webbrowser.open(f"https://www.google.com/search?q={user_term}")