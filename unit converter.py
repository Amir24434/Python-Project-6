
def km_miles(number):
    answer = number * 0.621
    return answer

def miles_km(number):
    answer = number/0.621
    return answer

def c_f(number):
    answer = number + 32
    return answer

def f_c(number):
     answer = number - 32
     return answer
 
def kg_p(number):
    answer = number * 2.205
    return answer

def p_kg(number):
    answer = number / 2.205
    return answer

while True:
    try:
        number = float(input("Enter the number you wish to convert: "))
        options = ["Km to miles", "miles to Km", "Celsius to Fahrenheit", "Fahrenheit to Celsius", "Kg to Pounds", "Pounds to Kg"]

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")    
            
            
        user = input("Choose an option above for conversion: ")

        if user == "1":
            answer = km_miles(number)
            print(f"{number} km is equivalent to {answer:.2f} miles")
            
        elif user == "2":
            answer = miles_km(number)
            print(f"{number} miles is equivalent to {answer:.2f} km")
            
        elif user == "3":
            answer = c_f(number)
            print(f"{number} celsius is equivalent to {answer:.2f} fahrenheit")
            
        elif user == "4":
            answer = f_c(number)
            print(f"{number} fahrenheit is equivalent to {answer:.2f} celsius")
            
        elif user == "5":
            answer = kg_p(number)
            print(f"{number} kg is equivalent to {answer:.2f} pounds")
            
        elif user == "6":
            answer = p_kg(number)
            print(f"{number} pounds is equivalent to {answer:.2f} kg")
            
        else:
            print("Invalid Input!")
            
        again = input("Do you still want to perform more conversions? (y or n): ")
        
        if again != "y".lower():
            print("Exiting app.......")
            break
    
    except ValueError:
        print("Invalid number!")
    
    

    