"""
Created on Mon Jun 18 23:21:10 2018

@author: WeiJin
"""


# Intro our tool to the user
print "Welcome! You're now a governer in the economy."
print ""
print "The economy is located near a lake and water is a crucial part of production. But if more water is used, water will be less efficient as a factor. Now, you get to decide the allocation of water to three different firms. Their efficiency of using water differs a lot."
print ""
print "The first coordinate of the following choices means the unit of water you give to the first firm, which is the firm with highest efficiency of using water."
print ""
print "Similarly, the second coordinate is the unit of water you give to the second firm, which is the firm with the second highest efficiency of using water."
print ""
print "Finally, the third coordiante of the choices means the unit of water you give to the last firm, who connot produce anything out of water."
print ""
print ""
print "There are four possible allocations of the last factor to the three firms:"
print ""
print "Option A: [Firm 1: 1; Firm 2: 1; Firm 3: 28]"
print ""
print "Option B: [Firm 1: 28; Firm 2: 1; Firm 3: 1]"
print ""
print "Option C: [Firm 1: 15; Firm 2: 10; Firm 3: 5]"
print ""
print "Option D: [Firm 1: 20; Firm 2: 7; Firm 3: 3]"
print ""
choice = raw_input("Please enter your choice (A/B/C/D):")
print ""

# Reveal user's choice
if choice == "A" or choice == "a":
    print "You have chosen to allocate:"
    print "1 unit to firm 1"
    print "1 unit to firm 2"
    print "28 units to firm 3"
    print ""
    print "You have chosen the worst allocation."
elif choice == "B" or choice == "b":
    print "You have chosen to allocate:"
    print "28 units to firm 1"
    print "1 unit to firm 2"
    print "1 unit to firm 3"
    print ""
    print "You have chosen the second best allocation!"
elif choice == "C" or choice == "c":
    print "You have chosen to allocate:"
    print "15 units to firm 1"
    print "10 units to firm 2"
    print "5 units to firm 3"
    print ""
    print "You have chosen the second worst allocation."
elif choice == "D" or choice == "d":
    print "You have chosen to allocate:"
    print "20 units to firm 1"
    print "7 units to firm 2"
    print "3 units to firm 3"
    print ""
    print "You have chosen the best allocation!"
else:
    print "Invalid input. Please input either A/B/C/D"

# Explanation of the different allocations
print ""
    

