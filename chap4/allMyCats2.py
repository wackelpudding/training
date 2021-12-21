catNames = []
while True:
    print('Enter the nane of cat ' + str(len(catNames) +1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for cat in catNames:
    print(' ' + cat)