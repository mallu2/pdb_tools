import pandas as pd
import mdtraj as md

def write_pdb(pandasDataFrame,outputfilename=DBD_PCA +"out.pdb"):
    outfile = open(outputfilename, 'w')
    for i in range(len(pandasDataFrame)-1):
        if len( pandasDataFrame.loc[i,2] ) == 4 :
            outfile.write('{dl[0]:6s}{dl[1]:5.0f} {dl[2]:4s} {dl[3]:3s} {dl[4]:1s}{dl[5]:4.0f}\
    {dl[6]:8.3f}{dl[7]:8.3f}{dl[8]:8.3f}{dl[9]:6.2f}{dl[10]:6.2f}\n'\
           .format(dl=pandasDataFrame.iloc[i]))
        else :
            outfile.write('{dl[0]:6s}{dl[1]:5.0f}  {dl[2]:3s} {dl[3]:3s} {dl[4]:1s}{dl[5]:4.0f}\
    {dl[6]:8.3f}{dl[7]:8.3f}{dl[8]:8.3f}{dl[9]:6.2f}{dl[10]:6.2f}\n'\
           .format(dl=pandasDataFrame.iloc[i]))
            
    outfile.write("TER\nEND\n")
    outfile.close()
