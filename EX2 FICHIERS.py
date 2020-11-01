from os import chdir
    
def copieFichierLigne(souce,destination):
    f=open("source","r")
    ch=f.readline()
    f.close()
    g=open("source","w")
    while(ch!=''):
        if (ch[0]!=@):
            g.write(ch)
        ch=f.readline()
    g.close()