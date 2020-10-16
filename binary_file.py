
"""
with open('./05.jpg', 'rb') as rf:
    with open('./05_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
"""


with open('./05.jpg', 'rb') as rf:
    with open('./005_copy.png', 'wb') as wf:
        chunk = 4096
        rf_content = rf.read(chunk)
        while len(rf_content) > 0:
            wf.write(rf_content)
            rf_content = rf.read(chunk)
