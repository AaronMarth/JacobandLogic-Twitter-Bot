import random

lyrics = [
"I don't wanna be alive, I don't wanna be alive\nI just wanna die today, I just wanna die\nI don't wanna be alive, I don't wanna be alive\nI just wanna die\nAnd let me tell you why",
"Kinda like John Wick, bars like a convict\nFuck around and you don't wanna start shit, woo!\nComin' with the hot shit, all they do is talk shit\nYou could never top it, boy, just stop, stop it",
"Son, you know why you the greatest alive?\nWhy, Dad?\nBecause you came out of my balls, nigga\nHahahahahaha\n(Roof!)",
"Now my phone blowin' up like ring\nLike ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring!\nThat Kevin Durant, I'm a champion\nCheck the numbers, I'm a champion",
"Work so fucking much, my greatest fear is I'ma die alone\nEvery diamond in my chain, yeah, that's a milestone (I'm lovin' it!)\nPeople calling me, askin' me for money, man (Uh)\nThe only thing I'ma give you motherfuckers is the dial tone (Yeah)",
"I'm the man of the year, man of the year\nMan of the year, man of the year\nMan of the year, man of the year",
"It's just me, Castro and 6ix, going crazy in this bitch\nPlus my homie Jon, and the whole RattPack, you know we on",
"Fuck a nine to five, I'm too alive for the real world\nNever die in the real world, lie in the real world\nEverything ain't what it seems\nWhen you following your dream",
"Yeah, smoking in London while the snow fall\nIn another country, so pardon me for the roll call\nDamn, who would've thought the fan base was this immense?",
"This a marathon, not a sprint\nSwitch up the plan like homie that went from Verizon to Sprint\nCan you hear me now? Does anybody out there feel me now?",
"They said I couldn't do it\nBack when I was broke going through it\n'Til I got a deal, now they talking 'bout \"I knew it\"",
"I hope you live a long life hatin'\nNow watch every Grammy just to see who they nominating, uh\nSo successful they probably say I signed with Satan\nBut I got God on my side, always down to ride"
]


def randomNumber():
    randNUM = random.randint(0,12)
    return(randomLyric(randNUM))

def randomLyric(randNUM):
    return(lyrics[randNUM])

randomNumber()
