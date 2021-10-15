"""

Created on Various Days 

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

"""

from TOpsPy.Modeling.GmTVector import *
 
    
    
def eleAxialForce(eleTag):
    import openseespy.opensees as ops
    
    '''
    
    This Function Return the Axial force of an element
    Tere is some Possibility that Element has some external
    Loads among its length so the axial force in the start 
    and in the end of the element can be different
    so this code returns two values, One for start and One for End
    
    '''
    Nodes=ops.eleNodes(eleTag)
    Nodei=ops.nodeCoord(Nodes[0])
    Nodej=ops.nodeCoord(Nodes[1])

    print(f'node 1 {Nodei} and type is {type(Nodei)}')

    #Initial Data
    x1, y1, z1=Nodei[0],Nodei[1],Nodei[2]
    x2, y2, z2=Nodej[0],Nodej[1],Nodej[2]
    
    R1=[x2-x1,y2-y1,z2-z1]

    elfor=ops.eleForce(eleTag)
    elefocesi=elfor[0:3]
    elefocesj=elfor[6:9]

    print(f'node 1 {elefocesi} and type is {type(elefocesj)}')

    eleAxial1=DotPrdct(elefocesi,R1)
    eleAxial2=DotPrdct(elefocesj,R1)

    return eleAxial1,eleAxial2
