class Technology:
    def __init__ (self, name, price, field):
        self.name = name
        self.price = price
        self.field = field
    
    def show_price(self):
        return self.price
    
    def say_name(self):
        return self.name
    
    def say_field(self):
        return self.field
    
    def capabilities(self):
        return "I can do anything"
    def __str__(self):
        return f"Technology(name = {self.name}, price ={self.price}, field = {self.field})"
    
class Phone(Technology):
    def __init__(self, name, price, field, year, color):
        super().__init__(name, price, field)
        self.year = year
        self.color = color
    
    def tell_year(self):
        return f"I was made in {self.year}"
    
    def tell_color(self):
        return f"My color is {self.color}"

    def capabilities(self):
        return "I can call, take photos, browse the internet, and so on"

    #@Override
    def __str__(self):
        return (
            f"Phone(name = {self.name}, price = {self.price}, field = {self.field}, "
            f"year = {self.year}, color = {self.color})"
        )
    
class Laptop(Technology):
    def __init__(self, name, price, field, ram, processor):
        super().__init__(name, price, field)
        self.ram = ram
        self.processor = processor

    def tell_ram(self):
        return f"I have {self.ram} GB RAM"

    def tell_processor(self):
        return f"My processor is {self.processor}"

    def capabilities(self):
        return "I can code, run programs, study, and play games"

    def __str__(self):
        return (
            f"Laptop(name= {self.name}, price = {self.price}, field = {self.field}, "
            f"ram=  {self.ram}, processor = {self.processor})"
        )