import itertools

with open('01.txt') as f:
    items = map(lambda mass: int(str(mass).strip()), f.readlines())

def get_fuel(mass):
    return mass // 3 - 2

def fuel_requirements(mass):
    while mass > 0:
        fuel = get_fuel(mass)
        mass = fuel
        yield max(fuel, 0)

simple_total = sum(map(get_fuel, items))
full_total = sum(itertools.chain(*map(list, map(fuel_requirements, items))))
print(total, full_total)
