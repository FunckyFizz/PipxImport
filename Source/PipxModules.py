# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def PipxImport(mod):
    import os
    
    CL = os.getcwd() 
    
    os.chdir(os.path.expanduser("~") + '/.local/pipx/venvs/opencv-python/lib64/python3.8/site-packages') 
    
    mod = __import__(mod)
    
    os.chdir(CL)
    
    return mod