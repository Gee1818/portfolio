p1 = [['08:00','09:00'], ['10:00', '11:30'],['14:00','15:00']]
p2 = [['09:30', '10:30'],['16:00','17:00']]
t = 30

def convertToMinutes(time):
    minutes = int(time[:2])*60 + int(time[3:])
    return minutes

def convertToMilitary(schedule):
    for meeting in range(len(schedule)):
        for time in range(2):
            if schedule[meeting][time] < 600:
                hour = int(schedule[meeting][time] / 60)
                minutes = int(schedule[meeting][time] % 60)
                if minutes < 11:
                    schedule[meeting][time] = f'0{hour}:00'
                else:
                    schedule[meeting][time] = f'0{hour}:{minutes}'
            else:
                hour = int(schedule[meeting][time] / 60)
                minutes = int(schedule[meeting][time] % 60)
                if minutes < 11:
                    schedule[meeting][time] = f'{hour}:00'
                else:
                    schedule[meeting][time] = f'{hour}:{minutes}'

    print(schedule)

def scheduleInMinutes(schedule):
    for meeting in range(len(schedule)):
        for time in range(2):
            schedule[meeting][time] = convertToMinutes(schedule[meeting][time])
    return schedule

def sort(schedule1, schedule2, outputschedule):
    schedule1 = scheduleInMinutes(schedule1)
    schedule2 = scheduleInMinutes(schedule2)
    while len(schedule1) and len(schedule2) > 0:  
        if schedule1[0][0] < schedule2[0][0]:
            outputschedule.append(schedule1[0])
            schedule1.pop(0)
        else:
            outputschedule.append(schedule2[0])
            schedule2.pop(0)
    if len(schedule1) == 0 and len(schedule2) > 0:
        outputschedule.append(schedule2[0])
        schedule2.pop(0)
    elif len(schedule2) == 0 and len(schedule1) > 0:
        outputschedule.append(schedule1[0])
        schedule1.pop(0)

def clean(sorted,time):
    finalSchedule = []
    for meeting in range(len(sorted)-1):
        if sorted[meeting+1][0] != sorted[meeting][0]:
            if sorted[meeting][1] <= sorted[meeting+1][0]:
                finalSchedule.append([sorted[meeting][1],sorted[meeting+1][0]])

    for meeting in range(len(finalSchedule)-1):
        delta = finalSchedule[meeting][1] - finalSchedule[meeting][0] 
        if delta < time :
            finalSchedule.pop(meeting)
    print(finalSchedule)
    return finalSchedule

p3 = []
sort(p1,p2,p3)
fschedule = clean(p3,t)
convertToMilitary(fschedule)