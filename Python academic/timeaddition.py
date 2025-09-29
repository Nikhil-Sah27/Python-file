class Time:
  pass
def print_time(t):
    return(t.hour,t.min,t.sec)
def add_time (tl,t2):
  sum =Time()
  sum.hour= tl.hour + t2.hour
  sum.min=tl.min+t2.min
  sum.sec= tl.sec + t2.sec
  if sum.sec>=60:
    sum.sec =sum.sec-60
    sum.min=sum.min+1
  if sum.min>=60:
    sum.min= sum.min-60
    sum.hour= sum.hour+1
  return sum
t1=Time()
t1.hour = 10
t1.min= 34
t1.sec =25
print('Time is:',print_time (t1))
t2 = Time()
t2.hour = 2
t2.min =12
t2.sec =41
print('Time is:',print_time(t2))
t3=add_time(t1,t2)
print('Aft adding 2 times, Time is:', print_time(t3))
