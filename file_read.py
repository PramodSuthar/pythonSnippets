
## read mode
##f = open('./test.txt','r')
## write mode --> open('./test.txt','w')
## append mode --> open('./test.txt','a')
## read and write mode --> open('./test.txt','r+')

##print(f.name)
##print(f.mode)
##f.close()

with open('./test.txt','r') as f:
    ##f_content = f.read()
    ##print(f_content)

    ##f_content = f.readlines()
    ##print(f_content)
    """
    f_content = f.readline()
    print(f_content,end='')
    f_content = f.readline()
    print(f_content,end='')
    f_content = f.readline()
    print(f_content,end='')
    """

    ##for line in f:
        ##print(line, end='')
    """
    f_content = f.read(100)
    print(f_content)
    f_content = f.read(100)
    print(f_content)
    f_content = f.read(100)
    print(f_content)
    """
    """
    chunk = 100
    f_content = f.read(chunk)
    while len(f_content) > 0:
        print(f_content)
        f_content = f.read(chunk)

    """
    chunk = 100
    f_content = f.read(chunk)
    print(f.tell())
    print(f_content)
    f_content = f.read(chunk)
    print(f_content)
    print(f.tell())
    f.seek(0)
    print(f.tell())





















    



##print(f.closed)
    
