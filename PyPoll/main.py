"""""
In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

"""""
import os
import csv
election_data = os.path.join("Resources" , "election_data.csv")

#variables
total_votes = 0
candidates = []
candidate_votes = {}

#index 0 = to voter ID
#index 2 = to candidates

#read csv file
with open(election_data) as election_data:
    csv_reader = csv.reader(election_data)
    # header row
    voter = next(csv_reader)


    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

        candidate_votes[row[2]] = 1
    else:
        candidate_votes[row[2]] += 1

#x = candidate_votes.count("Khan")

for candidates in candidate_votes:
    votes = candidate_votes.get(candidates)

    vote_percentage = (float(votes) / float(total_votes)) * 100.00
    print(vote_percentage)

    


#print(f"Total votes = {total_votes} ")

#print(candidate_votes)    
x = candidates.count("Correy")
print(x)