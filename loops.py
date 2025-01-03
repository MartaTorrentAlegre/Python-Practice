 # Print numbers 1 to 10 using a for loop
for i in range (1, 11):
    print (i)

# Print in a multiplication table
num = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Countdown from 10 using a loop
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
