# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template

#def greet(name = 'Ingrid', greeting_template = 'Hello,'):
#    print(greeting_template, name)
from inspect import formatargvalues


def greet(name, greeting_template = 'Hello, <name>!'):
    greet = greeting_template.replace('<name>', name)
    print(greet)
    return greet
#greet('Winc Academy!', 'Goedemorgen,')  
greet('Feline', 'Hello, <name>!')
#greet('Wincpy')

# Part 2: Force
# force  = mass  x gravity
# kracht = massa x zwaartekracht (gewicht van de appel 0,1 kg x 9,8N = 0,98 N bijn 1 newton)

def force(mass, body = "earth"):
#bodies = {"name_body" : "sun", "gravity" : 9.8}
    celestial_bodies = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6
}
    return mass * celestial_bodies[body]
    
# Part 3: Gravity

def pull(m1, m2, d):
    g = (6.674 * (10 ** -11)) # 6.67408e-08 
    gravitional_pull = (g * ((m1*m2) / d**2))  # machtsverheffen = d ** 2

    #m1 = float(object_mass_in_kg)          #example > car1 800kg
    #m2 = float(another_object_mass_in_kg)  #example > car2 1500kg
    #d = float(distance_in_meters)          #example > 3m
    #g = 6.67408e-08 ((6.67428 * 10) ** -11) m2/kg2

    return (gravitional_pull)

round(pull(800, 1500, 3), 10)
print(round(pull(800, 1500, 3), 10))

#print(pull())