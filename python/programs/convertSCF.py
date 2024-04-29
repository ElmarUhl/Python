# Convert units
# Elmar Uhl - 2024
# em desenvolvimento

def angstron2au(value):
    angstron = value
    au = angstron/1.8897259886
    return au

def au2angstron(value):
    au = value
    angstron = au*1.8897259886
    return angstron

def cal2j(value):
    j = 4.1868*value
    return j

def j2hatree(value):
    hartree = 2.2937123E+17*value
    return hartree
    
    

# Convert angstron to unit
angstron = float(input('Type the value in angstron: '))
au = angstron2au(angstron)
print(f'The value in au is {au}')

cal = float(input('Type in value of energy in cals: '))
j = cal2j(cal)
print(f'The value of energy is {j} j')

j = float(input('Type in value of energy in joules: '))
hartree = j2hatree(j)
print(f'The value of energy in hartree is {hartree}')

