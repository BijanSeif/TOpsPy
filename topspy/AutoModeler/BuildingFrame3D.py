def BuildingFrame3D(numBayX, numBayY, numFloor):
    import openseespy.opensees as ops
    '''
    This model modes 3D building that beams and columns are connectied to each other continuesly
    only enter number of bays and floors
    model is ready for eigen value analysis
    Sample:
    BuildingFrame3D(numBayX=4, numBayY=4, numFloor=5)
    
    '''
    ops.wipe()
    ops.model('Basic', '-ndm', 3, '-ndf', 6)

    bayWidthX = 6.0
    bayWidthY = 5.0
    storyHeights = [3 for x in range(numFloor+1)]

    E = 2.1e10
    massX = 2000

    coordTransf = "Linear"


    # Nodes
    nodeTag = 1
    zLoc = 0.
    for k in range(0, numFloor + 1):
        xLoc = 0. 
        for i in range(0, numBayX + 1):
            yLoc = 0.
            for j in range(0, numBayY + 1):
                ops.node(nodeTag, xLoc, yLoc, zLoc)
                ops.mass(nodeTag, massX, massX, 0.01, 1e-5,1e-5, 1e-5)
                if k == 0:
                    ops.fix(nodeTag, 1, 1, 1, 1, 1, 1)

                yLoc += bayWidthY
                nodeTag += 1
                NodetagL=nodeTag-1

            xLoc += bayWidthX

        if k < numFloor:
            storyHeight = storyHeights[k]

        zLoc += storyHeight


    # Define Elements
    ops.geomTransf("Linear", 1, 1, 0, 0)
    ops.geomTransf("Linear", 2, 0, 0, 1)

    eleTag = 1
    nodeTag1 = 1

    #Add Columns
    for k in range(0, numFloor):
        for i in range(0, numBayX+1):
            for j in range(0, numBayY+1):
                nodeTag2 = nodeTag1 + (numBayX+1)*(numBayY+1)
                iNode = ops.nodeCoord(nodeTag1)
                jNode = ops.nodeCoord(nodeTag2)
                ops.element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 0.25, E, E/2/1.3, 0.1**4/12, 0.05**4/12, 0.05**4/12, 1)
                eleTag += 1
                nodeTag1 += 1

    # add beam elements
    nodeTag1 = 1+ (numBayX+1)*(numBayY+1)

    for j in range(1, numFloor + 1):
        for i in range(0, numBayX):
            for k in range(0, numBayY+1):
                nodeTag2 = nodeTag1 + (numBayY+1)
                iNode = ops.nodeCoord(nodeTag1)
                jNode = ops.nodeCoord(nodeTag2)
                ops.element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 0.25, E, E/2/1.3, 0.1**4/12, 0.05**4/12, 0.05**4/12, 2)
                eleTag += 1
                nodeTag1 += 1

        nodeTag1 += (numBayY+1)

    # add beam elements
    nodeTag1 = 1+ (numBayX+1)*(numBayY+1)

    for j in range(1, numFloor + 1):
        for i in range(0, numBayY+1):
            for k in range(0, numBayX):
                nodeTag2 = nodeTag1 + 1
                iNode = ops.nodeCoord(nodeTag1)
                jNode = ops.nodeCoord(nodeTag2)
                ops.element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 0.25, E, E/2/1.3, 0.1**4/12, 0.05**4/12, 0.05**4/12, 2)
                eleTag += 1
                nodeTag1 += 1
            nodeTag1 += 1

    # set damping based on first eigen mode
    # freq = ops.eigen('-genBandArpack', 1)[0]**0.5
    # dampRatio = 0.05
    # ops.rayleigh(0., 0., 0., 2*dampRatio/freq)