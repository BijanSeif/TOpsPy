# TOpsPY

[![PyPI version fury.io](https://badge.fury.io/py/TOpsPy.svg)](https://pypi.python.org/pypi/topspy/)
[![Downloads](https://pepy.tech/badge/topspy)](https://pepy.tech/project/topspy)
[![Downloads](https://pepy.tech/badge/topspy/month)](https://pepy.tech/project/topspy)
[![Downloads](https://pepy.tech/badge/topspy/week)](https://pepy.tech/project/topspy)



**By: Bijan Sayyafzadeh (b.sayyaf@yahoo.com)**

This module conatin my functions for openseespy and you can find the doucumentation using shift+Tab key after their name.


### Packages and Functions that Are presented are here with their usage Description:


* **AutoModeler** (SubPackage)

* **TimeHistories** (SubPackage)

* **dynamic** (SubPackage)
   - **LAT2**   : Function for importing acceleration data from *.AT2 PEER Files.
   - **RspSpc** : Function for calculating Linear Response Spectrum for any Time History.
   - **SDFTHA** : Function for calculation the displacement response history of a SDF under any time history acceleration.
* **modeling** (SubPackage)
   - **ElePerPend**    : Function that Provide a vector that is perpendicular to the line from first defined point to the last defined point.
   - **eleAxialForce** : Function That return the Axial force of the defined element.
   - **MultiEl**       : Function That draw any number of elements alog defined nodes. This function also returns middle point/s NodeTag/s and their corresponding coordinates. There is an option that by this option User Can specify that end connection be pinned or fixed!    
   - **GmTVector**     : Function that return the Geometric Transformation Vector of any element using only one Parameter. For more information Review This: https://github.com/BijanSeif/My-Opensees-Jupyter-NoteBooks/blob/main/Auto%20Geometric%20Transform%20Function%20(GmTVector).ipynb


### How to use it:
1- Install it : **pip install topspy**     (for windows)\
2- In your python code import it:
- For dynamic subpackage: **import topspy.dynamic as bjd**
- For modelling subpackage: **import topspy.modeling as bjm**

3- Using **bjd** or **bjm** you have access to mentioned function.

### Example of using the functions:

* **AutoModeler** (SubPackage)

* **TimeHistories** (SubPackage)

* **dynamic** (SubPackage)
   - **LAT2**   : 
   - **RspSpc** : 
   - **SDFTHA** : 
* **modeling** (SubPackage)
   - **ElePerPend**    :  **bjm.ElePerPend(1,5)** Using Node Numbers (Node 1 and Node 5) , **bjm.ElePerPend(a,b)** Using Node Coordinate (a and b are the coordinate list of node 1 and node 5)
   - **eleAxialForce** :  **Axial1,Axial2=bjm.eleAxialForce(eleTag)** using element Tag number the axial force of the element is presented in  Axial1, Axial2.
   - **MultiEl**       :  **bjm.MultiEl(4,5,5,elep,0)** #Define 5 elements with elep properties from node 4 to node 5 with no buckling shape and in a direct line. **bjm.MultiEl(4,5,5,elep,0,'Yes',1e9,10)** The last **'Yes'** cause that generated element be 2 head pinned using zero length Element with Rigid Stiffness equal to 1e9 or any other user value with NewMaterialTag equal to 10!. **(ATTENTION: it is very important that user don't define any previously used tag for NewMaterialTag)**
   - **MultiElEQDOF**  : 
   - **GmTVector**     :  **vec=bjm.GmTVector(Node1,Node2,Theta)** Using Node Coordinate (Node1,Node2 are the coordinate list of node 1 and node 5) and Theta is the cross section rotation angle according degree and the result (vec) is the Geometric transformation vector.

Find more examples in detail: https://github.com/BijanSeif/My-Opensees-Jupyter-NoteBooks
