import collections
from dataclasses import dataclass
import itertools
# import string

import numpy as np
from recordclass import RecordClass

# 1. Found 5 most usable letters in poem
with open('poem.txt', 'r', encoding='utf-8') as f:
    poem = f.read()

new_poem = [i for i in poem.lower() if i.isalpha()]

cnt = collections.Counter(new_poem)
for k, v in cnt.most_common(5):
    print(k, v)

# 2. Create list of cars using namedtuple
Car = collections.namedtuple('Car', [
    'manufacture',
    'model',
    'height',
    'width',
    'length',
    'engine_power',
    'acceleration',
    'fuel_con',
])

vw_golf = Car('Vw', 'Golf', 1452, 1799, 4255, 150, 8.6, 5.2)
vw_tiguan = Car('Vw', 'Tiguan', 1643, 1839, 4486, 240, 6.2, 7.5)
bmw_m5 = Car('Bmw', 'M5', 1479, 1868, 4936, 462, 4, 8.9)
bmw_x5 = Car('Bmw', 'X5', 1762, 1938, 4886, 381, 5.3, 7.6)
kia_stinger = Car('Kia', 'Stinger', 1400, 1870, 4830, 370, 5.4, 11)
reliant_robin = Car('Reliant', 'Robin', 1372, 1422, 3327, 40, 16, 3.3)

my_cars = [vw_golf, vw_tiguan, bmw_m5, bmw_x5, kia_stinger, reliant_robin]


# 3. Found and print three highest cars
def show_highest():
    def height(item: Car):
        return item.height

    my_cars.sort(key=height, reverse=True)

    for car in my_cars[:3]:
        print(car.manufacture + '-' + car.model)


# 3. Found and print three fastest cars
def show_fastest():
    def acceleration(item: Car):
        return item.acceleration

    my_cars.sort(key=acceleration)

    for car in my_cars[:3]:
        print(car.manufacture + '-' + car.model)


show_highest()
show_fastest()


# 4. Create list of cars using RecordClass
class RcCar(RecordClass):
    manufacturer: str
    model: str
    height: int
    width: int
    length: int
    engine_power: int
    acceleration: float
    fuel_con: float


rc_car = RcCar('Vw', 'Golf', 1452, 1799, 4255, 150, 8.6, 5.2)
rc_car1 = RcCar('Vw', 'Tiguan', 1643, 1839, 4486, 240, 6.2, 7.5)
rc_car2 = RcCar('Bmw', 'M5', 1479, 1868, 4936, 462, 4, 8.9)
rc_car3 = RcCar('Bmw', 'X5', 1762, 1938, 4886, 381, 5.3, 7.6)
rc_car4 = RcCar('Kia', 'Stinger', 1400, 1870, 4830, 370, 5.4, 11)
rc_car5 = RcCar('Reliant', 'Robin', 1372, 1422, 3327, 40, 16, 3.3)

my_rc_cars = [rc_car, rc_car1, rc_car2, rc_car3, rc_car4, rc_car5]


# 4. Improve engine power by 10% for 3 fastest cars
def improve_power():
    def acceleration(item: RcCar):
        return item.acceleration

    my_rc_cars.sort(key=acceleration)

    for car in my_rc_cars[:3]:
        percent = car.engine_power * 0.1
        car.engine_power += percent


# 5. Create list of cars using dataclass
@dataclass
class DcCar:
    manufacturer: str
    model: str
    height: int
    width: int
    length: int
    engine_power: int
    accel: float
    fuel_con: float


dc_car = DcCar(
    manufacturer='Vw',
    model='Golf', height=1452, width=1799, length=4255, engine_power=150, accel=8.6, fuel_con=5.2)
dc_car1 = DcCar(
    manufacturer='Vw',
    model='Tiguan', height=1643, width=1839, length=4486, engine_power=240, accel=6.2, fuel_con=7.5)
dc_car2 = DcCar(
    manufacturer='Bmw',
    model='M5', height=1479, width=1868, length=4936, engine_power=462, accel=8.6, fuel_con=8.9)
dc_car3 = DcCar(
    manufacturer='Bmw',
    model='X5', height=1762, width=1938, length=4886, engine_power=381, accel=8.6, fuel_con=7.6)
dc_car4 = DcCar(
    manufacturer='Kia',
    model='Stinger', height=1400, width=1870, length=4830, engine_power=370, accel=5.4, fuel_con=11)
dc_car5 = DcCar(
    manufacturer='Reliant',
    model='Robin', height=1372, width=1422, length=3327, engine_power=40, accel=16, fuel_con=3.3)

my_dc_cars = [dc_car, dc_car1, dc_car2, dc_car3, dc_car4, dc_car5]


# 5. Function for convert liters per 100 kilometers to miles per gallon(US)
def convert_lpk_mpg(lpk):
    constant = 235.215
    mpg = constant / lpk
    return round(mpg, 2)


def convert_all(list_of_cars):
    for car in list_of_cars:
        car.fuel_con = convert_lpk_mpg(car.fuel_con)


# 6. Print all combinations of 2 dice
tmp_list = list(itertools.product(range(1, 7), repeat=2))
print(tmp_list)


# 6. Print 3 most common sums
def make_sum(arg1, arg2):
    return arg1 + arg2


tmp_list = list(itertools.starmap(make_sum, tmp_list))
cnt = collections.Counter(tmp_list)
for k, v in cnt.most_common(3):
    print(k)

# 7. Change values from file iris.data
values = np.genfromtxt('iris.data', delimiter=',', usecols=[0, 1, 2, 3])
labels = np.genfromtxt('iris.data', delimiter=',', usecols=[4], dtype=str)
values = np.where(values >= 3, values, -values)
print(values)
