# CF_Submissions_Visualization_Using_Plotly
One can visualize the submission distribution in codeforces by inputting handle of the user.

## Introduction
The problem that I was facing that I was not able to see the number of problems that I have solved and I obviously can't count it if it has reached above some limit and even there are multiple submissions for each problem and also it is time-consuming. So, I have come up with a solution which not only tells the number of problems that were accepted but also tells the number of unaccepted problems, TLE, MLE, etc. and visualized it using pie-chart.

### Note : It shows the number of unique problems solved/unsolved and not the repeated submissions.

Run below before running the main script to fulfill the prerequisites
```
pip install -r prerequisites.txt
```

Supposing you want to visualize the submission distribution of ```Jeet_Karia``` (handle name on [CodeForces](http://codeforces.com/))
```
python cf-sub-dist.py --handle Jeet_Karia
```

Sample Output is:
![Output](https://github.com/JeetKaria06/CF_Submissions_Visualization_Using_Plotly/blob/master/output.png)

