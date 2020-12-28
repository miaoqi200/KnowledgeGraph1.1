with open('data/zstp14_ownthink_ON.csv', 'r', encoding='utf-8') as f:
    with open('data/zstp15_ownthink_NR_yes.csv', 'a+', encoding='utf-8') as ff:
        with open('data/zstp15_ownthink_NR_other.csv', 'a+', encoding='utf-8') as fff:
            with open('data/zstp15_ownthink_NR_out.csv', 'a+', encoding='utf-8') as ffff:
                for i in f:
                    line = i.split(',')
                    s = line[2]
                    for y in [r'\u3000', 'u3000', '&gt;', '&amp;', '&lt;', '&gt;', r'\u200b', 'u200b', r'\ufeff',
                              r'\xa0', '』',
                              r'\u200d', 'u200d']:
                        s = s.replace(y, '')
                    string = line[0] + ',' + line[1] + ',' + s + ',' + line[3]
                    if s != '':
                        if '\\' in string or '&' in string or '3000' in string or '200' in string:
                            fff.write(string)
                        else:
                            ff.write(string)
                    else:
                        ffff.write(string)


with open('data/zstp14_ownthink.csv', 'r', encoding='utf-8') as f:
    with open('data/zstp15_ownthink_NRN_yes.csv', 'a+', encoding='utf-8') as ff:
        with open('data/zstp15_ownthink_NRN_other.csv', 'a+', encoding='utf-8') as fff:
            with open('data/zstp15_ownthink_NRN_out.csv', 'a+', encoding='utf-8') as ffff:
                for i in f:
                    line = i.split(',')
                    s = line[2]
                    for y in [r'\u3000','u3000', '&gt;', '&amp;', '&lt;', '&gt;', r'\u200b','u200b', r'\ufeff', r'\xa0', '』',
                              r'\u200d','u200d']:
                        s = s.replace(y, '')
                    string = line[0] + ',' + line[1] + ',' + s + ',' + line[3]
                    if s != '':
                        if '\\' in string or '&' in string or '3000' in string or '200' in string:
                            fff.write(string)
                        else:
                            ff.write(string)
                    else:
                        ffff.write(string)

