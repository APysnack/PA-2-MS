import csv


# class to generate a CSV File
class GenCSV:

    # constructor that takes a file name and CSV header
    def __init__(self, fname, header):
        self.name = fname
        self.header = header

    # creates a new CSV with the instance name and header
    def create(self):
        with open(self.name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
        f.close()

    # takes a "list" argument and appends it as a new row to the CSV file
    def add_row(self, new_row):
        with open(self.name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)

        f.close()