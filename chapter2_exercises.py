# Exercises for chapter 2:

# Name: Brian Yee

# 2.1
# Python thinks this variable with a leading zero is an octal instead of an integer

# 2.2
print 5
print x = 5
print x + 1

# 2.3
width = 17
height = 12.0
delimiter = '.'
# 1. 8 int
print width / 2
# 2. 8.5 float
print width / 2.0
# 3. 4.0 float
print height / 3
# 4. 11 int
print 1 + 2 * 5
# 5. '.....' str
print delimiter * 5

# 2.4
# 1. 523.6
print (4.0 / 3.0) * 3.14159 * (5 ** 3)
# 2. $945.45
print ((24.95 * .6) * 60) + 3 + (.75 * 59)
# 3. 7:30:06 am
minute = 60
hour = minute * 60
startTime = (6 * hour) + (52 * minute)
easy = (8 * minute) + 15
tempo = (7 * minute) + 12
runTime = (2 * easy) + (3 * tempo)
finishTime = startTime + runTime
finishHour = finishTime / 60 / 60
finishMinute = (finishTime / 60) % 60
finishSecond = (finishTime % 60) % 60
print str(finishHour) + ':' + str(finishMinute) + ':' + str(finishSecond)