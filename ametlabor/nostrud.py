import csv

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
