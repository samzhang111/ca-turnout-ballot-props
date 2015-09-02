with open('_ca-pop-raw.csv', 'r') as f:
    data = map(int, f.readline().strip().split(','))

    assert(len(data) == (2013 - 1971 + 1))

    data = zip(range(1971, 2013 + 1), data)

with open('ca-annual-pop.csv', 'w') as out:
    out.write('year,pop\n')
    for year, pop in data:
        out.write('%d,%d\n'%(year, pop))
