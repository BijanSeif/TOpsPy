"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""

  
from TOpsPy.Modeling.GmTVector import *

def ElePerPend(Nodei,Nodej):
    
    '''
    This Function Provide A Perpendicular Vector on the Line connected from 
    Nodei to Node join
        Nodei : Opensees 3D node as a list with 3 elements
        
    Nodej : Opensees 3D node as a list with 3 elements
    
    The 3rd coordinate value is considered as Vertical Direction
    
    '''
    
    #Initial Data
    x1, y1, z1=Nodei[0],Nodei[1],Nodei[2]
    x2, y2, z2=Nodej[0],Nodej[1],Nodej[2]
    
    
    R1=[x2-x1,y2-y1,z2-z1]
    if R1[0]==0 and R1[1]==0:
       R2=[R1[0],R1[1]+0.1,R1[2]]
    else:
       R2=[R1[0],R1[1],R1[2]+0.1]
       
    
    R3=VecProduct(R1,R2)
    R3=Nrmlz(R3,1)
    
    return R3
    
 