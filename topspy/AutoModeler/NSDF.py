"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""
   
     
def NSDF(Tn, DampRatio, E, Fy):
    
    '''
    This function Models a nonlinear single degree of freedom system where Fy is the yielding force
    
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com
    @Date: 10/14/2021
    
    
    Parameters
    ----------
    Tn : Natural period of the SDF that should be a float value.
    DampRatio : Is a float variable.
    E= Stiffness of the system
    Fy=Yield Force of the system
    '''
    import openseespy.opensees as ops
    #Model
    op.wipe()
    op.model('basic', '-ndm', 2, '-ndf', 3) 
    
    # Define some parameters ...   
    wn=2*3.1415/Tn
    L=1
    A=1
    k=E*A/L
    m=k/wn**2
    
    # Define an Elastic Material
    epsyP=Fy/E
    matTag=1
    ops.uniaxialMaterial('ElasticPP', MatTag, E, epsyP)
    
    #Define 2 nodes and mass and truss element
    ops.node(1, *[0,0])
    ops.fix(1,1,1,1)
    ops.node(2, *[L,0], '-mass', *[m,m,1.0e-10])
    ops.element('Truss', 1, *[1,2], A, matTag)
    
    # set damping based on first eigen mode
    freq = ops.eigen('-fullGenLapack', 3) # for the define model Always there is 3 Eigen Values
    freq=max(freq)
    freq=freq**0.5
    ops.rayleigh(2*DampRatio*freq, 0., 0., 0)    

    print(f'2DModel is ready and in the domain. node 1 is fixed and node 2 in the right side of node 1 is free and their mass and stifness cause wn={wn} or Tn={2*3.1415/wn}')