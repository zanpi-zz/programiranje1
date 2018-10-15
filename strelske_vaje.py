import math
#hitrost in kot
speed = int(input("Vpiši hitrost "))
angle_degree = int(input("Vpiši kot "))

#pretvori stopinje v RD
angle_rd = angle_degree*0.0174533
#g pospešek
g = 9.80665

print("Razdalja, ki jo prepotuje krogla " + str((speed**2* (math.sin(2*angle_rd)))/g) + " m")

