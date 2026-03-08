math= int(input("enter math mark"))
bio = int(input("enter bio mark"))
db= int(input("enter db mark"))        
total= math + bio + db
avg= total/3
print("total marks are", total, " and average is", avg)
if avg < 40 and avg >= 0:
    print("fail")
else:
    print("try again")
if avg >= 40 and avg < 50:
    print("C grate")
if avg >= 50 and avg < 60:
    print("B grate")
if avg >= 60 and avg <= 80:
    print("A grate")
if avg > 80 and avg <= 100:
    print("A+ grate")
       
        
    