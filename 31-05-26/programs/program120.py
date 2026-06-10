def compound_intrest(p,t,r,n):
    a=p*(1+(r/n))**(n*t)
    return round(a,2)
print(compound_intrest(1000,5,0.05,12))
