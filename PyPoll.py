#Total number of votes cast?
"""

##A complete list of candidates who received votes?


###Total number of votes each candidate received?


####Percentage of votes each candidate won?


###The winner of the election based on popular vote?

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Assign a variable for the file to load and the path.
#file_to_load = 'Resource/election_results.csv'

# Open the election results and read the file.
#election_data = open( file_to_load , 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
    print(election_data)
"""

#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resource", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
  #   print(csv.reader(election_data))

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
   # txt_file.write("Hello World")

    #Add the counties Arapahoe, Denver, Jefferson
     #txt_file.write("Arapahoe, ")
     #txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")

          # Write three counties to the file.
    # txt_file.write("Arapahoe, Denver, Jefferson")

    # Write three counties to the file.
   #  txt_file.write("Counties in the Election\n")
   #  txt_file.write("__________________\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")


# Add our dependencies.
#import csv
#import os
# Assign a variable to load a file from a path.
#file_to_load = os.path.join("Resource", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
#total_votes = 0

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     # Read the file object with the reader function.
 #   file_reader = csv.reader(election_data)
  
     # Read the file object with the reader function.
    #file_reader = csv.reader(election_data)

    # Print the header row.
  #  headers = next(file_reader)
    #print(headers)

      # Print each row in the CSV file.
   # for row in file_reader:

        # 2. Add to the total vote count.

    # total_votes += 1

           # Print each row in the CSV file.
   # for row in file_reader:
      #  print(row)

     # 3. Print the total votes.
    #    print(total_votes)
    

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resource", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
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

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            #adding the votes per voter
        candidate_votes[candidate_name] += 1


# Print the candidate vote dictionary.
print(candidate_votes)

   #Make a dictionary for candidates 
 #  candidate_votes = {"candidate_name1":votes, "Candidate_name2": votes,"candidate_name3":Votes}

 # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # 4. Print the candidate name and percentage of votes.
   # print(f"{candidate_name}: received {vote_percentage } 0,0% of the vote.")

      #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
      f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")


print(winning_candidate_summary)
