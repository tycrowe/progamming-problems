"""
DESCRIPTION:
    You’d like to figure out whether a car was speeding while it was driving down a straight road. Unfortunately, you
    don’t have any radar guns or related instruments for measuring speed directly; all you have are photographs taken
    of the car at various checkpoints on the road at various times. Given when and where these photographs were taken,
    what is the fastest speed that you can prove the car must have been going at some point along the road?

INPUT:
    The first line of input contains an integer 'n' (2≤n≤100), which is the number of photographs taken.

    Each of the following 'n' lines contains two space-separated integers 't' (0≤t≤104) and 'd' (0≤d≤106), where 't' is the
    time of the photograph in hours, and 'd' is the distance along the road in miles. The first photograph is always
    taken at time 0 with distance 0, and both the times and distances strictly increase.

OUTPUT:
    Output a single integer, which is the greatest integral speed that you can be certain the car was going at some
    point in miles per hour.

EXAMPLES:
    (1)
    Input:              Output:
    2                   6
    0 0
    7 42

    (2)
    Input:              Output:
    5                   34
    0 0
    5 24
    10 98
    15 222
    20 396

"""
import sys

number_of_photos = 0
max_ = 0
dOld = 0
tOld = 0

for i, line in enumerate(sys.stdin):
    if i == 0:
        number_of_photos = int(line)
    elif len(line) > 0:
        d_t = line.split(" ")
        tNew = int(d_t[0])
        t = tNew - tOld
        dNew = int(d_t[1])
        d = dNew - dOld
        if t != 0 and (d // t) > max_:
            max_ = d // t
        dOld = dNew
        tOld = tNew

print(max_)


