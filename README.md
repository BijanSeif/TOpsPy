# TOpsPY

**By: Bijan Sayyafzadeh (b.sayyaf@yahoo.com)**

This module conatin my functions for openseespy and you can find the doucumentation using shift+Tab key after their name.

Special Thanks to **Dr. Silivia Mazzoni & Prof. Michael Scott** Because of many guidances on my efforts\
And\
Also So many thanks to **Ph. D. Candidate Selamawit Dires** for her supports.

### Packages and Functions that Are presented are here with their usage Description:

* **dynamic** (SubPackage)
   - **LAT2**   : Function for importing acceleration data from *.AT2 PEER Files.
   - **RspSpc** : Function for calculating Linear Response Spectrum for any Time History.
   - **SDFTHA** : Function for calculation the displacement response history of a SDF under any time history acceleration.
* **modeling** (SubPackage)
   - **ElePerPend**    : Function that Provide a vector that is perpendicular to the line from first defined point to the last defined point.
   - **eleAxialForce** : Function That return the Axial force of the defined element.
   - **GmTVector**     : Function that return the Geometric Transformation Vector of any element using only one Parameter. For more information Review This: https://github.com/BijanSeif/My-Opensees-Jupyter-NoteBooks/blob/main/Auto%20Geometric%20Transform%20Function%20(GmTVector).ipynb


### How to use it:
1- Install it : **pip install topspy**     (for windows)\
2- In your python code import it:
- For dynamic subpackage: **import topspy.dynamic as bjd**
- For modelling subpackage: **import topspy.modeling as bjm**

3- Using **bjd** or **bjm** you have access to mentioned function.

### Example of using the functions:
* **dynamic** (SubPackage)
   - **LAT2**   : 
   - **RspSpc** : 
   - **SDFTHA** : 
* **modeling** (SubPackage)
   - **ElePerPend**    : 
   - **eleAxialForce** : 
   - **GmTVector**     : 
