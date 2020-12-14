# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = input("regexp: ")
if regex != '':
    regex = r"[\"\'][a-zA-ZА-Яа-я\d\s[\]{}()\\\.:;,-]*[\"\']|\b[a-zA-Z\d]+"
test_str = input("regexp: ")


matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
input()