
# Python Imports
import csv
import os

# Load file paths
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
            #Start Counting votes
        candidate_votes[candidate_name] += 1

# Save to text
with open(file_to_save, "w") as txt_file:

    # Printing
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Printing Process to new file --- like before.
    for candidate_name in candidate_votes:

        # Count and Percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print Results to terminal and save file
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winner details
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print 
    winning_candidate_results = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n")
    print(winning_candidate_results)
    txt_file.write(winning_candidate_results)