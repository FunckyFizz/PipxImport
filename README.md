PipxImport

The intention of this project is to be able to install and use isolated modules, installed via pipx, in your projects. This means that setting up a virtual environment for every project is not necessary.

Pull requests welcome (and appreciated).

This module has only so far been tested on one computer running Pop!_OS linux (Ubuntu compatible).

To use this module put the file in the same directory as your script and type the command "from PipxImport import *"

Once this is done, you will be able to import any modules you have installed with pipx.

An example of how to do this where cv2 (opencv-python) has been pipx installed:

cv2 = cv2 = PipxImport('cv2')
