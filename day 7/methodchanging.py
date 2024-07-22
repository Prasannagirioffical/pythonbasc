# class burger:
#         def bun(self):
#             print("bun")
#             return self
#         def patty(self):
#             print("patty")
#             return self
#         def tomato(self):
#             print("tomato")
#             return self
    
# burger = Burger()
    
# burger.bun().patty().tomato().bun()
class pizza:
    
    def base(self):
        print("base")
        return(self)
    
    def sauce(self):
        print("sauce")
        return(self)
    
    def meat(self):
        print("meat")
        return(self)

pizza = pizza()
pizza.base().sauce().meat().base()
    
    
    