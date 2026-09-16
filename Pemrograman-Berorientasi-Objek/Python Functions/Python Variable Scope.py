def greet():

    # variabel lokal
    message = 'Hello'
    
    print('Local', message)

greet()
# mencoba mengakses variabel message di luar fungsi greet()
# print(message)  # Di-comment agar tidak menghentikan eksekusi program (NameError)

# deklarasi variabel global
message = 'Hello'

def greet():
    # deklarasi variabel lokal
    print('Local', message)

greet()
print('Global', message)

# fungsi luar 
def outer():
    message = 'local'

    # fungsi dalam (nested function)  
    def inner():

        # deklarasi variabel nonlocal
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()