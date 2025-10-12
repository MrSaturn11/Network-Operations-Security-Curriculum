from scapy.all import *

def tracer(dst, max_hops = 30):
    a = IP()
    b = ICMP()
    a.dst = dst
    for ttl in range(1, max_hops + 1):
        a.ttl = ttl
        pkt = a/b #ICMO Echo requests are defined by IP()/ICMP()

        reply = sr1(pkt, timeout = 2, verbose=0) #send and recieve 1 packet
        #verbose = 0 just cleans up the printout 
        if reply and reply.type==0:
            print(ttl, ":", reply.src)
            print("Destination Reached")
            break
        elif reply:
            print(ttl,":",reply.src)

tracer("8.8.8.8") #calls the tracer function above
