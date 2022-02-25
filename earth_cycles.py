import math

x = math.factorial(52)
print(x)
total_time = x

circumference_of_earth = 4075 *10**6
thickness_of_paper = 0.1 *10**-3
length_one_step = 2.8
time_one_step = 100000000*365.25*24*60*60
distance_earth_to_sun = 149597870*10**3
volume_pacific = 710000000 *10**9
volume_drop = 0.05 *10**-9

print(circumference_of_earth)
print(thickness_of_paper)
print(length_one_step)
print(time_one_step)
print(distance_earth_to_sun)

drops = volume_pacific/volume_drop
print(drops)

sheets = distance_earth_to_sun/thickness_of_paper
print(sheets)

time_one_earth = circumference_of_earth/(length_one_step/time_one_step)
print(time_one_earth)

rounds = sheets*drops
time_to_sun = rounds*time_one_earth
print(time_to_sun)

remaining_time = x - time_to_sun
print(remaining_time)