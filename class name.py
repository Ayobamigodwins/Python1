class_name = TOTAL
class_name = str(input("Class:"))
if TOTAL >30 and TOTAL <=35:
    class_name = "Class A"
elif TOTAL >25 and TOTAL <=30:
    class_name = "Class B" 
elif TOTAL >20 and TOTAL <=25:
    class_name ="Class C"    
elif TOTAL >15 and TOTAL <=20:
    class_name = "Class D"
elif TOTAL >10 and TOTAL <=15:
    class_name = "Class E"
elif TOTAL >0 and TOTAL <=10:
    class_name = "Disqualified"
print("Class: " + str(class_name))