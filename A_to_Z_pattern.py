L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for a in range(0,len(L)+1):
    for b in range(0,a):
        print(L[b],end=' ')
    print()
