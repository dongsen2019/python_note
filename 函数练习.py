def rtg(x, y, s=1):
    print('# '*x)
    for i in range(1, y-1):
        if s == 1:
            print('# '*x)
        else:
            nbsp = '  ' * (x-2)
            print('# {}#'.format(nbsp))
    print('# ' * x)

rtg(10,10,0)


