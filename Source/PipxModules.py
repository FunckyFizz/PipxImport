def PipxImport(mod):
    import os
    
    CL = os.getcwd() 
    
    if os.name == 'nt':
        os.chdir(os.path.expanduser("~") + r'\.local\pipx\venvs\opencv-python\Lib\site-packages') 
    else:
        os.chdir(os.path.expanduser("~") + '/.local/pipx/venvs/opencv-python/lib64/python3.8/site-packages') 
    
    mod = __import__(mod)
    
    os.chdir(CL)
    
    return mod
