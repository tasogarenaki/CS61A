"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########

# ----------------------------------------- Q1 ---------------------------------- #
def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # Index must be corrected, it's like 'remove' all the False Index
    # In this case used 2 different Index Systems to locate the correct one

    # Check the List with full Indexs
    for i in range(len(paragraphs)):
        if select(paragraphs[i]):
            # Check the corrected Index with right order
            if k == 0:
                return paragraphs[i]
            k -= 1
    return ''






# ----------------------------------------- Q2 ---------------------------------- #
def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'

    >>> dogs = about(['dogs', 'hounds'])
    >>> dogs('A paragraph about cats.')
    False
    >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
    True
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # Use Higher-Order Function
    def check(x):
        # remove punctuations, lowercase of sentence then split via utils.py
        x = split(lower(remove_punctuation(x)))
        # use double for-statement to find the same key word
        for i in topic:
            # samke as topic[i] == x[k]:
            if i in x:
                return True
        return False
    return check
    





# ----------------------------------------- Q3 ---------------------------------- #
def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    len_typed, len_ref = len(typed_words), len(reference_words)
    count, k = 0, 0
    
    # if texts are empty, return 0.0
    if typed_words == [] or reference_words == []:
        return 0.0
    else:
        for i in typed_words:
            # for case len_typed > len_ref (out of range) -> break
            if k >= len_ref:
                break
            # use different index (i and k), cause i are str not int
            if i == reference_words[k]:
                count += 1
            k += 1
    return float(count/len_typed) * 100






# ----------------------------------------- Q4 ---------------------------------- #
def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # characters / 5 (as question required, incl. spaces)
    # >>> len(typed) / 5 * 60 / elapsed
    return 12 * len(typed) / elapsed






# ----------------------------------------- Q5 ---------------------------------- #
def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    min_diff, index = -1, 0
    flag = False
    if limit == 0 or user_word in valid_words:
        return user_word
    else:
        for i, k in enumerate(valid_words):
            # count the lowest difference between user and valid
            diff = diff_function(user_word, k, limit)
            # change the min diff then only let the lowest diff in
            if min_diff == -1 or diff < min_diff:
                min_diff = diff
                # marke the lowest diff index
                if diff <= limit:
                    index = i
                    flag = True
    # if lowest diff > limit
    if flag == False:
        return user_word
    return valid_words[index]






# ----------------------------------------- Q6 ---------------------------------- #
def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    diff = abs(len(start)-len(goal))

    # version 1: return the correct answer for tests, but didn't pass the ok.py
    # can't figured out why
    """
    count = 0
    # Question required
    if count > limit:
        return limit + 1
    # return diff_length + total 
    if len(start) == 0 or len(goal) == 0:
        return count + diff
    # count the different chars
    if start[0] != goal[0]:
        count += 1
    # recursion: use [1:] -> by running every time the length of string will -1
    # + count, cause will reset as 0 every time
    return shifty_shifts(start[1:], goal[1:], limit) + count
    """

    # version 2: use Higher-Order function pass the ok.py
    def counting(start, goal, limit, count):
        if count > limit:
            return limit + 1
        if len(start) == 0 or len(goal) == 0:
            return count + diff
        if start[0] != goal[0]:
            count += 1
        return counting(start[1:], goal[1:], limit, count)
    return counting(start, goal, limit, 0)






# ----------------------------------------- Q7 ---------------------------------- #
def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # similar as shifty_shifts

    
    def counting(start, goal, limit, count):
        diff = abs(len(start)-len(goal))
        if count > limit:
            return limit + 1
        # if one is empty, should change n times of lengh another word which is diff
        if len(start) == 0 or len(goal) == 0:
            return count + diff
        # if same char, skip with next char
        if start[0] == goal[0]:
            return counting(start[1:], goal[1:], limit, count)
        # minimize the amount
        # if diff char, there's three conditions 
        # 1) compare with same index
        # 2)/3):
        # compare with one word each time, maybe a[1] == b[0]
        # or a[0] == b[1], e.g. a, b = "ckiteus", "kittens"
        return min(counting(start[1:], goal[1:], limit, count+1), 
        counting(start[1:], goal, limit, count+1), counting(start, goal[1:], limit, count+1))
    
    return counting(start, goal, limit, 0)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########

# ----------------------------------------- Q8 ---------------------------------- #
def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    i = 0
    for k in typed:
        # located the first incorrect word
        if k != prompt[i]:
            break
        i += 1
    # calculate the error ratio
    progress = i / len(prompt)
    # "print"
    send({'id': user_id, 'progress': progress})
    return progress 


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report





# ----------------------------------------- Q9 ---------------------------------- #
def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    """
    >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
    >>> words = ['This', 'is', 'fun']
    >>> game = time_per_word(p, words)
    >>> all_words(game)   ----> game[0]
    ['This', 'is', 'fun']
    >>> all_times(game)   ----> game[1]
    [[3,2,1],[4,2,3]]

    >>> p = [[0, 2, 3], [2, 4, 7]]
    >>> game = time_per_word(p, ['hello', 'world'])
    >>> word_at(game, 1)   ----> game[0][word_index]
    'world'
    >>> all_times(game)
    [[2,1],[2,3]]
    >>> time(game, 0, 1)   ----> game[1][player_num][word_index]
    1: 0 -> [2,1] -> 1 -> [1]
    """

    # Initial 2D-Array
    # times[i][j] with player i (num) and index of word j (num)
    times = [[0 for i in range(len(j)-1)] for j in times_per_player]
    i = 0
    for layer1 in times_per_player:
        # first value represents the initial starting time
        j = 0
        for layer0 in layer1:
            if j != 0:
                # e.g. times[0][0] = times_per_player[0][1] - times_per_player[0][0]
                #                  = 4 - 1 = 3
                times[i][j-1] = layer0 - layer1[j-1]
            j += 1
        i += 1
    # change the order as rrequested
    return game(words, times)





# ----------------------------------------- Q10 ---------------------------------- #
def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"

    """
    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 2]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
    # p0 has only 'What' faster than p1, so ['What']
    # p1 has both 'great' and 'luck' faster than p0, so ['great','luck']
    [['What'],['great','luck']]

    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 3]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  
    # with a tie, choose the first player
    [['What','luck'],['great']]
    """

    # see exmaple with time() by Q9
    # Initial a empty 2D-Array
    result = [[] for i in player_indices]
    # begin with compair for word 1 with different players 
    for word in word_indices:
        for player in player_indices:
            # default set the player 0 is always the winner
            # in the case of a tie, the player 0 wins 
            if player == 0:
                winer = 0
                # set the player's time as minimum
                min_time = time(game, player, word)
            # save the current time
            cur_time = time(game, player, word)
            # reset the minimum time 
            if cur_time < min_time:
                min_time = cur_time
                winer = player
        # add the word in the array
        result[winer] += [word_at(game, word)]
    return result 



def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)