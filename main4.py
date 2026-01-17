#code to square numbers in a given range
starting_number=int(input("Enter the starting number: "))
ending_number=int(input("Enter the ending number: "))
squared_numbers=[]
for num in range(starting_number, ending_number + 1):
    squared_numbers.append(num ** 2)
print("List of squared numbers:", squared_numbers)
#separate odd squares from even squares
odd_squares=[]
even_squares=[]
for num in squared_numbers:
    if num % 2 == 0:
        even_squares.append(num)
    else:
        odd_squares.append(num)
print("Odd squares:", odd_squares)
print("Even squares:", even_squares)