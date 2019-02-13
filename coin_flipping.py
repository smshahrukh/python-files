
import sys
import numpy as np
import matplotlib.pyplot as plt

def build_walk(length=10000, bias=0):
    """
    Produces a random walk of given length and bias.
    """
    if bias < 0 or bias > .5:
        print('bias must be in [0,.5])')
        return
    flips = np.random.binomial(1, .5 - bias, size=length)
    steps = (flips * 2) - 1
    return np.cumsum(steps)


def display_walk(walk):
    """
    Plot the walk.
    """
    abscissas = range(len(walk))
    ordinates = walk
    plt.scatter(abscissas, ordinates, s=1, color='r')
    plt.show()


def main(length=10000, bias=0, seed=None):
    """
    Seed rng and call subroutines to build the walk and display it.
    """
    if seed:
        try:
            np.random.seed(seed=seed)
        except TypeError:
            np.random.seed(seed=0)
    walk = build_walk(length=length, bias=bias)
    print(len(walk) - np.count_nonzero(walk))
    display_walk(walk)


if __name__ == '__main__':
    ARGS = sys.argv[1:]
    if len(ARGS) not in range(4):
        print('wrong ARGS count.  length bias seed(optional)')
        exit()
    else:
        if not ARGS:
            main()
        if ARGS[0] == 'seed':
            main(seed=1)
        elif len(ARGS) == 1:
            main(length=int(ARGS[0]))
        elif len(ARGS) == 2:
            main(length=int(ARGS[0]), bias=float(ARGS[1]))
        else:
            main(length=int(ARGS[0]), bias=float(ARGS[1]), seed=int(ARGS[2]))