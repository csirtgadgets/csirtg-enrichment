from csirtg_enrichment import resolve

DATA = [
    'google.com',
    '1.1.1.1',
    '8.8.8.8',
    'csirtgadets.com'
]


def test_basics():

    c = 0
    for i in DATA:
        r = resolve(i)
        c += len(r)

    assert c > 0
