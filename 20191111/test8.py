import time
words = input('Please input the words you want to say!:')
for item in words.split():
    letterslist = []
    for y in range(12,-12,-1):
        list_X = []
        letters = ''
        for x in range(-30,30):
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += item[(x-y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterslist += list_X
    print('\n'.join(letterslist))
    time.sleep(1.5);