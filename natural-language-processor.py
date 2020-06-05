from nltk import RegexpParser
from nltk.tokenize import WhitespaceTokenizer
import nltk


# Finds relational phrases
def findOutside(tagged_phrase, appendee):
    i = 0
    while i < len(tagged_phrase):
        existing = ''
        while tagged_phrase[i][2] == 'O':
            if tagged_phrase[i][0] == 'and':
                appendee.append('and')
                i = i + 1
                continue
            if existing == '':
                existing = tagged_phrase[i][0]
            else:
                existing = existing + ' ' + tagged_phrase[i][0]
            i = i + 1
            if i == len(tagged_phrase):
                break
        if existing != '':
            appendee.append(existing)
        i = i + 1
    return


# Finds noun phrases (modified version of above function)
def findNounPhrase(tagged_phrase, appendee):
    i = 0
    while i < len(tagged_phrase):
        existing = ''
        while tagged_phrase[i][2] != 'O':
            if existing == '':
                existing = tagged_phrase[i][0]
            else:
                existing = existing + ' ' + tagged_phrase[i][0]
            i = i + 1
            if i >= len(tagged_phrase):
                break
        if existing != '':
            appendee.append(existing)
        i = i + 1
    return


def identifyNounClassifiers(nounClassifiers, taggedNounPhrase):
    i = 0
    classifiers = []
    noun = []
    while i < len(taggedNounPhrase):
        if taggedNounPhrase[i][1] == 'JJ':
            classifiers.append(taggedNounPhrase[i][0])
        if taggedNounPhrase[i][1] == 'NN':
            noun.append(taggedNounPhrase[i][0])
        i = i + 1
    nounClassifiers.append([noun, classifiers])
    return


