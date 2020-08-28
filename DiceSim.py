#This is a dice simulator

import random


print('This is a dice simulator.')
x = ''

while x != 'q':                 #infinite loop: q for quit
    x = random.randint(1, 6)    #random number for die
    if x == 1:                  #draw die representing number
        print('''
{     }
{  o  }
{     }
You rolled a 1!
''')
    if x == 2:
        print('''
{o    }
{     }
{    o}
You rolled a 2!
''')
    if x == 3:
        print('''
{o    }
{  o  }
{    o}
You rolled a 3!
''')
    if x == 4:
        print('''
{o   o}
{     }
{o   o}
You rolled a 4!
''')
    if x == 5:
        print('''
{o   o}
{  o  }
{o   o}
You rolled a 5!
''')
    if x == 6:
        print('''
{o   o}
{o   o}
{o   o}
You rolled a 6!
''')
    x = input('\nEnter q to quit or enter another key to reroll: ')
    
