from classes import Technology, Phone, Laptop


def main():
    tech1 = Technology("Cool Tech", 100, "Black Holes")
    phone1 = Phone("iPhone 1337", 1200, "Mobile devices and Hoverboard", 2030, "Black-black")
    laptop1 = Laptop("For study laptop", 1500, "Computers", 64, "Intel i9 99900")

    technologies = [tech1, phone1, laptop1]

    for item in technologies:
        print(item)  
        print("Name:", item.say_name())
        print("Price:", item.show_price())
        print("Field:", item.say_field())
        print("Capabilities:", item.capabilities())  
        print()

    print(phone1.tell_year())
    print(phone1.tell_color())
    print(laptop1.tell_ram())
    print(laptop1.tell_processor())


if __name__ == "__main__":
    main()