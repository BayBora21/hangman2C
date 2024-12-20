
kill={"taha":75, "sule":57}
print(kill["taha"])
uss=kill.keys()
print(uss)
uss2=kill.values()
print(uss2)
my_dictionary_4 = {"key1" : 100, "key2" : [10,20,30], "key3" : {"a":5}}
print(my_dictionary_4["key3"]["a"])
print(my_dictionary_4["key2"][1])
setim= [1,2,2,3,3,4,1,1,2,5,7]
iki=set(setim)
print(iki)
benlist=[1,23,49]
type(list)
benlist.append("1," + " 2")
benlist.append("a")
benlist.append([1,2])
benlist.append("b")  
print(benlist)  
k=benlist.index("b")
print(k)
x=5
y=4
z=8
eger=x>y and z>x
print(eger)
forricin=[1,2,3,4,5,6]
for kstr in forricin:
    if kstr % 2== 0:
        print (kstr)
isim="taha"
print(isim[2])
a=0
while a<20:
    print(f"Sayiniz: {a} " )
    a+=1