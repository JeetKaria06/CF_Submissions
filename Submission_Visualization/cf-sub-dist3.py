import requests
import json
import argparse
import plotly.express as px
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-handle", "--handle", required=True, help="Handle of the user whose details you are looking for.")
args = vars(ap.parse_args())

handle = args["handle"]
response = requests.get("https://codeforces.com/api/user.status?handle="+handle+"&from=1")

if(response.status_code==400):
    print("No such handle exists :( ")
    exit()

stat = response.json()['result']

subDict = {}

for submission in stat:
    # print(submission)
    # print()
    for tag in submission['problem']['tags']:
        if tag not in subDict.keys():
            subDict[tag] = {}
        if submission['verdict'] not in subDict[tag].keys():
            subDict[tag][submission['verdict']] = {}
        if 'rating' in submission['problem'].keys():
            subDict[tag][submission['verdict']][str(submission['problem']['rating'])] = []
        else:
            subDict[tag][submission['verdict']]['unrated'] = []

# print(subDict)

for submission in stat:
    for tag in submission['problem']['tags']:
        if 'rating' in submission['problem'].keys():
            subDict[tag][submission['verdict']][str(submission['problem']['rating'])].append(submission['problem']['name'])
        else:
            subDict[tag][submission['verdict']]['unrated'].append(submission['problem']['name'])

subData = {}
dfSub = pd.DataFrame({'tag': [], 'verdict': [], 'rating': [], 'number': []})

for tag in subDict:
    subData[tag] = subDict[tag]
    for verdict in subDict[tag]:
        for rating in subDict[tag][verdict]:
            subData[tag][verdict][rating] = len(set(subDict[tag][verdict][rating]))
            if rating == 'unrated':
                dfSub = dfSub.append({'tag': tag, 'verdict': verdict, 'rating': 'UNRATED', 'number': subData[tag][verdict][rating]}, ignore_index=True)
            else:
                dfSub = dfSub.append({'tag': tag, 'verdict': verdict, 'rating': rating, 'number': subData[tag][verdict][rating]}, ignore_index=True)

print(dfSub)

fig = px.sunburst(dfSub, values='number', path=['tag', 'verdict', 'rating'], title='Codeforces Submission Distribution of '+handle)
# fig.update_layout(uniformtext_minsize=18, uniformtext_mode='hide')
fig.update_layout(margin = dict(l=0, r=0, b=0))
fig.show()


