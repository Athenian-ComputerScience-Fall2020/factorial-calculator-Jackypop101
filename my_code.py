# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Megan
def factorial_calc(num):   #you may choose the name of the parameter
    factorial = 1
    for i in range (1,(num)+1):
        factorial = factorial * i
    return factorial   

if __name__ == '__main__':
   num = int(input("Pick a number to be factorialize:"))
   print(factorial_calc(num))

    #print(factorial_calc(int(num)))
    # Test your code with this first
    # Change the argument to try different values


    # After you are satisfied with your results, use input() to prompt the user for a value:
    
