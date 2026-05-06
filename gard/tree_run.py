from Bio import SeqIO
import sys
import subprocess

alin = sys.argv[1]

skip = []

breakpoints = [830, 2053, 2982, 4318, 4933, 5464, 6156, 6868, 7945, 10342, 11515, 14034, 14601, 15480, 17313, 18351, 19395, 19923, 21003, 21705, 21828, 22816, 22935, 23868, 24803, 25670, 26075, 26423, 27852, 28319, 28772]


for i in range(len(breakpoints)):

    run = i +1
    
    if run not in skip:
            
        alfile = alin.replace('.fas', '_reg%i.fas'%run)
            
        start = 0
        if run != 1:
            start = breakpoints[i-1]
        
        end = breakpoints[i]
        
        fasta = ''    
        
        records = SeqIO.parse(alin, 'fasta')
        
        for rec in records:
            desc = rec.description
            thisseq = str(rec.seq)[start:end]
            fasta = fasta + '>%s\n%s\n'%(desc, thisseq)
        
        with open(alfile, 'w+') as out:
            out.write(fasta[:-1])
        
        cmd = 'iqtree2 -nt 20 -s %s -m GTR+F+R4 -B 10000'%alfile
        subprocess.Popen([cmd], shell = True,close_fds=True).wait()

        #do the last region
        if run == len(breakpoints):
            
            run = run +1
            alfile = alin.replace('.fas', '_reg%i.fas'%run)
                
            start = breakpoints[i]
            
            fasta = ''    
            
            records = SeqIO.parse(alin, 'fasta')
            
            for rec in records:
                desc = rec.description
                thisseq = str(rec.seq)[start:]
                fasta = fasta + '>%s\n%s\n'%(desc, thisseq)
            
            with open(alfile, 'w+') as out:
                out.write(fasta[:-1])
            
            cmd = 'iqtree2 -nt 6 -s %s -m GTR+F+I+G4 -B 10000'%alfile   
            subprocess.Popen([cmd], shell = True,close_fds=True).wait()        
