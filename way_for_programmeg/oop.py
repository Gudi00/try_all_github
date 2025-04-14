
# 1. Базовый класс (Суперкласс)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # Общая реализация для неопределенного животного
        print(f"{self.name} издает какой-то звук.")

# 2. Производный класс (Подкласс) - Собака
class Dog(Animal):
    # Переопределяем метод speak() из класса Animal
    def speak(self):
        print(f"{self.name} говорит: Гав!")

# 3. Еще один производный класс (Подкласс) - Кошка
class Cat(Animal):
    # Переопределяем метод speak() из класса Animal
    def speak(self):
        print(f"{self.name} говорит: Мяу!")

# 4. Еще один производный класс, который НЕ переопределяет speak
class Cow(Animal):
    # У коровы нет своего метода speak(), поэтому она будет использовать
    # метод из родительского класса Animal
    pass

# --- Демонстрация полиморфизма через переопределение ---

# Создаем объекты разных классов
my_dog = Dog("Рекс")
my_cat = Cat("Мурка")
generic_animal = Animal("Нечто")
my_cow = Cow("Буренка")

# Помещаем их в один список
animals = [my_dog, my_cat, generic_animal, my_cow]

print("--- Вызываем метод speak() для каждого животного ---")
# Используем полиморфизм: вызываем один и тот же метод speak()
# для объектов разных типов
for animal in animals:
    animal.speak() # Python сам определит, какую версию метода вызвать

print("\n--- Использование super() ---")

# Пример использования super() для вызова родительского метода
class LoudDog(Dog): # Наследуемся от Dog
    def speak(self):
        # Сначала вызываем оригинальный метод speak() из родительского класса (Dog)
        super().speak()
        # Затем добавляем свое поведение
        print("(очень громко!)")

loud_dog = LoudDog("Гром")
loud_dog.speak()