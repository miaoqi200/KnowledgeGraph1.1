with open('data/finallcql2020.csv', 'a+', encoding='utf-8') as ff:
    # with open('data/finallcql.csv', 'a+', encoding='utf-8') as f2:
    with open('data/finallcql.csv', 'r', encoding='utf-8') as f:
        for string in f:
            ff.write(string.replace(' ', ''))