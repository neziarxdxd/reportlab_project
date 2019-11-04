collect = ['a','b','c','d','e','f','g','h', 'j']
x=0

for i in range(len(collect)):
    for j in range(2):
        print(collect[i], "x:{},y:{}".format(x,  ((i%2)*5) + 5  ))
        break
    x+=1

    if x ==2:
        x=0
    
    


    if i%4==3:
        print("\n------------")
