# debugging

from random import randint
dice_img = ['1','2','3','4','5']
dice_num = randint(6,6) #always produce error
dice_num = randint(0,5) #not gives error
print(dice_img[dice_num])


