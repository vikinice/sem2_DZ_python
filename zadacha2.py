#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.



import fractions


def start():
    fract_1 = get_str("Введите первую дробь: ")
    fract_2 = get_str("Введите вторую дробь: ")
    print("Методы:")
    print(f"{fract_1} + {fract_2} = {fract_sum(fract_1, fract_2)}")
    print(f"{fract_1} * {fract_2} = {fract_milt(fract_1, fract_2)}")
    print("Проверка:")
    print(f"{fract_1} + {fract_2} = {fractions.Fraction(fract_1) + fractions.Fraction(fract_2)}")
    print(f"{fract_1} * {fract_2} = {fractions.Fraction(fract_1) * fractions.Fraction(fract_2)}")

def fract_sum(fract_1: str, fract_2: str) -> str:
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    fract_lcm = my_lcm(fract_1_part[1], fract_2_part[1])
    mult_1 = int(fract_lcm / fract_1_part[1])
    mult_2 = int(fract_lcm / fract_2_part[1])
    fract_1_part = [i * mult_1 for i in fract_1_part]
    fract_2_part = [i * mult_2 for i in fract_2_part]
    fract_1_part[0] += fract_2_part[0]
    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])

def split_fraction(fract: str) -> list:
    fraction_parts = fract.split("/")
    fraction_parts = [int(s) for s in fraction_parts]
    return fraction_parts

def fract_milt(fract_1: str, fract_2: str) -> str:
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    fract_1_part[0] *= fract_2_part[0]
    fract_1_part[1] *= fract_2_part[1]
    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])

def my_gcd(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    while num_2:
        num_1 %= num_2
        num_1, num_2 = num_2, num_1
    return int(num_1)

def my_lcm(num_1: int, num_2: int) -> int:
    return int(num_1 / my_gcd(num_1, num_2) * num_2)

def get_str(message: str = None) -> str:
    if message is None:
        message = "Введите строку: "
    return input(message)

if __name__ == "__main__":
    start()