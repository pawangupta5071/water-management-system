# Water Management System

apartment = int(input('Apartment-Type 2BHK or 3BHK:\n'))
if apartment == 2:
    people = 3
elif apartment == 3:
    people = 5
else:
    print(" Please choose between 2 or 3 ")

ratio = input('Ratio between Corporation water and Borewell water :\n')
s = ratio.split(":")

corp_water = s[0]
borewell_water = s[1]

total_altd_water = int(corp_water) + int(borewell_water)

alloted_water = people*10*30

corp_water_cost = alloted_water*int(corp_water)
corp_water_cost = int(corp_water_cost)//int(total_altd_water)


borewell_water_cost = int(alloted_water)*int(borewell_water)
borewell_water_cost = int(borewell_water_cost)//int(total_altd_water)
borewell_water_cost = borewell_water_cost*1.5

total_altd_water_cost = corp_water_cost + borewell_water_cost

no_of_guests = 0
while(True):
    Add_guests = int(input('Add Guests/or Enter 0 for Bill:\n'))
    if (Add_guests != 0):
        no_of_guests += int(Add_guests)

    else:
        break

guest_consumed_water = no_of_guests*10*30
if (guest_consumed_water > 0 and guest_consumed_water < 500):
    guest_cost = guest_consumed_water*2

elif (guest_consumed_water > 500 and guest_consumed_water <= 1500):
    guest_cost = (500*2)+(guest_consumed_water - 500)*3

elif (guest_consumed_water > 1500 and guest_consumed_water <= 3000):
    guest_cost = (500*2)+(1500-500)*3+(guest_consumed_water - 1500)*5

elif (guest_consumed_water > 3000):
    guest_cost = (500*2)+(1500-500)*3+(3000 - 1000) * \
        5+(guest_consumed_water - 3000)*8

else:
    guest_cost = 0

print('')
waterconsumed = alloted_water + (no_of_guests*10*30)
Total_cost = guest_cost + total_altd_water_cost
Total_cost = int(Total_cost)
print(f" total water consumed is {waterconsumed} ltr and total cost is {Total_cost}")