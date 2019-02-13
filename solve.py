from __future__ import division
from itertools import permutations
from re import findall
from string import maketrans

def solve(s):
    words = findall('[A-Za-z]+', s)
    chars = set(''.join(words))
    assert len(chars) <= 10
    firsts = set(w[0] for w in words)
    chars = ''.join(firsts) + ''.join(chars -firsts)
    n = len(firsts)
    for perm in permutations('0123456789', len(chars)):
        if '0' not in perm[:n]:
            trans = maketrans(chars, ''.join(perm))
            equation = s.translate(trans)
            try:
                if eval(equation):
                    print equation
            except ArithmeticError:
                pass

for alphametic in [
        'SEND + MORE == MONEY',
        'VIOLIN * 2 + VIOLA == TRIO + SONATA',
        'SEND + A + TAD + MORE == MONEY',
        'ZEROES + ONES == BINARY',
        'DCLIZ + DLXVI == MCCXXV',
        'COUPLE + COUPLE == QUARTET',
        'FISH + N + CHIPS == SUPPER',
        'SATURN + URANUS + NEPTUNE + PLUTO == PLANETS',
        'EARTH + AIR + FIRE + WATER == NATURE',
        'TWO * TWO == SQUARE',
        'HIP * HIP == HURRAY',
        'PI * R ** 2 == AREA',
        'NORTH / SOUTH == EAST / WEST',
        'NAUGHT ** 2 == ZERO ** 3',
        'I + THINK + IT + BE + THINE == INDEED',
        'DO + YOU + FEEL == LUCKY',
        'NOW + WE + KNOW + THE == TRUTH',
        'SORRY + TO + BE + A + PARTY == POOPER',
        'SORRY + TO + BUST + YOUR == BUBBLE',
        'STEEL + BELTED == RADIALS',
        'ABRA + CADABRA + ABRA + CADABRA == HOUDINI',
        'I + GUESS + THE + TRUTH == HURTS',
        'LETS + CUT + TO + THE == CHASE',
        'THATS + THE + THEORY == ANYWAY',
        '1/(2*X-Y) == 1',        
    ]:
    print alphametic
    solve(alphametic)
    print