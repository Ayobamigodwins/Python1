Name = input("Type name of student")

p = int(input("Number of push ups: "))
if p >50:
     p=5
elif p<=50 and p>=40:
     p=4
elif p<40 and p>=30:
     p=3
elif p<30 and p>=20:
     p=2
elif p<20 and p>=10:
     p = 1
elif p<10:
     p=0
P1 = p

p2 = int(input("Number of pull ups:"  ))
if p2>=20:
    p2=5
elif p2<20 and p2>=15:
    p2=4
elif p2<15 and p2>=10:
    p2=3
elif p2<10 and p2>=5:
    p2=2
elif p2<5 and p2>1:
    p2=1
elif p2==0:
    p2=0
P2 = p2    
s1 = int(input("Number of sit ups: " ))
if s1 > 100:
    s1=5
elif s1 <= 100 and s1 > 75:
    s1=4 
elif s1 <= 75 and s1 > 50:
    s1=3
elif s1 <= 50 and s1 > 25:
    s1=2
elif s1 < 25 and s1 > 10:
    s1=1
elif s1 < 10:
    s1=0
S1 = s1
       
b = str(input("Basketball skill test: "))
if b == "AA":
    b = 5
elif b == "A":
    b = 4
elif b == "B":
    b = 3   
elif b == "C":
    b = 2
elif b == "D":
    b = 1
elif b == "F":
    b = 0
B = b

f = str(input("Football skill test: "))
if f == "AA":    
   f = 5
elif f == "A":
    f = 4
elif f == "B":
    f = 3
elif f == "C":
    f = 2
elif f == "D":
    f = 1
elif f == "F":
    f = 0
F = f
sprint = int(input("Sprint time for 100m in seconds : "))
if sprint <20:
    sprint=5
elif sprint <25 and sprint >=20:
    sprint=4
elif sprint <30 and sprint >=25:
    sprint=3
elif sprint <35 and sprint >=30:
    sprint=2
elif sprint <40 and sprint >=35:
    sprint=1
elif sprint >=40:
    sprint = 0
SP = sprint
swim = int(input("Swimming time for 100m in seconds:"))
if swim < 40:
    swim=5
elif swim < 45 and swim >= 40:
    swim=4
elif swim < 50 and swim >= 45:
    swim=3                  
elif swim < 55 and swim >= 50:  
    swim=2
elif swim < 60 and swim >= 55:
    swim=1  
elif swim >=60:
    swim=0 
SW = swim 
TOTAL = P1 + P2 + S1 + B + F + SP + SW

print("Total points: " + str(TOTAL))

class_name = TOTAL
if TOTAL >30 and TOTAL <=35:
    class_name = "Class A"
elif TOTAL >25 and TOTAL <=30:
    class_name = "Class B"
elif TOTAL >20 and TOTAL <=25:
    class_name = "Class C"
elif TOTAL >15 and TOTAL <=20:
    class_name = "Class D"
elif TOTAL >10 and TOTAL <=15:
    class_name = "Class E"
elif TOTAL >0 and TOTAL <=10:
    class_name ="Disqualified"
print("Class: " + str(class_name))