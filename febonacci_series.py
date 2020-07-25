def elements_to_display(n):
    for r in range(0, n):
        if r == 0:
            i = r
            print i
        elif r == 1:
            j = r
            print j
        else:
            sum = i + j
            print sum
            i = j
            j = sum


if __name__ == '__main__':
    elements_to_display(6)
