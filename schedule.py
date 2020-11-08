p1 = [['08:00','09:00'], ['10:00', '11:30'],['14:00','15:00']]
p2 = [['09:45', '10:30'],['15:00','16:00']]

def convertToMinutes(time):
    minutes = int(time[:2])*60 + int(time[3:])
    return minutes

def scheduleInMinutes(schedule, minuteSchedule):
    for meeting in range(len(schedule)):
        for time in range(2):
            minuteSchedule[meeting][time] = convertToMinutes(schedule[meeting][time])

def sort(schedule):
    length = len(schedule)
    print(length)
    
    

p1Min = p1
p2Min = p2
scheduleInMinutes(p1,p1Min)
scheduleInMinutes(p2,p2Min)
mergedSch = p1Min+p2Min
#print(mergedSch)
mergedSch.sort
print(mergedSch)
sort(mergedSch)
