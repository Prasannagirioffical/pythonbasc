class House:
    window=10
    door=10
    color="red"
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color 
    
ram_ghar = House()
hari_ghar = House()

# ram_ghar.color = "black"
# hari_ghar.window =20
# print(ram_ghar.color)
ram_ghar.set_color("green")
print(ram_ghar.get_color())



