import random

url = "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/";

print -3, url.split('/')[-3]
print -2, url.split('/')[-2]
print -1, url.split('/')[-1]

x = '!@#$SDFGRY#$%@TGZDFGDFSG@#$%TASFHY#$%^'
print x.count("$%@")


# Random element from array
y = ['you like the piano girl', 'you want to fuck ling', 'you dislike Rachael', 'you like riding', 'you hate being stupid']
random_key = random.randint(1, 5)
print random_key
values = [w.capitalize() for w in random.sample(y, random_key)]
print values
