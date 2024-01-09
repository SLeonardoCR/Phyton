import numpy as np
import line_profiler

@profile
def my_fib_iter1(n):
    out = np.zeros(n)
    
    out[:2] = 1
    
    for i in range(2, n):
        out[i] = out[i-1] + out[i-2]
        
    return out

@profile
def my_fib_iter2(n):
    
    out = [1, 1]
    
    for i in range(2, n):
        out.append(out[i-1]+out[i-2])
    
    return np.array(out)

my_fib_iter1(1000000)
my_fib_iter2(1000000)