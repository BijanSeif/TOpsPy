# By Bijan Sayyafzadeh and Saeedeh Koohestany

proc VecProduct  {v1 v2} {
 
 set v1x  [lindex $v1 0]
 set v1y  [lindex $v1 1]
 set v1z  [lindex $v1 2]
 set v2x  [lindex $v2 0]
 set v2y  [lindex $v2 1]
 set v2z  [lindex $v2 2]
 set vec  [list [expr $v1y*$v2z-$v1z*$v2y] [expr $v1z*$v2x-$v1x*$v2z] [expr $v1x*$v2y-$v1y*$v2x]]
 return $vec
}


proc DotPrdct  {v1 v2} {
 
 set v1x [lindex $v1 0]
 set v1y [lindex $v1 1]
 set v1z [lindex $v1 2]
 set v2x [lindex $v2 0]
 set v2y [lindex $v2 1]
 set v2z [lindex $v2 2]

 return  [expr ($v1x*$v2x+$v1y*$v2y+$v1z*$v2z)]
}



proc Nrmlz  {V a} {

 set V0 [lindex $V 0]
 set V1 [lindex $V 1]
 set V2 [lindex $V 2]
 
 set A [expr (($V0**2+$V1**2+$V2**2)**0.5)]
 set V [list [expr ($V0/$A*$a)] [expr ($V1/$A*$a)] [expr ($V2/$A*$a)]] 
 return $V
}


proc VecSize {V} {
 #Return a vector size
 set V0 [lindex $V 0]
 set V1 [lindex $V 1]
 set V2 [lindex $V 2]
 
 set V [expr (($V0**2+$V1**2+$V2**2)**0.5)]
 return $V
}

proc GmTVector {FirstNode SecondNode Theta } {

    #--------------------------Finding main Vectors -------------------

	#Initial Data
	set x1 [lindex [nodeCoord $FirstNode] 0]
	set y1 [lindex [nodeCoord $FirstNode] 1]
	set z1 [lindex [nodeCoord $FirstNode] 2]
	set x2 [lindex [nodeCoord $SecondNode] 0]
	set y2 [lindex [nodeCoord $SecondNode] 1]
	set z2 [lindex [nodeCoord $SecondNode] 2]
	
    set theta [expr $Theta-180]
	 
    #V1 is the Main element
    set V1 [list  [expr ($x2-$x1)] [expr ($y2-$y1)] [expr ($z2-$z1)]]
    #V2 is a vector that is located in Perpendicular plane
    set z2 [expr $z2+0.1]
	
	if {$x1==$x2 && $y1==$y2 } {
    set z2 $z1
    set x2 $x1
    set y2 [expr $y1-0.1]
	}
    set V2 [list  [expr ($x2-$x1)] [expr ($y2-$y1)] [expr ($z2-$z1)]]
	
	set VN [VecProduct $V1 $V2]
	set pi 3.14159265359
	set theta [expr -$theta*$pi/180 ]
	set c [expr cos($theta)]
    set s [expr sin($theta)]
	
	set ux [expr [lindex $V1 0]/[VecSize $V1]]
	set uy [expr [lindex $V1 1]/[VecSize $V1]]
	set uz [expr [lindex $V1 2]/[VecSize $V1]]
	
    set VR [list [expr ($c+$ux**2*(1-$c))*[lindex $VN 0]+($ux*$uy*(1-$c)-$uz*$s)*[lindex $VN 1]+($ux*$uz*(1-$c)+$uy*$s)*[lindex $VN 2]] [expr ($uy*$ux*(1-$c)+$uz*$s)*[lindex $VN 0]+($c+$uy**2*(1-$c))*[lindex $VN 1]+($uy*$uz*(1-$c)-$ux*$s)*[lindex $VN 2]] [expr ($uz*$ux*(1-$c)-$uy*$s)*[lindex $VN 0]+($uz*$uy*(1-$c)+$ux*$s)*[lindex $VN 1]+($c+$uz**2*(1-$c))*[lindex $VN 2]]]

    set VR [Nrmlz $VR 1]
    set VN [Nrmlz $VN 1]
    #--------------- Calculation Of Geometric Transform ---------------------
    
    set VRsize [VecSize $VR]
    set GeomTrans [list [expr [lindex $VR 0]/$VRsize] [expr [lindex $VR 1]/$VRsize] [expr [lindex $VR 2]/$VRsize]]

    return $GeomTrans
 }
	