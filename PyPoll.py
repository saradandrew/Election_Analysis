import csv
import os
file_to_load = os.path.join("Downloads","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
with open(file_to_save, "w") as txt_file:
    txt_file.write("Acrapahoe\nDenver\nJefferson")