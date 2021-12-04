counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

    counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.") 

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)    

for i in range(len(counties)):
    print(counties[i])  

counties_tuples = ("Arapahoe","Denver","Jefferson")

for county in counties_tuples:

    print(county)
        

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])   

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])  

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)       

for county_dict in voting_data:

     print(county_dict['registered_voters'])  
         
for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")   

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multine F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

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