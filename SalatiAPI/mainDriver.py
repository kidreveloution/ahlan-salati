import requests

#Given the location, this file spits out the .ics file.

def createEvent(name,day,time,f):
    trueDay = day.replace('-','')
    prayerTime = int(time.replace(':',''))

    prayerTime = str(check24(prayerTime))
    
    
    tempEnd = int(prayerTime) +500
    if len(str(tempEnd)) < 6:
        tempEnd = '0' + str(tempEnd)
    else:
        tempEnd = str(tempEnd)
    tempEnd = checkMinutes(tempEnd)
    #print(tempEnd)


    beginEvent = str(trueDay)+str("T")+str(prayerTime)
    endEvent = str(trueDay)+str("T")+str(tempEnd)
    eventString = "\nBEGIN:VEVENT\nDTSTART:"+beginEvent+"\nSUMMARY:"+name+"\nDESCRIPTION:"+"\nDTEND:"+endEvent+"\nEND:VEVENT\n"
    f.write(eventString)
    #print(eventString)

def checkMinutes(tempEnd):
    tempMinute = list(tempEnd)
    #print(tempMinute)
    if  tempMinute[2] == '6':
        #print("Function was used")
        tempMinute[2] = '0'
        tempMinute[1] = str(int(tempMinute[1])+1)    
    tempMinute = "".join(tempMinute)
    return(tempMinute)

def getSalat(lat,long,f):
    response = requests.get("https://api.pray.zone/v2/times/this_month.json?longitude="+str(lat)+"&latitude="+str(long))
    data = response.json()
    getCalander(data,f)

def check24(time):
    if time >= 240000:
        time = time-240000
        if time <= 99999:
            time = str("0")+str(time)
            return (time) 
        return (time)
    else:
        if time <= 99999:
            time = str("0")+str(time)
            return (time) 
        return(time)


def getCalander(jsonFile,f):
     for x in range(len(jsonFile["results"]["datetime"])):
    
        day = jsonFile["results"]["datetime"][x]["date"]["gregorian"]

        fajr = jsonFile["results"]["datetime"][x]["times"]["Fajr"]+str(":00")
        dhuhr = jsonFile["results"]["datetime"][x]["times"]["Dhuhr"] +str(":00")     
        asr = jsonFile["results"]["datetime"][x]["times"]["Asr"]+str(":00")
        maghrib = jsonFile["results"]["datetime"][x]["times"]["Maghrib"]+str(":00")
        isha = jsonFile["results"]["datetime"][x]["times"]["Isha"]+str(":00")
        createEvent("Fajr",day,fajr,f)
        createEvent("Dhuhr",day,dhuhr,f)
        createEvent("Asr",day,asr,f)
        createEvent("Maghrib",day,maghrib,f)
        createEvent("Isha",day,isha,f)
        #print(day,fajr,dhuhr,asr,maghrib,isha)


def mainFunc(lat, long):
    f = open("/tmp/mySalat.ics", "w")
    f.write("\nBEGIN:VCALENDAR\n")
    cal = getSalat(long, lat, f)
    f.write("\nEND:VCALENDAR\n")


#testing area
if __name__ == "__main__":
    f = open("myics.ics", "w")
    print("Initiate Testing")
    f.write("BEGIN:VCALENDAR\n")
    cal = getSalat(-83,42,f)

    f.write("\nEND:VCALENDAR\n")

#mainFunc(-83,42)



