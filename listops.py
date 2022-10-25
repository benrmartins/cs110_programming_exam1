# Returns True if any value in the list a is True, and False otherwise.
def any(a):
    # iterate through the entire list
    for i in a:
        # checks if value any item in the list is true
        if i:
            return True
    return False


# Returns True if all values in the list a are True, and False otherwise.
def all(a):
    # iterate through the entire list
    for i in a:
        # checks if value of all of the items of the list is true
        if not i:
            return False
    return True


# Returns True if exactly k values in the list a are True, and False otherwise.
def exactly(a, k):
    count = 0

    # iterate through the entire list
    for i in a:
        # counts the number of True items in the list
        if i:
            count += 1
    # check if k and the number of True items in the list is equal
    if k == count:
        return True

    return False


# Returns the number of True values in the list a.
def count(a):
    count = 0

    # iterate through the entire list
    for i in a:
        # counts the number of True items in the list
        if i:
            count += 1
    # returns the number of true items in the list
    return count


# Unit tests the library.
def _main():
    import stdio

    a = [False, False, True, False, True, True, True]
    stdio.writeln('a             = ' + str(a))
    stdio.writeln('any(a)        = ' + str(any(a)))
    stdio.writeln('all(a)        = ' + str(all(a)))
    stdio.writeln('exactly(a, 3) = ' + str(exactly(a, 3)))
    stdio.writeln('count(a)      = ' + str(count(a)))


if __name__ == '__main__':
    _main()
