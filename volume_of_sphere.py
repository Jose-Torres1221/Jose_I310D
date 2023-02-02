#Function to calculate volume of sphere
def calculate_volume_of_sphere(radius):
    PI = 3.14
    volume = (4/3) * PI * (radius)**2
    return volume

#Calculate volume of spheres radii 30, 40

volume = calculate_volume_of_sphere(30)
print(volume)
volume = calculate_volume_of_sphere(40)
print(volume)