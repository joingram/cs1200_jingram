"""
These are some helper functions for our funny chatbot
"""

import random

class BotHelper():
    
    # keep track of what has been said so far
    utterances = []

    # some utterances the bot knows how to say
    questions = [
        'Wanna hear a joke? I have so many.',
        'Want to hear another joke?',
        'I have another one for you {name}',
        'I can see you rolling on the floor laughing over there',
        'Buahahahaha, so funny. Do you want more?',
        'Next one is really good one, want to hear it?',
        'I have another, really funny one.'
        ]

    @staticmethod
    def parse_jokes(file_obj):
        """Parses funny text"""
        try:
            return [x.strip().split('|') for x in file_obj.readlines()]
        except:
            print("Provided file object is invalid")

    @staticmethod
    def tell_joke(jokes): 
        resp = None
        """Chooses and tells 1 random joke"""
        for line in jokes[random.randint(0, len(jokes) - 1)]:
            print('Yup') if resp is not None and \
                resp == line.lower().replace('.','') else print('\n' + line)
            resp = input("").strip().lower().replace('.','')

    @staticmethod
    def want_a_joke(name = ''):
        """Chooses random way to ask user if they want to hear a joke"""
        q = None

        if len(BotHelper.utterances) == len(BotHelper.questions):
            BotHelper.utterances = []
        if len(BotHelper.utterances) == 0:
            q = BotHelper.questions[0]
        else:
            tmp = list(set(BotHelper.questions) - set(BotHelper.utterances))
            q = tmp[random.randint(0, len(tmp) - 1)]
        BotHelper.utterances.append(q)
        return "\n{0}\n".format(q.replace('{name}', name).strip())
