def fibonacci(n):
    """
    function that solve a Fibonacci series
    Arguments:
        n:integer;the number of sequence 
    Returns:
        Number that is in  Fibonacci series
    """
    if n ==0:
        return n
    elif n==1:
        return n 
    else:
        return fibonacci(n-1)+ fibonacci(n-2)



def lucas(n):
    """
    function that solve a lucas series
    Arguments:
        n:integer;the number of sequence 
    Returns:
        Number that is in  lucas series
    """
    if n ==2:
        return n
    elif n==1:
        return n 
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n,a=0,b=1):
    """
    function that solve a sum series similar to Fibonacci and Lucas
    Arguments:
        n:integer;the number of sequence 
        a:optional integer; value of series at index 0
        b:optional integer; value of series at index 1
    Returns:
        Number similar to Fibonacci and Lucas series 
        but could be any other math series based on the first two values
    """
    if a==0 and b==1:
        return fibonacci(n)
    elif a==2 and b==1:
        return lucas(n)
    else:
        return n 

print(sum_series(4))