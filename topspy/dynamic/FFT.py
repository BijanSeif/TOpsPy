"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""
   
     
def FFT(x, y, max_freq=None, Trange=None):
    '''
    This function returns the fourier transform of function y=f(x)
    
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com
    @Date: 11/08/2022
    
    
    Parameters
    ----------
    Acceleration : should be a List.
    x : Domain.
    y : Function f values of x.
    max_freq : maximum frequency That user wants to get the results for
    Trange : a two value list that specify range of results values be in this range
    
    
    Funtion calculates the Fourien transform and returns:
    [xf, Tf, wf, yf]
    xf : Frequency
    Tf : Period
    wf : Angular Speed
    yf : Frequency Magnitude
    
    sample: [xf,tf,wf, yf]=bdy.FFT(t,e,Trange=[0.3,0.4])     #Returns the fourier transform in the period range between 0.3 and 0.4 sec
    '''
    import numpy as np
    
    x=np.array(x)
    y=np.array(y)
    
    T=max(x)-min(x)
    N = y.shape[0]
    Nf = N // 2 if max_freq is None else int(max_freq * T)
    xf = np.linspace(0.00001, 0.5 * N / T, N // 2)               #Frequency
    Tf=1/xf                                                      #Period
    wf=2*np.pi/Tf                                                #Angular speed
    
    yf = 2.0 / N * np.fft.fft(y)   
    
    tbot=0
    ttop=Nf
    
    if Trange!=None and type(Trange)==list:
        if len(Trange)==2:
            T=list(Tf)
            ttop=T.index([i for i in T if i>=Trange[0]][-1])
            tbot=T.index([i for i in T if i>=Trange[1]][-1])        

    #Frequency Magnitude
    return xf[tbot:ttop], Tf[tbot:ttop], wf[tbot:ttop], yf[tbot:ttop]
    #--------------------------- End of the Function --------------------------
  
