import csv
import uuid

def dataExtraction():
    with open("rozvrh.csv", "r", encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=';')
        # datum[0];start[1];end[2];předmět;eventtype[4];name[5];podtéma[6];učebna;učitel;...
        events = []   
        i = 0
        for row in csv_reader:    
            event = {}
            if(i>0):
                event["ID"] = str(uuid.uuid1())
                event["name"] = row[5]
                event["eventtype"] = row[4]


                events.append(event)
            i+=1
            if(i>10):
                break


    print(events)        

# 'events': [
#     {
#         'id': "45b2df80-ae0f-11ed-9bd8-0242ac110002" , 'name': 'Zkouška', 'name_en': 'Exam', 
#         'eventtype_id': 'b87d3ff0-8fd4-11ed-a6d4-0242ac110002',
#         'startdate': datetime.datetime(year=2022, month=11, day=2, hour=8, minute=0), 
#         'enddate': datetime.datetime(year=2022, month=11, day=2, hour=10, minute=0)
#     }

# 'eventtypes' : [
#       {'id': "c0a12392-ae0e-11ed-9bd8-0242ac110002" , 'name': 'P', 'name_en': ''},

dataExtraction()
