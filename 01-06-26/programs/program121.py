def return_only_integers(lst):
    return [x for x in lst if isinstance(x,int) and not isinstance(x,str)]
print(return_only_integers([9,2,"Ganga","car","lion",16]))
