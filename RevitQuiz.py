print ('Revit Quiz Game')

playing = input('Do you want to play? ').upper()

if playing != 'YES':
    quit()

print ('Ok, let\'s play')

answer1 = input('What does BIM stand for? ').upper()
if answer1 == 'BUILDING INFORMATION MODELLING' or 'BUILDING INFORMATION MODELING':
    print ('Correct')
else: 
    print ('Incorrect')

answer1 = input('Is BIM only available in AutoDesk Revit? Yes/No ').upper()
if answer1 == 'NO':
    print ('Correct')
else: 
    print ('Incorrect')
