def main():
    infile = open('clients.txt','r')
    
    linenum=0
    for line in infile:
        linenum=linenum+1
        print(linenum,'.', line.rstrip('\n'),sep='')

main()
