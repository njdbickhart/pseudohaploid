# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:22:08 2019

@author: dbickhart
"""
import sys


def process_paf(paf : str, outfile : str) -> int:
    # Process file and filter based on percent ID and alignment length
    filtered = 0
    with open(paf, 'r') as input, open(outfile, 'w') as out:
        for l in input:
            l = l.rstrip()
            s = l.split()
            
            pid = (float(s[9]) / float(s[10])) * 100
            if pid < 90 or int(s[10]) < 1000:
                filtered += 1
                next
            
            alenr = int(s[8]) - int(s[7])
            alenq = int(s[3]) - int(s[2])
            
            # rotate values to conform to coords file
            if s[4] == '-':
                t = s[3]
                s[3] = s[2]
                s[2] = t
            
            block = [s[7], s[8], s[2], s[3], alenr,
                     alenq, pid, s[6], s[1], s[5], s[0]]
            
            out.write("\t".join(block) + "\n")
    
    return filtered

process_paf(snakemake.input[0], snakemake.output[0])
            
"""
if __name__ == "__main__":
    usage = "python3 " + sys.argv[0] + " <input paf file> <output coords file>\n"
    
    if len(sys.argv) < 3:
        print(usage)
        sys.exit(-1)
        
    filtered = process_paf(sys.argv[1], sys.argv[2])
    
    print(f'Removed {filtered} entries from PAF file')
"""