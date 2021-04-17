from pprint import pprint
import random
import nltk

knowledge = {("person1", "name", "?"),
             ("person1", "town", "?"),
             ("person1", "street", "?")}

active = True
while active:
    unknowns = {(person, fact, value) for (person, fact, value)
                in knowledge if value == "?"}
    print("UNKNOWN:")
    pprint(unknowns)
    print("KNOWN:")
    pprint(knowledge - unknowns)
    if unknowns:  # is non-empty
        (person, fact, value) = random.choice(list(unknowns))
        question = "What is your" + " " + fact + "?"
        reply = input(question)
        tagged_reply = nltk.pos_tag(nltk.word_tokenize(reply))
        new_reply = ''
        for i, j in tagged_reply:
            if j == 'NNP':
                new_reply = i
        knowledge.remove((person, fact, value))
        knowledge.add((person, fact, new_reply))
        print(knowledge)
        # to fill in - process reply
    else:
        question = "How can I help you? "
        helpRequest = input(question)
        tagged_request = nltk.pos_tag(nltk.word_tokenize(helpRequest))
        verbs = []
        # to fill in - process reply
    print()
