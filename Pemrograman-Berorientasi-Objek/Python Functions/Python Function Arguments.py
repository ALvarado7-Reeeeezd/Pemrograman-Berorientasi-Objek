def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)# Output: Sum: 5

def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)# pemanggilan fungsi dengan dua argumen
add_numbers(2, 3)#  pemanggilan fungsi dengan satu argumen
add_numbers(a = 2)# pemanggilan fungsi tanpa argumen
add_numbers()

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')

# program untuk menghitung jumlah dari beberapa angka 
def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)# pemanggilan fungsi dengan 3 argumen
find_sum(1, 2, 3)# pemanggilan fungsi dengan 2 argumen
find_sum(4, 9)