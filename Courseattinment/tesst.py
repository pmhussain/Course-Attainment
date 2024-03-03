import csv
with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    for line in csv_reader:
            print(line)


with open('txt_file.txt', "w") as my_output_file:
    with open('test.csv', "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]

"""
    with open('test_read.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        #next(csv_reader)
        for line in csv_reader:
            print(line)
            csv_writer.writerow(line)
"""
