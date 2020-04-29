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

stat = response.json()['result']

tot = []
subData = {}
subNum = {}
for submission in stat:
    tot.append(submission['verdict'])
    subData[submission['verdict']] = []

for submission in stat:
    s = {submission['verdict']: submission['problem']['name']}
    subData[submission['verdict']].append(submission['problem']['name'])

dfSub = pd.DataFrame({'verdict': [], 'Number': []})

for verdict in set(tot):
    subNum[verdict] = len(set(subData[verdict]))
    dfSub = dfSub.append({'verdict': verdict, 'Number': subNum[verdict]}, ignore_index=True)

fig = px.pie(dfSub, values='Number', names='verdict', title='Codeforces Submission Distribution of '+handle, color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_layout(uniformtext_minsize=18, uniformtext_mode='hide')
fig.show()
