c = 1 # variabel global
def add():
    print(c)

add()# Output: 1

# variabel global
c = 1 
def add():

     # menambahkan c dengan 2
    # c = c + 2  # Di-comment agar tidak menyebabkan UnboundLocalError

    print(c)

add()

# variabel global
c = 1 
def add():

    # penggunaan kata kunci global
    global c

    # menambahkan c dengan 2
    c = c + 2 

    print(c)

add()# Output: 3