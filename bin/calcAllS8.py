from __future__ import print_function
import os
cmdRoot = "python bin/calcS8Fisher.py "

#expList = ['S4-1.0-paper','S4-1.5-paper','S4-1.5-0.7','S4-1.5-0.3','S4-1.5-0.2','S4-1.5-0.1','S4-1.5-0.05','S4-2.0-paper','S4-2.5-paper','S4-3.0-paper']
expList = ['S4-1.0-paper','S4-1.5-paper','S4-2.0-paper','S4-2.5-paper','S4-3.0-paper']
calList = ['CMB_all']#,'CMB_pol']#,'CMB_all_miscentered','CMB_pol_miscentered']

#expList = ['S4','SO']
#expList = ['S4']
resList = ['']#-3m','-5m','-6m','-7m']
#atmList = ['-noatm']
atmList = ['']#,'-noatm']

#expList = ['S4','SO']
#resList = ['-3m','-5m','-6m','-7m']
#atmList = ['','-noatm']
#calList = ['CMB_all','owl2']#,'CMB_pol','owl1']
#calList = ['CMB_all','CMB_pol','CMB_all_miscentered','CMB_pol_miscentered']
#calList = ['CMB_pol']#,'CMB_pol','owl1']
#calList = ['owl1']#,'CMB_pol','owl1']

gridList = ['grid-default']
#gridList = ['grid-1.5','grid-1.2','grid-mid']


for exp in expList:
    for res in resList:
        for atm in atmList:
            for cal in calList:
                for grid in gridList:
            
                    cmd = cmdRoot + exp+res+atm+" "+grid+" "+cal+" "
                    print(cmd)
                    os.system(cmd)
