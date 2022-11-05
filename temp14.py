def BMIfunction(name,centmeter,kg):
    BMI = kg/((centmeter/100)**2)
    if BMI > 24:
        return f"Hi {name}, Your BMI: {'%.6f'%BMI} too HIGH."
    elif BMI < 18.5:
        return f"Hi {name}, Your BMI: {'%.6f'%BMI} too LOW."
    else:
        return f"Hi {name}, Your BMI: {'%.6f'%BMI}."
    
name = input()
centmeter = int(input())
kg = int(input())
print(BMIfunction(name,centmeter,kg))