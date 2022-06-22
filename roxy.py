hero = "Super Man"
hero =hero.split(' ') #['Super' , 'Man']
hero = list(map('!'.join, hero))
print(hero)