def relatePhrase(phrase):
    # Part of speech tags:
    # DT = determiner; NN = noun; IN = preposition or subordinating conjunction; TO = to;

    prepositions = ['above', 'behind', 'below', 'front', 'back', 'left', 'right', 'against', 'at', 'beside', 'between',
                    'close', 'near', 'next', 'on', 'on top', 'over', 'vicinity']
    descriptor_prepositions = ['front', 'back', 'left', 'right', 'highest', 'lowest', 'farthest', 'rightmost',
                               'leftmost']
    leftRelations = ['leftmost', 'left']
    rightRelations = ['rightmost', 'right']
    topRelations = ['top', 'highest', 'topmost']
    bottomRelations = ['bottom', 'lowest', 'below', 'under']
    frontRelations = ['frontmost', 'closest', 'front', 'close']
    backRelations = ['backmost', 'furthest', 'farthest', 'back', 'far']
    masterRelations = ['leftmost', 'left', 'rightmost', 'right', 'top', 'highest', 'bottom', 'lowest', 'frontmost',
                       'closest', 'front', 'close', 'backmost', 'furthest', 'farthest', 'back', 'far', 'below', 'under',
                       'topmost']
    most = ['leftmost', 'rightmost', 'highest', 'lowest', 'furthest', 'farthest', 'closest']
    # Note to self later on: if there are unwanted triggers of the below ifs, it is probably because of these ^^
    # below, under
    phrase_array = WhitespaceTokenizer().tokenize(phrase)
    if "that's" in phrase_array:
        phrase_array.remove("that's")
    if "it's" in phrase_array:
        phrase_array.remove("it's")
    tagged_phrase = nltk.pos_tag(phrase_array)
    # Problematic phrases
    # to the right/left/back/front
    semantic = []
    original = ''
    objects = []
    relations = []
    remove = []
    originalflag = False
    for i in range(0, len(tagged_phrase)):
        if tagged_phrase[i][0] == 'sphere' or tagged_phrase[i][0] == 'cylinders' or tagged_phrase[i][0] == 'boxes' or \
                tagged_phrase[i][0] == 'pyramids':
            tagged_phrase[i] = (tagged_phrase[i][0], 'NN')
        if tagged_phrase[i][0] in masterRelations or tagged_phrase[i][0] == 'blue':
            tagged_phrase[i] = (tagged_phrase[i][0], 'JJ')
    i = 0
    print(tagged_phrase)
    while i < len(tagged_phrase):
        # in (the) front/back
        try:
            if tagged_phrase[i][0] in frontRelations or tagged_phrase[i][0] in backRelations:
                if tagged_phrase[i - 1][0] == 'in':
                    if i + 1 >= len(tagged_phrase):
                        if i - 3 >= 0:
                            if tagged_phrase[i - 3][1] == 'JJ' and tagged_phrase[i - 3][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s" in objects:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s ")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 2][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 2][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 2][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 2][0]
                            if tagged_phrase[i - 2][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 2][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 2][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                    elif tagged_phrase[i + 1][0] != 'of':
                        if i - 3 >= 0:
                            if tagged_phrase[i - 3][1] == 'JJ' and tagged_phrase[i - 3][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s" in objects:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s ")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 2][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 2][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 2][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 2][0]
                            if tagged_phrase[i - 2][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 2][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 2][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                elif tagged_phrase[i - 2][0] == 'in':
                    if i + 1 >= len(tagged_phrase):
                        if i - 4 >= 0:
                            if tagged_phrase[i - 4][1] == 'JJ' and tagged_phrase[i - 4][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                            else:
                                if tagged_phrase[i - 5][1] == 'JJ' and tagged_phrase[i - 5][0] not in masterRelations:
                                    if original == '':
                                        original = tagged_phrase[i - 5][0] + ' ' + tagged_phrase[i - 3][0]
                                    if tagged_phrase[i - 5][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                        objects.append(tagged_phrase[i - 5][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                    else:
                                        objects.append(tagged_phrase[i - 5][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                                else:
                                    if original == '':
                                        original = tagged_phrase[i - 3][0]
                                    if tagged_phrase[i - 3][0] + "s" not in objects:
                                        objects.append(tagged_phrase[i - 3][0] + "s")
                                    else:
                                        objects.append(tagged_phrase[i - 3][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 3][0]
                            if tagged_phrase[i - 3][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 3][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 3][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                        remove.append(i - 2)
                    elif tagged_phrase[i + 1][0] != 'of':
                        if i - 4 >= 0:
                            if tagged_phrase[i - 4][1] == 'JJ' and tagged_phrase[i - 4][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 3][0]
                            if tagged_phrase[i - 3][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 3][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 3][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                        remove.append(i - 2)
        except:
            pass
        # on (the) top/bottom/left/right
        try:
            if tagged_phrase[i][0] in masterRelations:
                if tagged_phrase[i - 1][0] == 'on':
                    if i + 1 >= len(tagged_phrase):
                        if i - 3 >= 0:
                            if tagged_phrase[i - 3][1] == 'JJ' and tagged_phrase[i - 3][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 2][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 2][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 2][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 2][0]
                            if tagged_phrase[i - 2][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 2][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 2][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                    elif tagged_phrase[i + 1][0] != 'of':
                        if i - 3 >= 0:
                            if tagged_phrase[i - 3][1] == 'JJ' and tagged_phrase[i - 3][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + ' ' + tagged_phrase[i - 2][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 2][0]
                                if tagged_phrase[i - 2][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 2][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 2][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 2][0]
                            if tagged_phrase[i - 2][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 2][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 2][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                elif tagged_phrase[i - 2][0] == 'on':
                    if i + 1 >= len(tagged_phrase):
                        if i - 4 >= 0:
                            if tagged_phrase[i - 4][1] == 'JJ' and tagged_phrase[i - 4][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 3][0]
                            if tagged_phrase[i - 3][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 3][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 3][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                        remove.append(i - 2)
                    elif tagged_phrase[i + 1][0] != 'of' and tagged_phrase[i][0] not in most:
                        if i - 4 >= 0:
                            if tagged_phrase[i - 4][1] == 'JJ' and tagged_phrase[i - 4][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 3][0]
                            if tagged_phrase[i - 3][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 3][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 3][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                        remove.append(i - 2)
        except:
            pass
        # to the right/left/back/front
        try:
            if tagged_phrase[i][0] in leftRelations or tagged_phrase[i][0] in rightRelations or tagged_phrase[i][
                0] in frontRelations or tagged_phrase[i][0] in backRelations:
                if tagged_phrase[i - 2][0] == 'to' and tagged_phrase[i - 1][0] == 'the':
                    if i + 1 >= len(tagged_phrase):
                        if i - 4 >= 0:
                            if tagged_phrase[i - 4][1] == 'JJ' and tagged_phrase[i - 4][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 3][0]
                            if tagged_phrase[i - 3][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 3][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 3][0] + "s ")
                        relations.append(tagged_phrase[i][0])
                        if tagged_phrase[i + 1][0] in leftRelations or tagged_phrase[i + 1][0] in rightRelations or \
                                tagged_phrase[i + 1][0] in frontRelations or tagged_phrase[i + 1][0] in backRelations:
                            relations.append(tagged_phrase[i][0] + ' ' + tagged_phrase[i + 1][0])
                            remove.append(i + 1)
                        else:
                            relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                        remove.append(i - 2)
                    elif tagged_phrase[i + 1][0] != 'of':
                        if i - 4 >= 0:
                            if tagged_phrase[i - 4][1] == 'JJ' and tagged_phrase[i - 4][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 4][0] + ' ' + tagged_phrase[i - 3][0] + "s ")
                            else:
                                if original == '':
                                    original = tagged_phrase[i - 3][0]
                                if tagged_phrase[i - 3][0] + "s" not in objects:
                                    objects.append(tagged_phrase[i - 3][0] + "s")
                                else:
                                    objects.append(tagged_phrase[i - 3][0] + "s ")
                        else:
                            if original == '':
                                original = tagged_phrase[i - 3][0]
                            if tagged_phrase[i - 3][0] + "s" not in objects:
                                objects.append(tagged_phrase[i - 3][0] + "s")
                            else:
                                objects.append(tagged_phrase[i - 3][0] + "s ")
                        if tagged_phrase[i + 1][0] in leftRelations or tagged_phrase[i + 1][0] in rightRelations or \
                                tagged_phrase[i + 1][0] in frontRelations or tagged_phrase[i + 1][0] in backRelations:
                            relations.append(tagged_phrase[i][0] + ' ' + tagged_phrase[i + 1][0])
                            remove.append(i + 1)
                        else:
                            relations.append(tagged_phrase[i][0])
                        remove.append(i)
                        remove.append(i - 1)
                        remove.append(i - 2)
        except:
            pass
        # below/above the/a
        try:
            if tagged_phrase[i][0] in bottomRelations or tagged_phrase[i][0] in topRelations:
                if i + 2 < len(tagged_phrase):
                    if tagged_phrase[i + 1][0] == 'the':
                        if tagged_phrase[i + 2][1] == 'NN':
                            objects.append(tagged_phrase[i + 2][0])
                            remove.append(i)
                            remove.append(i + 2)
        except:
            pass
        # left/right of the
        try:
            if (tagged_phrase[i][0] in leftRelations or tagged_phrase[i][0] in rightRelations) and tagged_phrase[i + 1][
                0] == 'of' and tagged_phrase[i + 2][0] == 'the':
                objects.append(tagged_phrase[i + 3][0])
                relations.append(tagged_phrase[i][0]+' of')
        except:
            pass
        # on the
        try:
            if tagged_phrase[i][0] == 'on' and tagged_phrase[i+1][0] == 'the' and tagged_phrase[i+2][0] != 'left' and tagged_phrase[i+2][0] != 'right':
                print('yes')
        except:
            pass
        inof = ['in', 'on', 'of']
        try:
            j = i
            k = 0
            while tagged_phrase[j][0] in masterRelations and (tagged_phrase[j - 1][0] not in inof or j - 1 < 0) and (
                    tagged_phrase[j - 2][0] not in inof or j - 2 < 0 or tagged_phrase[j][0] in most) and (
                    tagged_phrase[j + 1][0] not in inof or j + 1 >= len(tagged_phrase) or tagged_phrase[j][0] in most):
                if tagged_phrase[j][0] in rightRelations:
                    relations.append('right')
                    remove.append(j)
                if tagged_phrase[j][0] in leftRelations:
                    relations.append('left')
                    remove.append(j)
                if tagged_phrase[j][0] in topRelations:
                    relations.append('above')
                    remove.append(j)
                if tagged_phrase[j][0] in bottomRelations:
                    relations.append('below')
                    remove.append(j)
                if tagged_phrase[j][0] in frontRelations:
                    relations.append('front')
                    remove.append(j)
                if tagged_phrase[j][0] in backRelations:
                    relations.append('back')
                    remove.append(j)
                k = k + 1
                j = j + 1
                i = i + 1
            if tagged_phrase[j][1] == 'JJ':
                j = j + 1
            if original == '' and tagged_phrase[j][0] != 'the' and k != 0:
                try:
                    if j + 1 >= len(tagged_phrase):
                        if tagged_phrase[j - 2][1] == 'NN':
                            if tagged_phrase[j - 1][1] == 'JJ' and tagged_phrase[j - 1][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[j - 2][0] + ' ' + tagged_phrase[j - 1][0] + ' ' + \
                                               tagged_phrase[j][0]
                            else:
                                if original == '':
                                    original = tagged_phrase[j - 2][0] + ' ' + tagged_phrase[j][0]
                        else:
                            if tagged_phrase[j - 1][1] == 'JJ' and tagged_phrase[j - 1][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[j - 1][0] + ' ' + tagged_phrase[j][0]
                            else:
                                if tagged_phrase[j - 3][1] == 'JJ' and tagged_phrase[j - 3][0] not in masterRelations:
                                    if original == '':
                                        original = original = tagged_phrase[j - 3][0] + ' ' + tagged_phrase[j][0]
                                else:
                                    if original == '':
                                        original = tagged_phrase[j][0]
                    else:
                        if tagged_phrase[j - 1][1] == 'NN':
                            if tagged_phrase[j - 2][1] == 'JJ' and tagged_phrase[j - 1][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[j - 2][0] + ' ' + tagged_phrase[j - 1][0] + ' ' + \
                                               tagged_phrase[j][0]
                            else:
                                if original == '':
                                    original = tagged_phrase[j - 2][0] + ' ' + tagged_phrase[j][0]
                        else:
                            if tagged_phrase[j - 1][1] == 'JJ' and tagged_phrase[j - 1][0] not in masterRelations:
                                if original == '':
                                    original = tagged_phrase[j - 1][0] + ' ' + tagged_phrase[j][0]
                            else:
                                if tagged_phrase[j - 2][1] == 'JJ' and tagged_phrase[j - 2][0] not in masterRelations:
                                    if original == '':
                                        original = tagged_phrase[j - 2][0] + ' ' + tagged_phrase[j][0]
                                else:
                                    if original == '':
                                        original = tagged_phrase[j][0]
                except:
                    if original == '':
                        original = tagged_phrase[j][0]
            modified = original + 's'
            while k > 0:
                objects.append(modified)
                modified = modified + ' '
                k = k - 1
        except:
            pass
        if tagged_phrase[i][0] == 'my':
            try:
                if tagged_phrase[i + 1][0] in masterRelations:
                    objects.append('me')
                    relations.append(tagged_phrase[i + 1][0])
                    originalflag = True
                    remove.append(i)
                    remove.append(i + 1)
            except:
                pass
        if tagged_phrase[i][0] == 'your':
            try:
                if tagged_phrase[i + 1][0] in masterRelations:
                    objects.append('you')
                    relations.append(tagged_phrase[i + 1][0])
                    originalflag = True
                    remove.append(i)
                    remove.append(i + 1)
            except:
                pass
        if "'" in tagged_phrase[i][0]:
            try:
                if tagged_phrase[i + 1][0] in masterRelations:
                    objects.append(tagged_phrase[i][0][slice(0, -2)])
                    relations.append(tagged_phrase[i + 1][0])
                    originalflag = True
                    remove.append(i)
                    remove.append(i + 1)
            except:
                pass
        if tagged_phrase[i][0] == 'front':
            try:
                if tagged_phrase[i - 1][0] == 'in' and tagged_phrase[i + 1][0] == 'of':
                    tagged_phrase[i] = (tagged_phrase[i][0], 'JJ')
            except:
                pass
        if tagged_phrase[i][0] in leftRelations or tagged_phrase[i][0] in rightRelations:
            try:
                if tagged_phrase[i - 2][0] == 'to' and tagged_phrase[i - 1][0] == 'the' and tagged_phrase[i + 1][
                    0] == 'of':
                    tagged_phrase[i] = (tagged_phrase[i][0], 'JJ')
            except:
                pass
        if tagged_phrase[i][0] in masterRelations:
            try:
                if tagged_phrase[i + 1][0] == 'of':
                    tagged_phrase[i] = (tagged_phrase[i][0], 'JJ')
            except:
                pass
        i = i + 1

    for i in range(0, len(tagged_phrase)):
        if tagged_phrase[i][0] == 'the' and i not in remove:
            remove.append(i)

    remove.sort()
    for i in range(0, len(remove)):
        del tagged_phrase[remove[i] - i]

    # Extracting noun phrases from the sentence
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    chunk_parser = RegexpParser(grammar)
    result = chunk_parser.parse(tagged_phrase)
    iob_tagged_phrase = nltk.tree2conlltags(result)
    print(iob_tagged_phrase)

    # Extracting relationships between noun phrases
    noun_phrases = []
    relationships = []
    findOutside(iob_tagged_phrase, relationships)
    findNounPhrase(iob_tagged_phrase, noun_phrases)
    if original not in noun_phrases and original != '':
        noun_phrases.append(original)
    if originalflag:
        original = noun_phrases[0]
        if 'robot' not in objects and 'my' not in objects and 'you' not in objects:
            objects.pop()
    print('objects')
    print(objects)
    print('relations')
    print(relations)
    while len(objects) < len(relations):
        objects.append(objects[-1] + ' ')

    semantic.append(original)
    semantic.append(objects)
    semantic.append(relations)

    print('original:  ' + original)

    # Creating list of nouns and their classifiers
    nounClassifiers = []
    colors = ['red', 'blue', 'black', 'white', 'yellow', 'green', 'pink', 'purple']
    for i in range(0, len(noun_phrases)):
        phrase_array = WhitespaceTokenizer().tokenize(noun_phrases[i])
        tagged_phrase = nltk.pos_tag(phrase_array)
        for i in range(0, len(tagged_phrase)):
            if tagged_phrase[i][0] == 'sphere' or tagged_phrase[i][0] == 'cylinders' or tagged_phrase[i][
                0] == 'boxes' or tagged_phrase[i][0] == 'pyramids':
                tagged_phrase[i] = (tagged_phrase[i][0], 'NN')
            if tagged_phrase[i][0] in colors:
                tagged_phrase[i] = (tagged_phrase[i][0], 'JJ')
            if tagged_phrase[i][0] in descriptor_prepositions:
                tagged_phrase[i] = (tagged_phrase[i][0], 'JJ')
        identifyNounClassifiers(nounClassifiers, tagged_phrase)

    return noun_phrases, relationships, nounClassifiers, semantic