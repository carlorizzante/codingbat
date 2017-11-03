# We want make a package of goal kilos of chocolate. We have small bars
# (1 kilo each) and big bars (5 kilos each). Return the number of small bars
# to use, assuming we always use big bars before small bars. Return -1 if it
# can't be done.

def make_chocolate(small, big, goal):
    if goal % 5 <= small and 5 * big + small >= goal:
        if goal > 5 * big:
            return goal - 5 * big
        else:
            return goal % 5
    else:
        return -1
