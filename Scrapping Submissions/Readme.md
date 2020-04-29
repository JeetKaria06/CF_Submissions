# CF_Submissions_Scrapping
One can scrap the correct submissions made in [codeforces](https://codeforces.com/) of a particular user.

## Introduction
People used to save the files to their PC before making any submissions to any problem. This seems very long process when he/she is feeling lazy. So, you don't need to do it anymore. Just input your ```handle``` of [CodeForces](https://codeforces.com/) and also the directory where you want to store all your submissions and then just relax because you are actually done.

### Note : In case of multiple submissions it will save the latest submission made.

## Dependencies
Before running main script run
```
pip install -r prerequesites.txt
```
to install all of the dependencies

## Steps to run
Suppose the name of the user ```handle``` is ```Jeet_Karia``` and the ```path``` to the directory where you want to store all the files is ```D:/Activities/Developer/Test```

```
python scrap-cf-sub.py --handle Jeet_Karia --dir D:/Activities/Developer/Test
```

Sample Output in my case:
```
Saving...
Approx Time = 0.77 min
Done!
```

### Note : In case if it misses any language then it will store that file in .cpp extension and will also display the names of that files in the output.
Let me know the issues if found any.
