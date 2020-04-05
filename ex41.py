import random
from urllib import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES  = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef__init__(self, ***)": "class %%% has-a __init__that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": "Set *** to an instance of class %%%",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."    
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FISTS = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip()) # .strip() returns a copy of the string with both leading and trailing characters removed or by removing everything in the parenthesis
    
def convert(snippet, phrase):
    classNames = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    otherNames = random.sample(WORDS, snippet.count("***"))
    results =[]
    paramNames = []

    for i in range (0, snippet.count("@@@")):
        paramCount = random.randint(1, 3)
        paramNames.append(', '.join(random.sample(WORDS, paramCount)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in classNames:
            result = result.replace("%%%", word, 1) # .replace(old, new, howManyTimes)
        
        # fake other names
        for word in otherNames:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in paramNames:
            result = result.replace("@@@", word, 1)
        
        results.append(result)

    return results

# keep going until they hit CTRL-D

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, anwser = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, anwser = anwser, question
            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" %anwser
except EOFError:
    print "\nBye"