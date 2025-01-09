# Draw Lots Automation -- NTU Volleyball Fields

These program helps NTUEE girl's volleyball team draw lots and generate "場單文"(A list of drawn fields)

## Description

English version

Every month, NTU sports center holds an online drawing lots activity. Volleyball teams submit the days and periods they want to use, 
and the system will randomly distribute each available time and fields to one team at the day of drawing. 
As a team member managing 5 accounts for this draw lots activity, it is a waste of time to log in and out 5 times (with complex clicks) every month. 

To save time from repetitive works, these codes provide two functions:

1. Draw lots: automatically log in and out (and hopefully in the future, select fields) with NTU sports center system.
2. Generate List: generate a list of drawn fields from email contents, and the list is ready for posting on our facebook club.

## Getting Started

### Dependencies

* python3
* a chrome driver
* python venv

### Installing

* clone this repo / download the codes.

### Executing program

1. drawing lot
- Run
```
python3 main.py
```
- Select the fields when logged in, submit
- login and out are automated by the system

2. generate list
```
python3 field_info.py
```

## Authors

[matxtam](https://github.com/matxtam/)

## Version History

* 0.1
    * Initial Release
 
## Roadmap
[x] auto login/out
[ ] UI for field preference selection
[ ] auto select fields
[x] generate field list
