class Car:
    model = "model"
    year = "0000"
    maker = "maker"
    power = "000 л.с."
    color = "color"
    price = "0000000000"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.maker}\n"
              f"Мощьность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, mark, year, maker, power, color, price):
        self.model = mark
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

h1 = Car()
h1.print_info()
h1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
h1.print_info()