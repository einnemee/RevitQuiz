print ('Revit Quiz Game')

playing = input('Do you want to play? ')

if playing != 'yes':
    quit()

print ('Ok, let\'s play')

answer1 = input('What does BIM stand for? ')
if answer1 == 'building information modelling':
    print ('Correct')
else: 
    print ('Incorrect')
