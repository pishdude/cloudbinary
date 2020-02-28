import time;
import csv;
f = open("input.txt")
reqId=0;
list=[];
c=0;
o=open("output_fibonnaci.log","w");
cs=open("output_fibonnaci.csv","w",newline='');
w = csv.writer(cs)
for x in f:
    start_time=time.time();
    reqId=reqId+1;
    a=0;
    b=1;
    list=[]
    for i in range(0,int(x)):
        list.append(a)
        c= a+b;
        a=b;
        b=c;
            
        
    time_taken =(time.time() - start_time);
    log = "requestId = {},time={:.6},n={},result={}\n";
    o.write(log.format(reqId,time_taken,x,list));
    #res=reqId+","+str(ime_taken)+","+str(x)+","+list;
    w.writerow([reqId,time_taken,x,list]);

o.close();





