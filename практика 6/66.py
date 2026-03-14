class Product:
    
    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

    def display_info(self):
        
        print(f"Название: {self.name}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Цена: {self.price} руб.")

    def matches(self, **criteria):
       
        if 'name' in criteria and self.name.lower() != criteria['name'].lower():
            return False
        if 'price' in criteria and self.price != criteria['price']:
            return False
        
        return True

    def __str__(self):
        return f"{self.name} ({self.manufacturer}) - {self.price} руб."


class Electronics(Product):
    
    def __init__(self, name, manufacturer, price, device_type):
        super().__init__(name, manufacturer, price)
        self.device_type = device_type

    def display_info(self):
        super().display_info()
        print(f"Тип устройства: {self.device_type}")
        print()

    def __str__(self):
        return super().__str__() + f", тип: {self.device_type}"


class Clothing(Product):
    
    def __init__(self, name, manufacturer, price, size):
        super().__init__(name, manufacturer, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Размер: {self.size}")
        print()

    def __str__(self):
        return super().__str__() + f", размер: {self.size}"


class Food(Product):
    
    def __init__(self, name, manufacturer, price, expiration_date):
        super().__init__(name, manufacturer, price)
        self.expiration_date = expiration_date

    def display_info(self):
        super().display_info()
        print(f"Срок годности: {self.expiration_date}")
        print()

    def __str__(self):
        return super().__str__() + f", годен до: {self.expiration_date}"



products = [
    Electronics("Смартфон", "Samsung", 50000, "Телефон"),
    Electronics("Ноутбук", "HP", 75000, "Ноутбук"),
    Clothing("Футболка", "Nike", 2500, "L"),
    Clothing("Джинсы", "Levi's", 6000, "32"),
    Food("Молоко", "Простоквашино", 80, "15.05.2026"),
    Food("Хлеб", "Хлебозавод №1", 45, "25.02.2026")
]


print("=== Вся информация о товарах ===")
for product in products:
    product.display_info()


def search_products(products, **criteria):
    """Возвращает список товаров, соответствующих критериям"""
    result = []
    for p in products:
        if p.matches(**criteria):
            result.append(p)
    return result


print("\n=== Поиск товаров с названием 'Молоко' ===")
found = search_products(products, name="Молоко")
for p in found:
    print(p)


print("\n=== Поиск товаров с ценой 2500 руб. ===")
found = search_products(products, price=2500)
for p in found:
    print(p)

print("\n=== Поиск товаров с названием 'Футболка' и ценой 2500 ===")
found = search_products(products, name="Футболка", price=2500)
for p in found:
    print(p)
