import time;
import csv;
f = open("input.txt")
o=open("output_factorial.log","w");
cs=open("output_factorial.csv","w",newline='');
w = csv.writer(cs)

reqId=0;
for x in f:
    start_time=time.time();
    reqId=reqId+1;
    factorial = 1;
    for i in range(1,int(x)+1):
        factorial = factorial * i;
    time_taken =(time.time() - start_time);
    log = "requestId = {},time={:.6},n={}.result={}";
    o.write(log.format(reqId,time_taken,x,factorial));
    w.writerow([reqId,time_taken,x,factorial]);






