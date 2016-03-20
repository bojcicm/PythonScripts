import re 

with open("data.html", "r") as configFile:
    data = configFile.readlines()

addEmployeeCounter = 0
totalTestCounter = 0

for row in data:
    if "test-suite" in row:
        suite = re.search('test-suite="(.+?)"', row).group(1)
        with open(suite,"r") as suiteFile:
            suiteData = suiteFile.readlines()
        for caseRow in suiteData:
            if 'test-case="./Data/Add cakes.html"' in caseRow:
                addEmployeeCounter += 1
            if 'test-case' in caseRow:
                totalTestCounter += 1

percentage = float(addEmployeeCounter) / totalTestCounter
percentage = percentage * 100

print 'Ukupno testova: {}'.format(totalTestCounter) 
print 'Add cakes: {}'.format(addEmployeeCounter)
print 'Postotak Add cakes testova: {0:.2f}%'.format(percentage)
