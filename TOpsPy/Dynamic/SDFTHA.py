"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""
   
     
def SDFTHA(Acceleration,dt,wn,Damping):
    '''
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com
    @Date: 10/14/2021
    
    
    Parameters
    ----------
    Acceleration : should be a List.
    dt : is a float variable.
    wn : Natural period of the SDF that should be a float value.
    Damping : Is a float variable.
    
    
    Funtion for calculating time history response of a SDF
    [t,ut]=SDFTH(e,dt,5,0.02)
    #Sample usage of the above function that calculate time history displacement response of a SDF with 
    0.02 damping and natural frequency equal to 2 under an acceleration that store in e (list) with dt time interval
    
    '''
    import openseespy.opensees as ops
    import numpy as np
    
    
    #Build the model
    ops.wipe()
    ops.model('basic', '-ndm', 2)
        
    # Define some parameters ...   
    m=1
    k=wn**2*m
    L=1
    E=float(100)
    A=k*L/E
    
    # Define an Elastic Material
    matTag=1
    ops.uniaxialMaterial("Elastic", matTag, E)
    
    #Define 2 nodes and mass and truss element
    ops.node(1, *[0,0])
    ops.fix(1,1,1,1)
    ops.node(2, *[L,0], '-mass', *[m,m,1.0e-10])
    ops.element('Truss', 1, *[1,2], A, matTag)
    
    
    # set damping based on first eigen mode
    freq = ops.eigen('-fullGenLapack', 3) # for the define model Always there is 3 Eigen Values
    freq=max(freq)
    freq=freq**0.5
    ops.rayleigh(0., 0., 0., 2*Damping/freq)
    
    
    # Set time series to be passed to uniform excitation
    ops.timeSeries('Path', 1, '-dt', dt, '-values', *Acceleration)

    # Create UniformExcitation load pattern
    ops.pattern('UniformExcitation',  1,   1,  '-accel', 1)

    # Delete the old analysis and all it's component objects
    ops.wipeAnalysis()
    ops.system('SparseGEN')
    ops.constraints('Transformation')
    ops.test('EnergyIncr', 1.0e-12,  10 )
    ops.algorithm('ModifiedNewton')
    ops.numberer('RCM')
    ops.integrator('Newmark',  0.5,  0.25 )
    ops.analysis('Transient')
    
    
    ut=[]
    
    for i in Acceleration: #Run Analysis for each step and get the results 
        ops.analyze(1, dt)
        u=ops.nodeResponse(2, 1, 1)
        ut.append(u)
    
    
    t=np.arange(0,dt*len(Acceleration),dt) #Time Vector
    
    
    
    
    #slv.drawModel() #To check the defined model
    return t, ut #Return the time vector and displacement history (ut)
    #--------------------------- End of the Function --------------------------
  
