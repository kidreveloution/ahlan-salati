import requests
import datetime
#Given the location, this file spits out the .ics file.

def createEvent(name,day,time,f):
    dayStrip = datetime.datetime.strptime(day, '%d-%m-%Y')
    day = dayStrip.strftime("%d")
    month = dayStrip.strftime("%m")
    year = dayStrip.strftime("%Y")

    prayerTime = int(time.replace(':',''))

    prayerTime = str(check24(prayerTime))
    
    
    tempEnd = int(prayerTime) +500
    if len(str(tempEnd)) < 6:
        tempEnd = '0' + str(tempEnd)
    else:
        tempEnd = str(tempEnd)
    tempEnd = checkMinutes(tempEnd)
    #print(tempEnd)

    beginEvent = str(year)+str(month)+str(day)+str("T")+str(prayerTime)
    endEvent = str(year)+str(month)+str(day)+str("T")+str(tempEnd)

    eventString = "\nBEGIN:VEVENT\nDTSTART:"+beginEvent+"\nSUMMARY:"+name+"\nDESCRIPTION:"+"\nDTEND:"+endEvent+"\nEND:VEVENT\n"
    f.write(eventString)

def checkMinutes(tempEnd):
    tempMinute = list(tempEnd)
    #print(tempMinute)
    if  tempMinute[2] == '6':
        #print("Function was used")
        tempMinute[2] = '0'
        tempMinute[1] = str(int(tempMinute[1])+1)    
    tempMinute = "".join(tempMinute)
    return(tempMinute)

def getSalat(lat,long,daysToGet,f):
    today = datetime.date.today()

    year = today.year
    response = requests.get("http://api.aladhan.com/v1/calendar/"+str(year)+"?latitude="+str(lat)+"&longitude="+str(long)+str("&method=2"))

    data = response.json()
    getCalander(data,daysToGet,f)

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


def getCalander(jsonFile,daysToGet,f): #need to be able to handle next 30 days from a given point 
    today = datetime.date.today()
    for x in range(0,daysToGet): #should not start at 1, should start at the current day
        date = today + datetime.timedelta(days=x)
        singluarDay = date.strftime("%d").lstrip("0")
        month = date.strftime("%m").lstrip("0")

        day = jsonFile["data"][str(month)][int(singluarDay)-1]["date"]["gregorian"]["date"]
        prayerDay = jsonFile["data"][str(month)][int(singluarDay)-1]["timings"]
        fajr = str(prayerDay["Fajr"][:-6]+str(":00"))
        dhuhr = str(prayerDay["Dhuhr"][:-6] +str(":00"))     
        asr = str(prayerDay["Asr"][:-6]+str(":00"))
        maghrib = str(prayerDay["Maghrib"][:-6]+str(":00"))
        isha = str(prayerDay["Isha"][:-6]+str(":00"))
        createEvent("Fajr",day,fajr,f)
        createEvent("Dhuhr",day,dhuhr,f)
        createEvent("Asr",day,asr,f)
        createEvent("Maghrib",day,maghrib,f)
        createEvent("Isha",day,isha,f)


def mainFunc(lat, long, daysToGet):
    f = open("/tmp/mySalat.ics", "w")
    f.write("BEGIN:VCALENDAR\n")
    cal = getSalat(long, lat, daysToGet,f)
    f.write("\nEND:VCALENDAR\n")


#testing area
if __name__ == "__main__":
    f = open("myics.ics", "w")
    print("Initiate Testing")
    f.write("BEGIN:VCALENDAR\n")
    cal = getSalat(42.322140,-83.175941,35)

    f.write("\nEND:VCALENDAR\n")

#mainFunc(-83,42)



