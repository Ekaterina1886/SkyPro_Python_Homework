from smartphone import Smartphone
catalog = [
    Smartphone ("Samsung", "A15", "+7 987 654-32-10"),
    Smartphone ("Xiaomi", "Note13", "+7 123 456-78-90"),
    Smartphone ("Apple", "iPhone 15 Pro Max", "+7 900 123-45-67"),
    Smartphone ("Samsung", "Galaxy S24 Ultra", "+7 911 234-56-78"),
    Smartphone ("OnePlus", "12R", "+7 944 567-89-01")
    ]
for smartphone in catalog:
    print (f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")