
temp = 28
wearing_coat = False

if temp > 27 or (temp > 27 and wearing_coat) :
    print("I'm too hot!")


name = "Charmer"
age  = 30
arms = 1
wears_wig = True
married = False

eligible = (age >=5 and age <=100
            and (arms >=1 or arms<=2)
            and (age < 18 and arms == 2)
            and (age > 40 and married and wears_wig))


if eligible:
    print(name + " is eligible :)")
else:
    print(name + " is not eligiable:(")

