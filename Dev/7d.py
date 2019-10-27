kwh = input("enter kilowatt-hours used: ")
if kwh < 0:
    print( "/nreckeck input value!")
    print( "(it was negative, and meters/ndon`t run backward.)")
else:
    if kwh <= 500.0:
        amount = 20.0
    elif kwh <= 1000.0:
        amount = 20.0 + 0.03*(kwh-500)
    else:
        amount = 35.0 + 0.02*(kwh-1000)
print "bill amount = $%1.2f" % amount


