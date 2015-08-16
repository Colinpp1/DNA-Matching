import subprocess
import os.path
import os

emb="/opt/exp_soft/emboss/bin/"
out="/home/cphillips/humanC"
root="/home/cphillips/"
f=open(root+"humanC.txt")
for i,line in enumerate(f):
    if i == 250:
       break;
    line=line.strip("\n")
    os.system(emb+"seqretsplit genbank:"+line+" -osdirectory2 "+out+" "+line+".fasta -auto")
f.close()
	

