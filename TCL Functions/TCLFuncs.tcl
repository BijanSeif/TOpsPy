# By Bijan Sayyafzadeh and Saeedeh Koohestany

proc ElePerPend  {Nodei Nodej} {
 
 set x1 [lindex [nodeCoord $Nodei] 0]
 set y1 [lindex [nodeCoord $Nodei] 1]
 set z1 [lindex [nodeCoord $Nodei] 2]
 set x2 [lindex [nodeCoord $Nodej] 0]
 set y2 [lindex [nodeCoord $Nodej] 1]
 set z2 [lindex [nodeCoord $Nodej] 2]
 
 set R1 [list [expr $x2-$x1] [expr $y2-$y1] [expr $z2-$z1]]

  if { [lindex $R1 0]==0 && [lindex $R1 1]==0 } {
	set R2 [list [lindex $R1 0] [expr [lindex $R1 1]+0.1] [lindex $R1 2]]
    } else {
	set R2 [list [lindex $R1 0] [lindex $R1 1] [expr [lindex $R1 2]+0.1]]
	}
	
 set R3 [VecProduct $R1 $R2]
 set R3 [Nrmlz $R3 1]
 return $R3
}

proc eleAxialForce {eleTag} {
   
  set Nodes [eleNodes $eleTag]

  set x1 [lindex [nodeCoord [lindex $Nodes 0]] 0]
  set y1 [lindex [nodeCoord [lindex $Nodes 0]] 1]
  set z1 [lindex [nodeCoord [lindex $Nodes 0]] 2]
  set x2 [lindex [nodeCoord [lindex $Nodes 1]] 0]
  set y2 [lindex [nodeCoord [lindex $Nodes 1]] 1]
  set z2 [lindex [nodeCoord [lindex $Nodes 1]] 2]
  
  set RM [expr (($x2-$x1)**2+($y2-$y1)**2+($z2-$z1)**2)**0.5]
  set R1 [list [expr ($x2-$x1)/$RM] [expr ($y2-$y1)/$RM] [expr ($z2-$z1)/$RM]]
  

  set elfor [eleForce $eleTag]
  set elefocesi [list [lindex $elfor 0] [lindex $elfor 1] [lindex $elfor 2]]
  set elefocesj [list [lindex $elfor 6] [lindex $elfor 7] [lindex $elfor 8]]

  set eleAxial1 [DotPrdct $elefocesi $R1]
  set eleAxial2 [DotPrdct $elefocesj $R1]

 # return [list $eleAxial1 $eleAxial2]
 return $eleAxial1
}
	
proc lremove {theList args} {
    # Special case for no arguments
    if {[llength $args] == 0} {
        return {}
    }
    # General case
    set path [lrange $args 0 end-1]
    set idx [lindex $args end]
    lset theList $path [lreplace [lindex $theList $path] $idx $idx]
}	
	
#MultiElement
proc getNewNodeNum {Nodei Nodej} {
 
 set Nodelist [getNodeTags]
 set cnt 0

 set Numb [format "%d" [format "%s" $Nodei][format "%s" $Nodej][format "%s" $cnt]]
 set check None
 while {$check != True} {
	if {$Numb in $Nodelist} { 
		set cnt [expr $cnt+1]
		set Numb [format "%d" [format "%s" $Nodei][format "%s" $Nodej][format "%s" $cnt]]
	} else {
		set check True
		return $Numb
	}	
 }
}
 
proc getNewEleNum {Nodei Nodej} {
 
 set EleList [getEleTags]
 set cnt 0
 set Numb [format "%d" [format "%s" $Nodei][format "%s" $Nodej][format "%s" $cnt]]
 set check None
 while {$check != True} {
	if {$Numb in $EleList} { 
		set cnt [expr $cnt+1]
		set Numb [format "%d" [format "%s" $Nodei][format "%s" $Nodej][format "%s" $cnt]]
	} else {
		set check True
	    return $Numb	
	}
 }
}
	
