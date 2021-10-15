"""

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""

def LAT2(Filename):
    
    '''
     @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com
     @Date: 10/14/2021
     
     LAT2=Load *.AT2 files
     
     A function for Transfering PEER NGA files (*.AT2) to the code parameters
     
     The function return [dt,e] where:
         
         dt= time interval (Float)
         e= Accelerogram Values (List)
     
    '''
    
    st=str(Filename)+'.AT2'
    f = open(st,'r')
    
    ee=f.readlines() #All data are located in e and so e is the time history 

    e=[]
    for i in ee:
        i=i.split()
        i=[i.upper() for i in i]
    
        if 'DT=' in i:  # Find dt (Time interval)
            dt=float(i[i.index('DT=')+1])
        
    
        try: #Convert lines that are not string
            e.extend([float(m) for m in i])
        except:
            continue
    
    return dt,e

