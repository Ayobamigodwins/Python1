swim = int(input("Swimming time100m[in seconds]"))
if swim < 40:
    swim = 5
elif swim < 45 and swim >= 40:
    swim = 4
elif swim < 50 and swim >= 45:
    swim = 3
elif swim < 55 and swim >= 50:
    swim = 2
elif swim < 60 and swim >= 55:
    swim = 1
elif swim >= 60:
    swim = 0
    SW = swim
    