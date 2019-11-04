collect = ['a','b','c','d','e','f','g','h', 'j']
l =len(collect)
a =0
for x in range(l):
   
    print(collect[x],a%2,((x%2)*5)+5)
    if x%2==0:
        a+=1
    if x%4==3:
        print("---------")
        