def calculate_potential_energy(height, weight):
    gravity = 9.81
    potential_energy = weight * height * gravity
    return potential_energy

height_1 = float(input("Enter height of drop in meters: "))
weight_1 = float(input("Enter weight of skier in kg: "))


potential_energy = calculate_potential_energy(height_1, weight_1)

print("The potential energy is ", potential_energy, "in joules")

height_2 = float(input("Enter height of drop in meters: "))
weight_2 = float(input("Enter weight of elephant in kg: "))

potential_energy = calculate_potential_energy(height_2, weight_2)

print("The potential energy is ", potential_energy, "in joules")

height_3 = float(input("Enter height of drop in meters: "))
weight_3 = float(input("Enter weight of Jerry in kg: "))

potential_energy = calculate_potential_energy(height_3, weight_3)

print("The potential energy is ", potential_energy, "in joules")



