def KMCMatrixes():
    '''
    This function returns Stiffness, Mass and Damping Matrixes for the model that is loaded in the Domain
    [K,M,C]=KMCMatrixes()
    
    ## References

    - [Prof. Michael H. Scott - Mass & Stiffness Matrixes in Opensees](https://portwooddigital.com/2020/05/17/gimme-all-your-damping-all-your-mass-and-stiffness-too/)
    '''

    import openseespy.opensees as ops
    import numpy as np
    ## Mass And Stiffness Matrixes Calculation
    # create the analysis
    ops.wipeAnalysis()    # clear previously-define analysis parameters
    ops.constraints('Plain')    # how it handles boundary conditions
    ops.numberer('Plain')    # renumber dof's to minimize band-width (optimization), if you want to
    ops.system('FullGeneral') # how to store and solve the system of equations in the analysis
    ops.algorithm('Linear') # use Linear algorithm for linear analysis
    ops.integrator('GimmeMCK',1.0,0.0,0.0)
    ops.analysis('Transient')   # define type of analysis: time-dependent
    # ok=ops.analyze(1,dt)

    # Mass
    ops.integrator('GimmeMCK',1.0,0.0,0.0)
    ops.analyze(1,0.0)

    # Number of equations in the model
    N = ops.systemSize() # Has to be done after analyze

    M = ops.printA('-ret') # Or use ops.printA('-file','M.out')
    # print('M=',M)
    M = np.array(M) # Convert the list to an array
    M.shape = (N,N) # Make the array an NxN matrix


    # Stiffness
    ops.integrator('GimmeMCK',0.0,0.0,1.0)
    ops.analyze(1,0.0)
    K = ops.printA('-ret')
    # print('K=',K)
    K = np.array(K)
    K.shape = (N,N)


    # Damping (We do not need Damping matrix. I put it here just for any possible future need)
    ops.integrator('GimmeMCK',0.0,1.0,0.0)
    ops.analyze(1,0.0)
    C = ops.printA('-ret')
    # print('C=',C)
    C = np.array(C)
    C.shape = (N,N)
    
    return K,M,C