proc MultiEl  {Nodei Nodej Number_Of_Elements EleParameters MidCurveDisp EndPinned E NewMaterialTag} {
  set matTag 2
  set n $Number_Of_Elements
  #Parameters For end Pinned Material--------  
  # if {[string toupper $EndPinned] == YES} {
    # set matTag $NewMaterialTag
	# }
         # try:
		   # #if code encounter with error means this material has been defined previously
           # uniaxialMaterial Elastic $matTag $E   
         # except:
            # pass
#Check We will have One middle point or two and Curve Factor-----------------------------------------------
set pi 3.14159265359
set midtag []
set midcoord []
 
 if { $n%2 == 0 } { 
  #tag of element that it's 2ndNode is the middle
		set elemtag [expr $n/2-1]
	for {set i 1} {$i < (($n/2)+1)} {incr i 1} {
		lappend fact [expr sin ($i/($n/2)* $pi/2)* $MidCurveDisp]
	}
		set fact "$fact  [lreverse [lrange $fact 0 end-1]]"
	for {set i 0} {$i < [llength $fact] } {incr i 1} {
		lappend fact3 [expr [lindex $fact $i+1]-[lindex $fact $i]]
	}
		set fact "[lindex $fact 0]  $fact3" 

 } else { 
		set elemtag [list [expr ($n-1)/2-1] [expr ($n-1)/2]]
	for {set i 1} {$i <= ((($n-1)/2)+1)} {incr i 1} {
		lappend fact [expr sin ($i/(($n-1)/2)* $pi/2)* $MidCurveDisp]
	}
		set fact "$fact [lreverse $fact] "
		set fact3 []
	for {set i 0} {$i < [expr [llength $fact]-1] } {incr i 1} {
		lappend fact3 [expr [lindex $fact $i+1]-[lindex $fact $i]]
	}
		set fact "[lindex $fact 0]  $fact3" 
   } 


  set NPV [ElePerPend $Nodei $Nodej]
  set NodeiC [nodeCoord $Nodei]
  set NodejC [nodeCoord $Nodej]

  lassign $NodeiC x1 y1 z1
  lassign $NodejC x2 y2 z2
  
  set Lxi [expr ($x2-$x1)/$n]
  set Lyi [expr ($y2-$y1)/$n]
  set Lzi [expr ($z2-$z1)/$n]
  
 #First Node Tag
 set  FstNode $Nodei
 #First zerolength Element
 if {[string toupper $EndPinned] == YES} {
	set Fstcoord [nodeCoord $Nodei]
	set lastcoord [nodeCoord $Nodej] 
	set vecx [list [expr [lindex  $lastcoord 0]-[lindex  $Fstcoord 0]] [expr [lindex  $lastcoord 1]-[lindex  $Fstcoord 1]] [expr [lindex  $lastcoord 2]-[lindex  $Fstcoord 2]]]

		if {[lindex  $vecx 0]==0 && [lindex  $vecx 2]==0 } {
			set vecyp [list [expr [lindex  $vecx 0] + 0.1] [lindex  $vecx 1] [lindex  $vecx 2]]
		} else {
			set vecyp [list [lindex  $vecx 0] [expr [lindex  $vecx 1] + 0.1] [lindex  $vecx 2]]
		}
		set FstNode [getNewNodeNum $Nodei $Nodej]
		node $FstNode [lindex $Fstcoord 0]  [lindex $Fstcoord 1] [lindex $Fstcoord 2]
		set Newele [getNewEleNum $Nodei $Nodej]
		element zeroLength $Newele $Nodei $FstNode -mat $matTag $matTag $matTag $matTag -dir 1 2 3 4 -orient  [lindex  $vecx 0] [lindex  $vecx 1] [lindex  $vecx 2] [lindex  $vecyp 0] [lindex  $vecyp 1] [lindex  $vecyp 2]
  }

 # --- Generating Nodes and Elements---------------------
 for {set i 0} { $i < $n} {incr i 1} {
		 set Fact [lindex $fact $i]
		 set Fstcoord [nodeCoord $FstNode] 
		 set Sndcoord [list [expr [lindex  $Fstcoord 0]+$Lxi] [expr [lindex  $Fstcoord 1]+$Lyi] [expr [lindex  $Fstcoord 2]+$Lzi]] 
		 
		 set Sndcoord [list [expr [lindex $Sndcoord 0]+ $Fact *[lindex $NPV 0]] [expr [lindex $Sndcoord 1]+ $Fact *[lindex $NPV 1]] [expr [lindex $Sndcoord 2]+ $Fact *[lindex $NPV 2]]]
		 
    if {$i == $n-1 && [string toupper $EndPinned] != YES} {
         set SndNode $Nodej
		 set Sndcoord [nodeCoord $SndNode]

	} else {                            
         set SndNode [getNewNodeNum $Nodei $Nodej]
         node $SndNode [lindex $Sndcoord 0]  [lindex $Sndcoord 1] [lindex $Sndcoord 2]

	} 
	if {$i in $elemtag} {
		lappend midtag $SndNode
		lappend midcoord $Sndcoord
	}		
     
		set Newele [getNewEleNum $Nodei $Nodej] 
		set eleTag $Newele
        set eleNodes [list $FstNode $SndNode]
		#set EleParameters [list elasticBeamColumn $eleTag $FstNode $SndNode 1000. 1000000. 100000000. 10000000. 10000000. 10000000. 1]

		element [lindex $EleParameters 0] $eleTag [lindex $eleNodes 0] [lindex $eleNodes 1] [lindex $EleParameters 4] [lindex $EleParameters 5] [lindex $EleParameters 6] [lindex $EleParameters 7] [lindex $EleParameters 8] [lindex $EleParameters 9] [lindex $EleParameters 10]
		

	 set FstNode $SndNode

  
  
 #Last Zero Length Element---------------------------------------------------------------
 
 if {$i==$n-1 && [string toupper $EndPinned] == YES} {
	set Fstcoord [nodeCoord $Nodei]  
	 set lastcoord [nodeCoord $Nodej]
	 set vecx [list [expr [lindex  $lastcoord 0]-[lindex  $Fstcoord 0]] [expr [lindex  $lastcoord 1]-[lindex  $Fstcoord 1]] [expr [lindex  $lastcoord 2]-[lindex  $Fstcoord 2]]]
		if {[lindex  $vecx 0]==0 && [lindex  $vecx 2]==0 } {
			 set vecyp [list [expr [lindex  $vecx 0] + 0.1] [lindex  $vecx 1] [lindex  $vecx 2]]
		 } else {
			 set vecyp [list [lindex  $vecx 0] [expr [lindex  $vecx 1] + 0.1] [lindex  $vecx 2]]
		 }
		 set Sndcoord [nodeCoord $SndNode]
		 set Newele [getNewEleNum $Nodei $Nodej]
		 element zeroLength $Newele $SndNode $Nodej -mat $matTag $matTag $matTag -dir 1 2 3 -orient  [lindex  $vecx 0] [lindex  $vecx 1] [lindex  $vecx 2] [lindex  $vecyp 0] [lindex  $vecyp 1] [lindex  $vecyp 2]
	}
   }
   
 return "$midtag $midcoord"

 }
 
 
 proc eledisp {Nodei Nodej} {

  set NodeiC [nodeCoord $Nodei]
  set NodejC [nodeCoord $Nodej]

  lassign $NodeiC Cx1 Cy1 Cz1
  lassign $NodejC Cx2 Cy2 Cz2
  
  set NodeiD [nodeDisp $Nodei]
  set NodejD [nodeDisp $Nodej]
  
  lassign $NodeiD Dx1 Dy1 Dz1
  lassign $NodejD Dx2 Dy2 Dz2
  
  set Lxi [expr ($Cx1+$Dx1)]
  set Lyi [expr ($Cy1+$Dy1)]
  set Lzi [expr ($Cz1+$Dz1)]
  
  set Lxj [expr ($Cx2+$Dx2)]
  set Lyj [expr ($Cy2+$Dy2)]
  set Lzj [expr ($Cz2+$Dz2)]
  
  set L1 [expr ((($Lxj-$Lxi)**2)+(($Lyj-$Lyi)**2)+(($Lzj-$Lzi)**2))**0.5 ]
  set L0 [expr ((($Cx2-$Cx1)**2)+(($Cy2-$Cy1)**2)+(($Cz2-$Cz1)**2))**0.5 ]
  set Disp [expr ($L1-$L0)]
  
  return $Disp
  }