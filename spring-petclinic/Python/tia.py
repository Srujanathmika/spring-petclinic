import csv
import subprocess

# Step 1: Get changed files from Git
changed_files = subprocess.check_output(
    ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
).decode("utf-8").splitlines()

print("Changed files:", changed_files)

# Step 2: Read mapping
impacted_tests = []
with open("../mapping.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for file in changed_files:
            if row["SourceFile"].split("/")[-1] in file:
                impacted_tests.append(row["TestFile"])

print("Impacted tests:", impacted_tests)
