
   
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
    

def MultiEl(Nodei,Nodej,Number_Of_Elements,EleParameters,EndPinned='No',E=100e6):
    


    '''
    
    @author: Bijan SayyafZadeh (B.sayyaf@yahoo.com)
    
        
    This Function generate muli elements between two nodes automatically and finally after
    generating the fils it returns the middle node tag/s and it's/their coordinate. 
    
    
    Parameters
    ----------
    Acceleration : should be a List.
    Nodei              : The first node TAG.
    Nodej              : The last node TAG.
    EndPinned          : If the User wants end pinned connection it Should be enter 'Yes'.
    Number_Of_Elements : Number of Elements that want to be generated along node Nodei to Nodej.
    Attention:    
    *EleParameters     : is a list that all the parameters that you have to define for any kind of elements that you need
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
    
    Also Above Codes can be written in this way: bjm.MultiEl(1,3,4,elep,'Yes',1e9) That the last 'Yes' cause generating element with 2 end pinned head with zero length element.
    
    Function returns:
    ----------
    midtag=list of middle point/s Tag
    midcoord=list of nodecoordinate of middle point/s
    
    '''

    
    import openseespy.opensees as ops
    
    
    #Parameters For end Pinned Material
    matTag=1
    ops.uniaxialMaterial('Elastic', matTag, E)



    n=Number_Of_Elements
    
    #Check We will have One middle point or two
    midtag=[]
    midcoord=[]
    if n%2==0:
        elemtag=[n/2-1] #tag of element that it's 2ndNode is the middle
    else:
        elemtag=[(n-1)/2-1, (n-1)/2] #tag of element2 that it's 2ndNodes are the middle


    NodeiC=ops.nodeCoord(Nodei)
    NodejC=ops.nodeCoord(Nodej)

    x1,y1,z1=NodeiC[0],NodeiC[1],NodeiC[2]
    x2,y2,z2=NodejC[0],NodejC[1],NodejC[2]
    Lxi=(x2-x1)/n
    Lyi=(y2-y1)/n
    Lzi=(z2-z1)/n



    # --- Generating Nodes and Elements--------------------
    FstNode=Nodei #First Node Tag

    if EndPinned.upper()=='YES':    #If user Decide to have an element with end pinned connection
        
        Fstcoord=ops.nodeCoord(Nodei)
        lastcoord=ops.nodeCoord(Nodej)
        vecx=[lastcoord[0]-Fstcoord[0],lastcoord[1]-Fstcoord[1],lastcoord[2]-Fstcoord[2]] #Longitudinal Vector of the Element
        vecyp=[vecx[0],vecx[1]+0.1,vecx[2]]
        
        FstNode=_getNewNodeNum(Nodei,Nodej)
        ops.node(FstNode,*Fstcoord)
        
        Newele=_getNewEleNum(Nodei,Nodej) # New element Tag
        
        ops.element('zeroLength', Newele, *[Nodei,FstNode], 
                    '-mat', *[matTag,matTag,matTag,matTag],
                    '-dir', *[1,2,3,4],
                    '-orient', *vecx, *vecyp)
        
        
       
    for i in range(n):
        Fstcoord=ops.nodeCoord(FstNode) #Get First Node Coordinate
        Sndcoord=[Fstcoord[0]+Lxi,Fstcoord[1]+Lyi,Fstcoord[2]+Lzi] #Second Node Coordinate
        
        if i==n-1 and EndPinned.upper()!='YES': #If second node is comatible on the last node
            SndNode=Nodej                  #Second node is the last node and no need to produce new node
            Sndcoord=ops.nodeCoord(SndNode)
        
        else:

            SndNode=_getNewNodeNum(Nodei,Nodej) 
            ops.node(SndNode,*Sndcoord)
            
            if i in elemtag:
                midtag.append(SndNode)
                midcoord.append(Sndcoord)
            
        

        
        Newele=_getNewEleNum(Nodei,Nodej) # New element Tag

        eleTag=Newele
        eleNodes=[FstNode,SndNode]+ EleParameters[4:]
        ops.element(EleParameters[0], eleTag, *eleNodes)


        FstNode=SndNode
        
        if i==n-1 and EndPinned.upper()=='YES': #If second node is comatible on the last node

            Fstcoord=ops.nodeCoord(Nodei)
            lastcoord=ops.nodeCoord(Nodej)
            
            vecx=[lastcoord[0]-Fstcoord[0],lastcoord[1]-Fstcoord[1],lastcoord[2]-Fstcoord[2]] #Longitudinal Vector of the Element
            vecyp=[vecx[0],vecx[1]+0.1,vecx[2]]
            
            Sndcoord=ops.nodeCoord(SndNode)
            
            Newele=_getNewEleNum(Nodei,Nodej) # New element Tag
            
            ops.element('zeroLength', Newele, *[SndNode,Nodej],
                        '-mat', *[matTag,matTag,matTag],
                        '-dir', *[1,2,3],
                        '-orient', *vecx, *vecyp)



    return midtag, midcoord

