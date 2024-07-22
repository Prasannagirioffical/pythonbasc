def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper
@star
def bye():
    print("bye")
    
@star
def guys():
    print("guys")

bye()
guys()

