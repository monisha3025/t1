def marks(g):
    if g>=90 and g<=100:
        return "Grade A"

    elif  g >= 80 and g<90:
        return "Grade B"

    elif g >= 70 and g <80:
        return "Grade C"
    else:
        return "FAIL"

g=float(input("Enter your score :"))
print(marks(g))