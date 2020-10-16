

with open('./test.txt', 'r') as rf:
    with open('./test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

    with open('./test_copy.txt', 'a') as wf:
        wf.write('\nThis is EOF!!!')
