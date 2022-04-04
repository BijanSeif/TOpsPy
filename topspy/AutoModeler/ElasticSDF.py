"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""
   
     
def ElasticSDF(wn,Damping):
    '''
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com
    
    Parameters
    ----------
    wn : Natural period of the SDF that should be a float value.
    Damping : Is a float variable.
    
    Funtion for Modelng a SDF:
    ElasticSDF(5,0.02)
    
    '''
    import openseespy.opensees as ops
   
    
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
    ops.rayleigh(2*Damping*freq, 0., 0., 0)
    
    
    print(f'2DModel is ready and in the domain. node 1 is fixed and node 2 in the right side of node 1 is free and their mass and stifness cause wn={wn} or Tn={2*3.1415/wn}')