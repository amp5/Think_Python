# Question # 3
str_now = input("what time is it now (Military time)?")
now = int(str_now)

str_alarm = input("When do you want your alarm (in hours)?")
alarm = int(str_alarm)

non_converted_time_at_alarm = now + alarm
print non_converted_time_at_alarm

days_time_at_alarm = non_converted_time_at_alarm // 24
print days_time_at_alarm

extra_hours_time_at_alarm = non_converted_time_at_alarm % 24
print extra_hours_time_at_alarm

time_at_alarm = extra_hours_time_at_alarm
print"Your alarm will go off at %d." % time_at_alarm

print "................"

# Question 4 - DIDNT GET THIS ONE QUITE RIGHT
#str_start = input("When do you leave? Please enter a number value (Sunday = 0, Saturday = 1)")
#start = int(str_start)

#str_length = input ("How long do you plan on staying?")
#length = int(str_length)

#nonconverted_return_date = start + length
#return_date = nonconverted_return_date / 6

#print return_date

print "................"

# Question 5
a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
i = "dull"
j = "boy."

print a, b, c, d, e, f, g, h, i, j

print "................"

# Question 7

str_years = input("Number of years?")
years = int(str_years)
#print (type(years))
#print years

t = years
#print t
#print(type(t))
p = 10000
r = .08
n = 12

compound_interest = p * ((1 + (r / n)) ** (n * t))
print compound_interest

# Question 8
#a = pi r squared

pi = 3.14159
str_r = input ("What is the radius?")
r = int(str_r)

area = pi * (r ** 2)
print ("Thanks! The area of this circle will be %d.") % area

# Question 9
# a = w * h

str_w = input("What is the width?")
w = int(str_w)

str_h = input("What is the height?")
h = int(str_h)

area = w * h
print ("The area is %d.") % area
