"""

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""
import os as _os
def LAT2(Filename):
    
    '''
     @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)
     
     LAT2=Load *.AT2 files in the current list
     
     A function for Transfering PEER NGA files (*.AT2) to the code parameters
     
     The function return [dt,e] where:
         
         dt= time interval (Float)
         e= Accelerogram Values (List)
     
    '''
    
    st=str(Filename)+'.AT2'
    
    pathdir=_os.path.dirname(__file__) #Get the current file path
    st=pathdir+'\\'+st
        
    
    f = open(st,'r')
    
    ee=f.readlines() #All data are located in e and so e is the time history 
    f.close()

    e=[]
    dt=None
    for i in ee:
        i=i.split()
        i=[i.upper() for i in i]
        
        #-------------------------------   Find dt ---------------------------------------------------------------------
        if 'DT=' in i:  # Find dt (Time interval)
            try:  #To check If next value doesn't be a number
                dt=float(i[i.index('DT=')+1])
            except:
                dt=None
                continue 
                
        if [a for a in i if a.startswith('DT=')==True and len(a)>3]!=[]:  #If Time Value was sticked to 'dt' Expression
            try: #To check If next value doesn't be a number
                dt=[a for a in i if a.startswith('DT=')==True and len(a)>3][0]
                dt=float(dt[3:len(dt)])
            except:
                dt=None
                continue
                
                
        if dt==None and 'NPTS,' in i and 'DT' in i:
            try:  #To check If next value doesn't be a number
                dt=float(i[1])
            except:
                dt=None
                continue
        #-----------------------------------------------------------------------------------------------------------------
        
    
        try: #Convert lines that are not string
            e.extend([float(m) for m in i])
        except:
            continue
    
    return dt,e


def Recordslist():
    pathdir=_os.path.dirname(__file__)
    return [x[:-4] for x in _os.listdir(pathdir) if x.endswith(".AT2") or x.endswith(".At2") or x.endswith(".at2")] #Get list of directories in the current file
