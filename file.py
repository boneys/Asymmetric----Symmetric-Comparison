import os
import time
i=1;
while(i<9):
   
    #System command to create file of sizes 100MB, 200MB ....
    file_name=raw_input("Input the name for %d00 MB file"%int(i))
    os.system("dd bs=100000000 count=%d if=/dev/zero of=%s >/dev/null " % (int(i),file_name))
    
    print("\n File %sMB Successfully Created \n" % file_name)
    file_sym=open("time_sy.txt","a")
    file_asy=open("time_asy.txt","a") 
    start=time.time()
    #Symmetric Encryption
    os.system("openssl aes-256-cbc -e -k boney -in %s -out %s" % (file_name,file_name))
    end=time.time()-start
    print("Time Taken for Symmetrically encrypting %s file  %f " % (file_name,end))
    file_sym.write("%d\t%f\n"% (i*100,end))
    start =time.time()
    #Asymmetric Encryption 
    os.system("openssl rsautl -encrypt -pubin -inkey public.pub -in %s -out %sencrypt" % (file_name,file_name))
    end=time.time()-start    
    print("Time Taken for Asymmetrically encrypting %s file  %f " % (file_name,end))
    file_asy.write("%d\t%f\n"%(i*100,end))
    i+=1
#Gnuplot command with command s in gnu_command.gp file    
os.system("gnuplot  gnu_command.gp")
file_sym.close()
file_asy.close()

