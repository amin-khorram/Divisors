def divisors(integer):
    result=[]
    for n in range (2, integer):
        if integer%n==0 and n!=integer:
            result.append(n)
            result.sort()
    if len(result)==0:
        result= str(integer)+" "+"is prime"
    return result



