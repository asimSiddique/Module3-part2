#Sajal Baral, Asim Siddique, Shawn Kiruba, Kevin Avila, Shail Patel
#https://realpython.com/python-timer/
#https://docs.python.org/3/library/time.html
#Website talk about different pyton timers function to calculate time elapsed. 
#Perf Counter is one method they talked about which return the time in either seconds or nanoseconds. 

import time

def fib(n):
    if n>1:
        return (fib(n-1)+fib(n-2))
    else:
        return n

time_start=time.perf_counter()
x=fib(35)
time_stop =time.perf_counter()
total_time=time_stop-time_start

print(f"fib(35) = {x}")
print(f"fib(35) took {total_time} seconds")
