import random  # importing random
import time # importing time
OPERATORS = ["+", "-", "*"] 
MIN_VALUE = 2
MAX_VALUE = 12
TOTAL_PROBLEMS = 12

def generate_math_problems(): #creating a function to generate the random math problems
    left = random.randint(MIN_VALUE, MAX_VALUE) #generating the random value for the left
    right = random.randint(MIN_VALUE, MAX_VALUE) #generating the random value for the right
    operator = random.choice(OPERATORS) #random operators choosing
    
    expression = str(left) + " " + operator +  " " + str(right)
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Please enter to continue")
print("-------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_math_problems()
    while True:
        guess = input("Problem #" +str(i+1) + ":" + expression + "=")
        if guess == str(answer):
            break 
        wrong +=1

end_time = time.time()
total_time = end_time - start_time

print("----------------")
print("Good job! You finished in ", total_time, "seconds!")


    