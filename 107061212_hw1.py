# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061212.csv'
#cwb_filename = 'sample_input.csv'
#cwb_filename = 'sample_input.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
target_data = list(filter(lambda item: item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))

target = []
ID = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
ID.sort()
for station in ID:
    tmp_data = list(filter(lambda item: item['station_id'] == station, target_data))
    humd_sum = 0
    if tmp_data != []:
        for humd in tmp_data:
            humd_sum += float(humd['HUMD'])
        target.append([station, humd_sum])
    else:
        target.append([station, 'None'])

#target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.
#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(target)
#========================================
