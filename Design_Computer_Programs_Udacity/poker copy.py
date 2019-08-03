# -----------
# User Instructions
# 
# Modify the poker() function to return the best hand 
# according to the hand_rank() function. Since we have
# not yet written hand_rank(), clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 
#

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key = hand_rank)

 # First the described behavior of each function was assumed
# and later the functions were implemented

def straight(ranks):
    "Returns True if the ordered ranks form a 5-card straight"
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Returns True if all the cards have the same suit"
    suits = [s for r,s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))

    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, card_ranks(hand))


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    fk_ranks = card_ranks(fk) # [9, 9, 9, 9, 7]
    fp_ranks = card_ranks(tp) # [9, 9, 6, 5, 5]

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 7, 6, 5, 2]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert kind(4, fk_ranks) == 9
    assert kind(3, fk_ranks) == None
    assert kind(2, fk_ranks) == None
    assert kind(1, fk_ranks) == 7

    assert two_pair(fk_ranks) == None
    assert two_pair(fp_ranks) == (9, 5)

    # Modify the test() function to include three new test cases.
    # These should assert that card_ranks gives the appropriate
    # output for the given straight flush, four of a kind, and
    # full house.
    #
    # For example, calling card_ranks on sf should output  
    # [10, 9, 8, 7, 6]
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]    
    # Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf

    # add 3 new assert statements here.
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    return "tests pass"
        
print (test())
