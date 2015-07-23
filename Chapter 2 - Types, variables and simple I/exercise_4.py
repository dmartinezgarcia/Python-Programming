# Exercise 4
#
# Write a Car Salesman program where the user enters the base price of a car. The program should add on a bunch of
# extra fees such as tax, license, dealer prep and destination charge. Make tax and license a percent of the base
# price. The other fees should be set values. Display the actual price of the car once all the extras are applied.
#

price_car = float(input("Please enter the base price of the car: "))
price_license = price_car * 0.15
price_tax = price_car * 0.20
price_dealer = 20.0
price_dest = 50.0
price_total = price_car + price_license + price_tax + price_dealer + price_dest

print("\t\t\t Car: " + str(price_car))
print("\t\t\t Tax: " + str(price_tax))
print("\t\t\t License: " + str(price_license))
print("\t\t\t Dealer prep: " + str(price_dealer))
print("\t\t\t Destination charge: " + str(price_dest))
print("\t\t\t TOTAL: " + str(price_total))