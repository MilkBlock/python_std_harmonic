a = 1
for i in range(5):
    if i ==2:
        print("enter break")
        break
    a+=1
    if i ==4:    
        print("range has been finished")
else :
    print("else has been done")
    a+=1
print(a)



def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            break
    else:
        return True
    return False

print("2 check",is_prime(2))
print("6 check",is_prime(6))
print("7 check",is_prime(7))
print("57 check",is_prime(57))