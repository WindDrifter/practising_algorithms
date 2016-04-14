
# this one use variable to save previous 2 instead of array
def fib(n):
    n_m_2 = 0 #f0
    n_m_1 = 1 #f1
    value = n_m_2+n_m_1 #f2
    if(n==0):
        return n_m_2
    elif(n==1):
        return n_m_1
    else:
        for i in range(2,n):
            n_m_2 = n_m_1
            n_m_1 = value
            value = n_m_1+n_m_2
        return value



print fib(12)
