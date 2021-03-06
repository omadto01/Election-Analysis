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
    #for row in file_reader:
        #print(row)  

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

#add, commit and push to GITHUB when it's back!


# Add our dependencies. Get Total Votes!
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)  

# Add our dependencies. Get Candidates list Name(s)
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# Print the candidate list.
#print(candidate_options)

# Add our dependencies. Get Candidates list Name(s) "If" to get filter duplicate
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Add our dependencies. Mod 3.5.3
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. align to "if"
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts. Mod 3.5.4 %
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

# Winning Candidate and Winning Count Tracker Mod 3.5.5
winning_candidate = ""
winning_count = 0
winning_percentage = 0    

# Determine the percentage of votes for each candidate by looping through the counts. Mod 3.5.5 %
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    winning_candidate_summary =(
        f"-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:1f}%\n"
        f"-------------------\n"
    )

    print(winning_candidate_summary)

# Add our dependencies. Complete code adding results to Txt file.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
  
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        # Save the final vote count to the text file.
    txt_file.write(election_results)  
    for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate, their voter count, and percentage to the terminal.
    print(candidate_results)
#  Save the candidate results to our text file.
    txt_file.write(candidate_results) 
    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
    
# Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
