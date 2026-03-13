sprint = int(input("Sprint time 100m [in seconds]: "))
if sprint <20:
    sprint = 5
elif sprint <25 and sprint >=20:
    sprint = 4
elif sprint <30 and sprint >=25:
    sprint = 3
elif sprint <40 and sprint >=30:
    sprint = 2
elif sprint <50 and sprint >=40:
    sprint = 1
elif sprint <60 and sprint >=50:
    sprint = 0
    SP = sprint