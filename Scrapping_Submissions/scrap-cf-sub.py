import requests
import json
from bs4 import BeautifulSoup
import time
import argparse

lang = {".c":["GNU C11"], ".cs":["Mono C#"], ".cpp":["Clang++17 Diagnostics", "GNU C++11", "GNU C++14", "GNU C++17", "MS C++", "MS C++2017"], 
        ".d": ["D"], ".go":["Go"], ".hs":["Haskell"], ".java":["Java 11", "Java 8"], ".js":["JavaScript", "Node.js"], ".kt":["Kotlin"], ".mli":["Ocaml"]
        , ".pas": ["Delphi", "FPC", "PascalABC.NET"], ".pl": ["Perl"], ".php":["PHP"], ".py": ["Python 2", "Python 3", "PyPy 2", "PyPy 3"], ".rb":["Ruby"]
        , ".rs": ["Rust"], ".scala": ["Scala"]}

defExt = '.cpp'
probs = []

ap = argparse.ArgumentParser()
ap.add_argument("-handle", "--handle", required=True, help="Handle of the user whose submissions you want to scrap.")
ap.add_argument("-directory", "--dir", required=True, help="path to the dir where you want to store all the submissions' source code.")
args = vars(ap.parse_args())

handle = args["handle"]
response = requests.get("https://codeforces.com/api/user.status?handle="+handle+"&from=1")

stat = response.json()['result']
okList = []
proList = []
i=0
for submission in stat:
    if i==0:
        print("Saving...")
    if submission['verdict']=='OK':
        okList.append(submission['problem']['name'])
    i=i+1

i=0
for submission in stat:
    # print(submission)

    if(submission['verdict']=='OK' and (submission['problem']['name'] not in proList)):
        proList.append(submission['problem']['name'])
        start = time.time()
        url = "https://codeforces.com/contest/"+str(submission['problem']['contestId'])+"/submission/"+str(submission['id'])
        resp = requests.get(url, timeout=161380)
        
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            plang = soup.find("table", {"class": ""})
            l = soup.find("pre", {"id":"program-source-text"})

            j=0
            for pl in plang.find_all('td'):
                j=j+1
                if(j==4):
                    plang = pl.text.strip()
                    break
            
            extension = [key for key, val in lang.items() if plang in val]
            if(extension==[]): 
                probs.append(str(submission['problem']['contestId'])+submission['problem']['index']+".cpp")
                extension = [defExt]

            file = open(args["dir"]+"/"+str(submission['problem']['contestId'])+submission['problem']['index']+extension[0], "w")   
            file.write(l.text)

            file.close()
            end = time.time()
            if i==0:
                print("Approx Time = {:.2f}".format((end-start)*len(set(okList))/60)+" min")
        else:
            print("Error Occurred.")
        i=i+1
print("Done!")

if(len(probs)>0):
    print("Following source codes file extension is .cpp as I don't know about them:")
    print(probs)
