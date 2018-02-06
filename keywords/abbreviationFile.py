import os
from csv import reader

class abbreviationFile:
    def __init__(self):
        self.abbreviation = []
        try:
            self.file = open(os.path.abspath('csv/abbreviation.csv'), 'r')
            csvReader = reader(self.file, delimiter=',')
            for line in csvReader:
                self.abbreviation.append(line)
        except Exception as e:
            print(e)
    
    def __del__(self):
        self.file.close()