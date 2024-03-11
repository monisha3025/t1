class Grades:
    def calGra(self,g):

        if g >= 90:
            return "Grade A"

        elif g >= 80:
            return "Grade B"

        elif g >= 70:
            return "Grade C"
        else:
            return "FAIL"

# res=Grades()
# g = float(input("Enter your score :"))
# res.calGra(g)