# csv file
import csv

with open('eggs.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['a', 'b', 'c'])
    csv_writer.writerow(['Hello'] * 5 + ['How are you'])
    # write multi lines
    csv_writer.writerows([('hello', 'world'), ('i', 'love', 'you')])

with open('eggs.csv', 'r') as file:
    for line in csv.reader(file):
        print(line)

with open('names.csv', 'w') as file:
    writer = csv.DictWriter(file, ['first_name', 'last_name'])
    writer.writeheader()
    writer.writerow({'first_name': 'zhang', 'last_name': 'zhanfeng'})
    writer.writerows([
        {'first_name': 'zhang', 'last_name': 'zhanfeng'},
        {'first_name': 'huang', 'last_name': 'hongli'},
    ])

with open('names.csv', 'r') as file:
    for row in csv.DictReader(file):
        print(row)
