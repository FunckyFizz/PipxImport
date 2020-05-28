# PipxImport


The intention of this project is to be able to install and use isolated modules, installed via pipx, in your projects. This means that setting up a virtual environment for every project is not necessary.

Pull requests welcome (and appreciated).

This module is cross compatible with both Linux and Windows but has only been tested on one machine for each OS.

To use this module put the file in the same directory as your script and type the command  `from PipxImport import *`

Once this is done, you will be able to import any modules you have installed with pipx.<br/><br/>


An example of how to do this where Automagica has been pipx installed:

automagica = PipxImport('automagica')<br/><br/>


Here is an example of how to import a "pipxed" module where the install name is differnt to the import name (OpenCV):

cv2 = PipxImport('cv2', 'opencv-python')
