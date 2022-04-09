cereals = open('cereals.csv')
maxValue = 0
minValue = -1
maxName = "N/A"
minName = "N/A"
totalRating = 0
rowCount = 0

for row in cereals:
    values = row.split(",")
    if(values[0] == "name"):
        continue
    name = str(values[0])
    rating = float(values[-1].strip())
    if(maxValue == 0 or rating > maxValue):
        maxValue = rating
        maxName = name
    if(minValue == -1 or rating < minValue):
        minValue = rating
        minName = name
    totalRating = totalRating + rating
    rowCount = rowCount + 1
    print(values[0], values[-1])
print("The lowest cereals rating value:", minValue, "Cereals name:", minName)
print("The average cereals rating value:", (totalRating/rowCount))
print("The highest cereals rating value:", maxValue, "Cereals name:", maxName)