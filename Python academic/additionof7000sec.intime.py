
class Time:
   pass
def increment (time, seconds):
    time.second=time.second+seconds
    if time.second>=60:
       s= time.second/60
       time.second=time.second-int(s) *60
       time.min=time.min + int(s)
    if time.min >= 60:
       m=time.min/60
       time.min=time.min-int(m) *60
       time.hour=time.hour+int(m)
    if time.hour>=12:
        time.hour = time.hour-12
    return time
def print_time(t):
    print('H',t.hour, 'M',t.min, 'S',t.second)
start = Time()
start.hour=9
start.min=45
start.second=0
seconds = 7000
done=increment(start, seconds)
print_time(done)

