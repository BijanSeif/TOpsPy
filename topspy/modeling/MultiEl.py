'''
DATE: 10/26/2021

@author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)

'''

def _getNewNodeNum(Nodei,Nodej):
    import openseespy.opensees as ops
  
    Nodelist=ops.getNodeTags()
    
    cnt=0

    Numb=int(str(Nodei) + str(Nodej) + str(cnt))

    check=None

    while check!=True:

        if Numb in Nodelist:
            cnt +=1
            Numb=int(str(Nodei) + str(Nodej) + str(cnt))
        else:
            check=True
            return Numb

def _getNewEleNum(Nodei,Nodej):
    import openseespy.opensees as ops
  
    EleList=ops.getEleTags()    
    cnt=0

    Numb=int(str(Nodei) + str(Nodej) + str(cnt))

    check=None

    while check!=True:

        if Numb in EleList:
            cnt +=1
            Numb=int(str(Nodei) + str(Nodej) + str(cnt))
        else:
            check=True
            return Numb
    

def MultiEl(Nodei,Nodej,Number_Of_Elements,EleParameters):
    


    '''
    
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)
    
    
    This Function generate muli elements between two nodes automatically. 
    
    Attention:    
    *EleParameters=is all the parameters that you have to define for any kind of elements that you need
    Attention that the function automatically assign value to EleParameters[1] and EleParameters[2] and any 
    value that you enter for them is not important. for example:
    
    EleP=['elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag]-->
    MultiEl(Nodei=1,Nodej=2,Number_Of_Elements=5,*EleParameters=EleP)


    A complete usage sample:
        
    import topspy.modeling as bjm
    transfTag +=1
    Node1=ops.nodeCoord(1)
    Node2=ops.nodeCoord(3)
    vecxz=GmT.GmTVector(Node1,Node2,Theta)
    ops.geomTransf('Linear', transfTag, *vecxz)

    elep=['elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag] #Opensees desire Elements Parameters

    bjm.MultiEl(1,3,4,elep)
    
    Or you can write
    
    bjm.MultiEl(1,3,4,['elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, G_mod, Jxx, Iy, Iz, transfTag])

    '''

    
    import openseespy.opensees as ops



    n=Number_Of_Elements

    NodeiC=ops.nodeCoord(Nodei)
    NodejC=ops.nodeCoord(Nodej)

    x1,y1,z1=NodeiC[0],NodeiC[1],NodeiC[2]
    x2,y2,z2=NodejC[0],NodejC[1],NodejC[2]
    Lxi=(x2-x1)/n
    Lyi=(y2-y1)/n
    Lzi=(z2-z1)/n



    # --- Generating Nodes and Elements--------------------
    FstNode=Nodei #First Node Tag
    for i in range(n):

        Fstcoord=ops.nodeCoord(FstNode) #Get First Node Coordinate
        Sndcoord=[Fstcoord[0]+Lxi,Fstcoord[1]+Lyi,Fstcoord[2]+Lzi] #Second Node Coordinate

        if i==n-1: #If second node is comatible on the last node
            SndNode=Nodej                  #Second node is the last node and no need to produce new node
            Sndcoord=ops.nodeCoord(SndNode)
        else:                              #For second node we have to define new node
            SndNode=_getNewNodeNum(Nodei,Nodej) 
            ops.node(SndNode,*Sndcoord)

        
        Newele=_getNewEleNum(Nodei,Nodej) # New element Tag

        eleTag=Newele
        eleNodes=[FstNode,SndNode]+ EleParameters[4:]
        ops.element(EleParameters[0], eleTag, *eleNodes)


        FstNode=SndNode


    return 'Generated'


















