import csv
import uuid
import json
import datetime

events = [] 
eventtypes = []

def dataExtraction():
    with open("rozvrh.csv", "r", encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=';')
        # datum[0];start[1];end[2];předmět;eventtype[4];name[5];podtéma[6];učebna;učitel;...
        
        i = 0
        for row in csv_reader:
            eventtype = {}    
            event = {}
            eType = ''
            if(i>0):
                if (row[4]==''):
                    eType = 'Jiná událost'
                else: eType = row[4]

                if (checkEventtype(eType) == "0"):
                    eventtype["ID"] = str(uuid.uuid1())
                    eventtype["name"] = eType
                    eventtypes.append(eventtype)

                event["ID"] = str(uuid.uuid1())
                event["name"] = row[5]
                event["eventtype_id"] = checkEventtype(eType)
                event["startdate"] = str(convertDateTime(row[0],row[1]))
                event["enddate"] = str(convertDateTime(row[0],row[2]))

                events.append(event)


            i+=1
            if(i>3499):
                break
    
    makeJson()

def checkEventtype(etype):
    for eventtype in eventtypes:
        if (etype in eventtype.values()):
            return eventtype["ID"]
    return "0"

def convertDateTime(date, time):
    date_string = date
    day, month, year = date_string.split('.')
    day = int(day)
    month = int(month)
    year = int(year)

    time_string = time
    hour, minute = time_string.split(':')
    hour = int(hour)
    minute = int(minute)

    return (datetime.datetime(year, month, day, hour, minute))

def makeJson():
    data = {}

    data["events"] = events
    data["eventypes"] = eventtypes

    with open("scrapedData.json", "w", encoding="utf-8") as out_file:
        json.dump(data, out_file, indent = 4, ensure_ascii = False)   

# 'events': [
#     {
#         'id': "45b2df80-ae0f-11ed-9bd8-0242ac110002" , 'name': 'Zkouška', 'name_en': 'Exam', 
#         'eventtype_id': 'b87d3ff0-8fd4-11ed-a6d4-0242ac110002',
#         'startdate': datetime.datetime(year=2022, month=11, day=2, hour=8, minute=0), 
#         'enddate': datetime.datetime(year=2022, month=11, day=2, hour=10, minute=0)
#     }

# 'eventtypes' : [
#       {'id': "c0a12392-ae0e-11ed-9bd8-0242ac110002" , 'name': 'P', 'name_en': ''},

print(eventtypes) 
