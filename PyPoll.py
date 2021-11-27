# The data we need to retrieve.
#1.Total number of votes cast
#2. A complete list of candidates who received votes
#3.Total number of votes each candidate received
#4.Percentage of votes each candidate won
#5.The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime
from typing import ClassVar
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Assign a variable for the file to load and path
file_to_load = "Resources/election_results.csv"

election_data = open(file_to_load, 'r') 

with open(file_to_load) as election_data:

      print(election_data)

election_data.close

#Mode "r" read 
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

with open(file_to_load) as election_data:

    #Print the file object
    print(election_data)

#Mode "w" write
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_save = os.path.join("analysis","election_analysis.txt")
open(file_to_save, "w")
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data) 

#Mode "w" write Outfile
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_save = os.path.join("analysis","election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World!!!")
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data)   
outfile.close()   

#Mode combine "r" & "w" & oufile and txtfile "Hello World"
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data) 

with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello World!")
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")
     
txt_file.close() 

#Mode txtfile "Arapahoe, Denver, Jefferson"
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data) 

with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.write("Arapahoe, Denver, Jefferson")
     
txt_file.close() 

#Mode txtfile \n ("Arapahoe\nDenver\nJefferson")
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data) 

with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")
     
txt_file.close() 

#Mode txtfile \n ("Arapahoe\nDenver\nJefferson") with Header
import csv
import os
#Assign a variable for the variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data) 

with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.write("Counties in the Election\n")
     txt_file.write(("-" * 10) + "\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")
     
txt_file.close() 

# Add our dependencies. pull from csv
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

# Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
# Print each row in the CSV file.
    for row in file_reader:
        print(row)  

# Add our dependencies. pull from csv with Header
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)            

#add, commit and push to GITHUB     