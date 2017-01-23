import re
import operator
from collections import defaultdict


# ------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be ---
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead", "could"]


def NextWordProbability(sampletext, word):
    words, dct = [], defaultdict(int)
    word = word.strip().lower()
    for i, w in enumerate(sampletext.split(' ')):
        match = re.search('\w+', w)
        if match:
            words.append(match.group().lower())

    start = 0
    while 1:
        try:
            loc = words[start:].index(word)
            start += loc + 1
            dct[words[start]] += 1
        except (IndexError, ValueError) as e:
            break

    return dct


def find_most_common(dct):
    if len(dct):
        max_value = max(dct.iteritems(), key=operator.itemgetter(1))[1]
        words = []
        for k, v in dct.items():
            if v == max_value:
                words.append(k)
        return words[0]

    return ''


def LaterWords(sample, word, distance):
    '''
    @param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    occurences = NextWordProbability(sample, word)
    occurences_level2 = defaultdict(int)

    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.

    if distance == 2:
        for w in occurences:
            dct = NextWordProbability(sample, w)
            for w2 in dct:
                occurences_level2[w2] = occurences[w] + dct[w2]
        return find_most_common(occurences_level2)

    return find_most_common(occurences)


if __name__ == '__main__':
    print LaterWords(sample_memo, "ahh", 2)
    # print LaterWords(sample_memo, "catch", 1)
    # print LaterWords(sample_memo, "catch", 2)
