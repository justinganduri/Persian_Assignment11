# File Name : main.py
# Student Name: Jacob Brumfield, Justin Ganduri
# email:  brumfijb@mail.uc.edu, gandurpn@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Code that cleans a CSV file and produces an acceptable output

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant: hi

from dataPackage.data_cleaner import *

def main():
    input_file = './Data/fuelPurchaseData.csv'
    output_file = './Data/cleanedData.csv'
    anomaly_file = './Data/dataAnomalies.csv'

    cleaner = DataCleaner(input_file, output_file, anomaly_file)
    cleaner.clean_data()
    print("Data cleaned and saved to cleanedData.csv")

if __name__ == "__main__":
    main()
