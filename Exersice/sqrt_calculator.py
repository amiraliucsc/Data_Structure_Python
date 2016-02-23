import math

def sqrt(number):
    start = 0;
    end = number;
    mid = (start+end)/2;
    prevMid = 0;
    diff = abs(mid - prevMid);
    precision = 0.0005;
    while((mid*mid != number) and (diff > precision)):
        if(mid*mid > number):
            end = mid;
        else:
            start = mid;
        prevMid = mid;
        mid = (start+end)/2;
        diff =abs(mid - prevMid);
    return mid
    
print(sqrt(4))