for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{}X{}={}".format(j, i, i*j), end=" ")
            if j == i:
                print('\n', end="")
