var = int(input("Please enter a positive integer:"))

print("The factors of",var,"are:")

for i in range (1, var + 1):

    if var % i == 0:

        print(i)
