#Convert JSON to CSV.
import json
import csv

# Opening JSON file and loading the data
# into the variable data
with open ('name.json') as json_file:
    name_data = json.load(json_file)

my_name = name_data['name']

# now we will open a file for writing
name_csv = open("name_csv.csv","w")

#create csv writer object
csv_writer = csv.writer(name_csv)

#values into csv file
csv_writer.writerow(my_name)