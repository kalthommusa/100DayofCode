#task1 for week6
#a recursive function that calculates the power of a number
def power(base,exp): 
    if(exp==1):
        return(base)

    if(exp!=1):
        return (base*power(base,exp-1))
"""
calling the recursive function
and passing the values of the base & exponential 
"""
print("Result:",power(5,3))