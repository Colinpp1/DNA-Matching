import os
import sys
import subprocess
import timeit
import glob


start = timeit.default_timer()
os.chdir(os.curdir)
emb="/opt/exp_soft/emboss/bin/"
seqA=os.curdir+"/"+sys.argv[1]+"/"
seqB=os.curdir+"/"+sys.argv[2]+"/"
root=os.curdir+"/"
m = len(glob.glob1(seqA,"*.fasta"))
n = len(glob.glob1(seqB,"*.fasta"))
file=(os.listdir(seqB)[0])
for i in range(0,m):
    file1 = (os.listdir(seqA)[i])
    for j in range(0,n):
       file2 = (os.listdir(seqB)[j])
       os.system(emb+"stretcher "+seqA+file1+" "+seqB+file2+" "+root+file+".txt")
       myline=""
       f = open(root+file+".txt")
       for i, line in enumerate(f):
           if i == 24:
              myline=line[9:14]	
              break
       f.close()
       score = myline
       FILE=open(root+"score.txt",'a')
       FILE.write(score+"\n")
       FILE.close()

stop = timeit.default_timer()



