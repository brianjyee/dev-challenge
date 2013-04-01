# Exercises for chapter 3:

# Name: Brian Yee

# 3.1
# NameError: name 'repeat_lyrics' is not defined
repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# 3.2
# Works fine because both functions have been defined. Prints the following:
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
repeat_lyrics()
    
# 3.3
def right_justify(s):
    print ' ' * (70 - len(s)) + s

# 3.4
def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print 'spam'

def print_twice(s):
    print s
    print s

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

# prints 'spam' once
#print_spam()

# prints 'spam' twice
#print_twice('spam')

# prints 'spam' four times
#do_twice(print_twice, 'spam')

# prints 'spam' eight times
#do_four(print_twice,'spam')
