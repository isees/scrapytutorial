class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject
        self.verb = verb
        self.obj = obj


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')


def parse_object(word_list):
    skip(word_list, 'stop')
    while word_list != []:
        next_word = peek(word_list)
        if next_word == "noun" or next_word == "direction":
            return match(word_list, next_word)
        word_list.pop(0)
    raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return match('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj, verb, obj)


# word_list = [('direction', 'north'), ('verb', 'run')]
# x = parse_sentence(word_list)
# print x.subject
# print x.verb
# print x.obj

word_list = [
    ("noun", "cat"),
    ("verb", "eat"),
    ("stop", "end"),
    ('noun', 'shit')
]

x = parse_sentence(word_list)
print 'subject', x.subject
print 'verb', x.verb
print 'obj', x.obj
