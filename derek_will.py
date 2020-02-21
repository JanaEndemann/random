from numpy.random import randint

what = ['play basketball', 
        'teach yoga',
        'travel',
        'start a new company',
        'dance like a primo ballerino',
        'take up a new study',
        'do absolutely nothing',
        'live off the grid',
        'win twitter',
        'sail a ship',
        'ride his bycicle',
        'write code',
        'snowboard down the highest mountain',
        'make an algorithm make him rich',
        'make a game']

how = ['in Utrecht',
        'in Japan',
        'in India',
        'in the middle of nowhere',
        'with all his friends',
        'all alone',
        'across the ocean',
        'with his family',
        'with his girlfriend',
        'from his bedroom',
        'while pondering the meaning of life']

why = ['simply because he can',
      'to be the best',
      'to save the world',
      'to help out his friends',
      'for no reason at all',
      "because he's bored",
      "because he hasn't tried it yet",
      ', but not be an ass about it',
      'to win a bet',
      'to make his friends jealous',
      "because it's a Monday",
      "because no one else is doing it",
      "because it's fun",
      "to learn from it",
      "because his 5th grade teacher told him to"]

def make_sentence():
    sentence = 'Derek will '
    for l in [what, how, why]:
        sentence += l[randint(0, len(l))]
        sentence +=' '
    sentence = sentence[:-1]
    sentence = sentence.replace(' ,', ',')
    return sentence + '.'

if __name__ == '__main__':
	print(make_sentence())
