import requests

#Given the location, this file spits out the .ics file.

def createEvent(name,day,time,f):
    trueDay = day.replace('-','')
    prayerTime = int(time.replace(':',''))
    #print(prayerTime)
    prayerTime = str(check24(prayerTime))
    beginEvent= str(trueDay)+str("T")+str(prayerTime)
    tempEnd = int(prayerTime) +500


    if len(str(tempEnd)) < 6:
        tempEnd = '0' + str(tempEnd)
    else:
        tempEnd = str(tempEnd)
    
    tempEnd = checkSecs(tempEnd)
    
    endEvent = str(trueDay)+str("T")+str(tempEnd)
    eventString = "\nBEGIN:VEVENT\nDTSTART:"+beginEvent+"\nSUMMARY:"+name+"\nDESCRIPTION:"+"\nDTEND:"+endEvent+"\nEND:VEVENT\n"
    f.write(eventString)
    #print(eventString)

def checkSecs(tempEnd):
    tempCheck = tempEnd
    print(type(tempCheck))
    tempCheck = tempCheck[2:]
    tempCheck = int(tempCheck)

    print("The Integer is",tempCheck)
    print (len(str(tempCheck)))
    print(tempCheck)
    if len(str(tempCheck)) == 4:
        if tempCheck >= 6000:
            print(tempEnd)

            tempEnd = int(tempEnd) - 6000
            tempEnd = tempEnd + 10000
            tempEnd = str(tempEnd)
    else:
        if tempCheck >= 600:
            print(tempEnd)
            tempEnd = int(tempEnd) - 600
            tempEnd = tempEnd + 1000
            tempEnd = '0' + str(tempEnd)

    print(tempEnd)

    return(tempEnd)

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
    f = open("myics.ics", "w")
    f.write("\nBEGIN:VCALENDAR\n")
    cal = getSalat(lat, long, f)
    f.write("\nEND:VCALENDAR\n")


#testing area
if __name__ == "__main__":
    f = open("myics.ics", "w")
    f.write("\nBEGIN:VCALENDAR\n")
    cal = getSalat(-83,42,f)
    f.write("\nEND:VCALENDAR\n")

mainFunc(-83,42)



