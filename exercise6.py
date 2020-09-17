# BMI (Body Mass Index) Calculator 

height = float(input("Input your height in inches(in): "))
weight = float(input("Input your weight in pounds (lbs): "))
bmi = round((weight*703)/(height*height),2)

if bmi <= 18.5:
    print('Your BMI is', bmi,'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
    print('Your BMI is', bmi,'which means you are normal weight.')

elif bmi > 25 and bmi < 30:
    print('Your BMI is', bmi,'which means you are overweight')

elif bmi > 30:
    print('Your BMI is', bmi,'which means you are obese.')

else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
              'and decimals were asked.')


