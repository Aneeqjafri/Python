#Function to take input from user and return a list of numbers 
def input_numbers(): 
    n = int(input("Enter how many numbers you want to sort: ")) 
    numbers = [] 
    for i in range(n): 
        num = int(input(f"Enter number {i+1}: ")) 
        numbers.append(num) 
    return numbers 
#Function to sort and print in ascending order 
def sort_ascending(numbers): 
    asc = sorted(numbers) 
    print("Ascending order:", asc) 
#Function to sort and print in descending order 
def sort_descending(numbers): 
    desc = sorted(numbers, reverse=True) 
    print("Descending order:", desc) 
#Main logic 
nums = input_numbers() 
sort_ascending(nums) 
sort_descending(nums)
