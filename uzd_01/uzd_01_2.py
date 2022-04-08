# Izveidot programmu, kura prasa lietot�jam ievad�t cilindra r�diusu un t� 
# augstumu, tiek apr��in�ts cilindra laukums un
#  tilpums. Rezult�ts tiek par�d�ts konsol�.
# tilpums = 3.14 * r�diuss * r�diuss * augstums
# laukums = 2 * (3.14 * r�diuss * r�diuss) + augstums * (2 * 3.14 * r�diuss)
# PI=-3.14

import math
h=int(input("ievadi augstumu:"))
r=int(input("ievadi rādiusu:"))

tilpums=math.pi*r*r*h
laukums=2*(math.pi*r*r)+h*(2*math.pi*r)
print(f"tilpums ir{tilpums}.")
print(f"tilpums ir{tilpums}.")