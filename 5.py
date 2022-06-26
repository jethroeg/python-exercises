# create a while loop that functions the same as this for loop 

#furniture = ['table', 'chair', 'desk', 'lamp', 'couch']

#for item in furniture:
#    print(f'YOU WILL NOT BE ABLE TO FIND A {item.upper()} CHEAPER THAN OUR PRICES AT FURNITURE MART!')
# this formatted string is the same as print('YOU WILL NOT BE ABLE TO FIND A ' + item.upper() + ' CHEAPER THAN OUR PRICES AT FURNITURE MART!')
furniture = ['table', 'chair', 'desk', 'lamp', 'couch']
i = 0

while i < len(furniture):
    print(f'YOU WILL NOT BE ABLE TO FIND A {furniture[i].upper()} CHEAPER THAN OUR PRICES AT FURNITURE MART!')
    i += 1
