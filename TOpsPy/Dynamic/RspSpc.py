"""


@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""
from TOpsPy.Dynamic.SDFTHA import *
 
def RspSpc(Acceleration,dt,PeriodRange,Damping):
    '''
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com
    @Date: 10/14/2021
    
    This function return the linear response spectrum of the defined acceleration in the definded period range 

    Parameters
    ----------
    Acceleration : should be a List.
    dt : is a float variable.
    PeriodRange : Should be a list.
    Damping : Is a float variable.

    The function returns 
    -------
    Tn : Period Range as list
    d : Displacement response spectrum as list.
    v : Pseudo Velocity as list.
    s : Pseudo Acceleration as list.

    '''
    
    
    import math
    
    
    #Define some parameters to store the results
    Tn=[]
    d=[]
    v=[]
    s=[]
    
    for T in PeriodRange:
        wn=2*math.pi/T
        [t,ut]=SDFTHA(Acceleration,dt,wn,Damping)
        ut=[abs(i) for i in ut]
        d.append(max(ut))
        v.append(max(ut)*wn)
        s.append(max(ut)*wn**2)
        Tn.append(T)
     
    return Tn,d,v,s

