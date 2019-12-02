from modules import MODULES

individual = []

def calc_fuel(mass):
    return (int(int(mass)/3))-2

def Reducer(mass):
    iterations = []
    fuel = calc_fuel(mass)
    while fuel > 0:
        iterations.append(fuel)
        fuel = calc_fuel(fuel)
    return sum(iterations)

if __name__ == "__main__":
    TOTAL = 0
    for m in MODULES:
        individual.append(Reducer(m))
    
    print(sum(individual))
