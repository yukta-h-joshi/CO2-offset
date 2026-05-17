import css 

la=int(input("enter land area") )
ts=int(input("tree species: 1.neem 2.ashoka 3.magnolia"))
ars=int(input("enter arrangment style"))

if ts==1:
    ts="neem absorbtion rate"
    if ars==1:
        ars="number of trees"
    elif ars==2:
        ars="number of trees"
    elif ars==3:
        ars="number of trees"
    co=la*ts*ars
elif ts==2:
    ts="neem absorbtion rate"
    if ars==1:
        ars="number of trees"
    elif ars==2:
        ars="number of trees"
    elif ars==3:
        ars="number of trees"
    co=la*ts*ars
elif ts==3:
    ts="neem absorbtion rate"
    if ars==1:
        ars="number of trees"
    elif ars==2:
        ars="number of trees"
    elif ars==3:
        ars="number of trees"
    co=la*ts*ars
print ("your co2 absorbtion rate is",co)
        
