import csv
# Open file
data = open('example.csv', encoding='utf-8')
# Create csv reader
csv_data = csv.reader(data)
# Reformat into python object of lists
data_lines = list(csv_data)

# first row
# print(data_lines[0])

# 1000 rows of data (1st row is header row)
# print(len(data_lines))

# Print every line until 5th row
# for line in data_lines[:5]:
    # print(line)

# print the 4th item in each row
# print(data_lines[10][3])

# get list of all emails in file
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])
    # print(all_emails)

# print(data_lines[10])

# get list of first and last names
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])
    # print(full_names)

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
# write single row
# print # of characters written to row (7 - includes commas and \n)
print(csv_writer.writerow(['a', 'b', 'c'])) 

# write multiple rows
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()

# re-open file
f = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()