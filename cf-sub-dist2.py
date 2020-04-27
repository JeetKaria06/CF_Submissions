import requests
import json
import argparse
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots

ap = argparse.ArgumentParser()
ap.add_argument("-handle", "--handle", required=True, help="Handle of the user whose details you are looking for.")
args = vars(ap.parse_args())

handle = args["handle"]
response = requests.get("https://codeforces.com/api/user.status?handle="+handle+"&from=1")

stat = response.json()['result']

tot = []
subData = {}
subDataRate = {}
subNum = {}
for submission in stat:
    # print(submission)
    tot.append(submission['verdict'])
    if((submission['verdict'] in subData.keys())==False):
        subData[submission['verdict']] = {}
        subData[submission['verdict']]['rating'] = {}
        subData[submission['verdict']]['tag'] = {}
    
    if('rating' in submission['problem'].keys()):
        subData[submission['verdict']]['rating'][str(submission['problem']['rating'])] = []
    for tag in submission['problem']['tags']:
        subData[submission['verdict']]['tag'][tag] = []

for submission in stat:
    if('rating' in submission['problem'].keys()):
        subData[submission['verdict']]['rating'][str(submission['problem']['rating'])].append(submission['problem']['name'])
    for tag in submission['problem']['tags']: 
        subData[submission['verdict']]['tag'][tag].append(submission['problem']['name'])

dfSub = pd.DataFrame({'verdict': [], 'tag': [], 'Number': []})
dfSubRate = pd.DataFrame({'verdict': [], 'rating': [], 'Number': []})

for verdict in set(tot):
    subNum[verdict] = subData[verdict]
    for rating in subData[verdict]['rating']:
        subNum[verdict]['rating'][rating] = len(set(subData[verdict]['rating'][rating]))
        dfSubRate = dfSubRate.append({'verdict': verdict, 'rating': rating, 'Number': subNum[verdict]['rating'][rating]}, ignore_index=True)

    for tag in subData[verdict]['tag']:
        subNum[verdict]['tag'][tag] = len(set(subData[verdict]['tag'][tag]))
        dfSub = dfSub.append({'verdict': verdict, 'tag': tag, 'Number': subNum[verdict]['tag'][tag]}, ignore_index=True)

fig = px.sunburst(dfSubRate, values='Number', path=['verdict', 'rating'], title='Codeforces Submission Distribution of '+handle, color_discrete_sequence=px.colors.sequential.RdBu)

fig.update_layout(margin = dict(l=0, r=0, b=0))
fig.show()
