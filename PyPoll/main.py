import csv
import os

fileData=os.path.join("Resources","02-Homeworks_03-Python_Instructions_PyPoll_Resources_election_data.csv")

CandidateData=[]
with open(fileData, "r", encoding="UTF-8") as csvfile:
    cvsreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(cvsreader)
    for row in cvsreader:
        CandidateData.append(row[2])

total=len(CandidateData)
Candidates=[]
Votes=[]
for candidate in set(CandidateData):
    Candidates.append(candidate)
    Votes.append(CandidateData.count(candidate))

Summary=zip(Candidates, Votes)
ElectionsResults=sorted(Summary, key=lambda x: x[1], reverse=True)

print(f'''Election Results
-----------------------------------------------
Total Votes: {int(total):,}
-----------------------------------------------''')
for CandidateResults in ElectionsResults:
    percentCandidate=(CandidateResults[1]/total)
    print(f'{CandidateResults[0]}  : {percentCandidate:.2%} ( {CandidateResults[1]:,})')
print(f'''-----------------------------------------------
Winner: {ElectionsResults[0][0]}
-----------------------------------------------''')

ElectionsFile=os.path.join("Analysis","Election_Results.txt")

with open(ElectionsFile, "w", newline='', encoding="UTF-8") as datafile:
    writer=csv.writer(datafile)
    writer.writerow(['Election Results'])
    writer.writerow(['-----------------------------------------------'])
    writer.writerow(['Total Votes: {:n}'.format(total)])
    writer.writerow(['-----------------------------------------------'])

    for row in ElectionsResults:
        writer.writerow([str(row[0])+': {:.2%}'.format(row[1]/total)+' ( {:n})'.format(row[1])])

    writer.writerow(['-----------------------------------------------'])
    writer.writerow(['Winner: '+str(ElectionsResults[0][0])])
    writer.writerow(['-----------------------------------------------'])