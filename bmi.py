"""Arif Dinulsyah Putra"""
weight = 70
height = 1.86
bmi = weight/height**height
if bmi >= 40:
    print "Very severely obese"
elif bmi >= 35:
     print "Severely obese"
elif bmi >= 30:
    print "Moderately obese"
elif bmi >= 25:
    print "Overweight"
elif bmi >= 18.5:
    print "Normal (healthy weight)"
elif bmi >= 16:
    print "Underweight"
elif bmi >= 15:
    print "Severely underweight"
else:
    print "Very Severely underweight"
