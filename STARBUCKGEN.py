import random

starlist = ('1','2','3','4','5','6','7','8','9','0')
codetemp = ('6171 6512 85','6171 8342 16')
starbuckscodes = open('starbucks codes' + ' ' + '.txt' , 'a')
amcodes = input("How many codes you want to generate: ")
if  amcodes.isnumeric():
    for i in range(int(amcodes)):
      starbuckscodes.write(
        random.choice(codetemp) + random.choice(starlist) + random.choice(starlist) + " " + random.choice(starlist) + random.choice(starlist) + random.choice(starlist) + random.choice(starlist) + '\n')
else:
    print('Numbers please. ')
    exit()
starbuckscodes.close()
