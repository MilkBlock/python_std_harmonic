i = 0
target = 8000
score = 0
r = 0
while score <target:
    score += 2
    r+=2
    if r==270:
        r=0
        r+=80
        target -= 80 
    i+=1
    print(i)
    


