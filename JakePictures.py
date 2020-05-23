import random

picture = [
"C:\\Users\\Aaron Marth\\Desktop\\Code\\jake.jpg",
"C:\\Users\\Aaron Marth\\Desktop\\Code\\jakeandheadset.jpg"
]

def randomNumber():
    randNUM = random.randint(0,1)
    return(randomPicture(randNUM))

def randomPicture(randNUM):
    return(picture[randNUM])

randomNumber()
