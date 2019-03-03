import csv

#found, missing, one_contact, two_contact

open_responses = open('PPRI Responses.csv')
responses = csv.reader(open_responses)

all_re_responses = []
list_b = []

for row in responses: 
    
    caseID = row[0]
    RE_person = row[1]
    RE_email = row[2]
    
    list_b = [caseID, RE_person]
    all_re_responses.append(list_b)
        
            
open_responses.close()





open_unknown = open('PPRI Unknown.csv')
unknown = csv.reader(open_unknown)

all_unknown = []
found = []
missing = []
list_p = []

for row in unknown: 
    
    caseNum = row[0]
    district = row[1]
    district_cap = district.upper()
    RE_role = row[2]
  
    list_p = [caseNum, district_cap, RE_role]
    all_unknown.append(list_p)
    
    
               
open_unknown.close()





open_contacts = open('PPRI Contacts.csv')
contacts = csv.reader(open_contacts)

one_contact = []
two_contact = []
compList = []
nameList = []

for row in contacts: 
    
    caseNumber = row[0]
    RE_name = row[1]
    RE_type = row[2]
    RE_contactRole = row[3]
    RE_contactName = row[4]
    workEmail = row[5]
    workPhone = row[6]
    
    goodList = [RE_name, RE_contactName, RE_contactRole, workEmail, workPhone]
    list_a = [RE_contactName, RE_contactRole, workEmail, workPhone]
    compList.append(goodList)
    nameList.append(RE_name)
    
    for x in all_re_responses:
        if x[1] in list_a:
            goodList.append('RESPONDED TO SURVEY')
            goodList.append(x[0])
                       
        
open_contacts.close()






nameBox2 = set([x for x in nameList if nameList.count(x) > 1])

counter = 0


for x in all_unknown:
    
    if x[1] and x[2] in compList[counter]:
        found.append(x)
        
    else:
        missing.append(x)
    counter += 1

for x in compList:
    if x[0] in nameBox2:
        two_contact.append(x)
    if x[0] not in nameBox2:
        one_contact.append(x)
        

with open('OneContact.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(one_contact)

csvFile.close()


with open('TwoContact.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(two_contact)

csvFile.close()


with open('found.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(found)

csvFile.close()


with open('missing.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(missing)

csvFile.close()
