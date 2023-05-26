import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import glob

# Initialize an empty set to store unique reactions for pan-genome
pan_genome_set = set()

# First iteration through the files to collect all unique reactions
for filename in glob.glob('path/to/tsv/files/*.tsv'):
    df = pd.read_csv(filename, delimiter='\t', header=None)
    reactions = df.iloc[0].values
    pan_genome_set.update(reactions)

# Map each reaction to an index
reaction_to_index = {reaction: index for index, reaction in enumerate(pan_genome_set)}

# Initialize a list to store the flux values for each patient
pan_genome_list = []

# Second iteration through the files to collect flux values
for filename in glob.glob('path/to/tsv/files/*.tsv'):
    df = pd.read_csv(filename, delimiter='\t', header=None)
    reactions = df.iloc[0].values
    flux_values = df.iloc[1:].values

    # Initialize a row for each simulation with zeros
    for flux in flux_values:
        row = [0]*len(pan_genome_set)
        for reaction, value in zip(reactions, flux):
            row[reaction_to_index[reaction]] = value
        pan_genome_list.append(row)

# Convert list to DataFrame
pan_genome_df = pd.DataFrame(pan_genome_list, columns=pan_genome_set)

# new comment

# Create the Output Matrix
labels = []  # replace with actual binary labels (cancerous or non-cancerous)
#for filename in glob.glob('path/to/tsv/files/*.tsv'):
    # Determine the label for each patient
    # Append the label to the list
    # labels.append(label)

output_matrix = np.array(labels)

# Train and Test Random Forest Model
#X_train, X_test, y_train, y_test = train_test_split(pan_genome_df, output_matrix, test_size=0.2)

#clf = RandomForestClassifier(n_estimators=100)  # Use desired parameters
#clf.fit(X_train, y_train)

#y_pred = clf.predict(X_test)

# Evaluate the model's performance
#print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
# Add more metrics as desired
