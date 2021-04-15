num_bars = 18 #Total number of bars
breakinto  = 7 #Number of square that can be broken into
people = 5

# Calculations
SPP  = num_bars // people * breakinto# Squares per person
leftOver = num_bars * breakinto - SPP * people
extra_pp = leftOver // people # Extra squares per person
leftOver -= extra_pp
print("Each of the {} people get {} squares ({} bars) plus an extra {} of remaining chocolate with a total of {} left over.".format(people, SPP, SPP / breakinto, extra_pp, leftOver))
