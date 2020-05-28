def PipxImport(ImportName,*InstallName):
    import os
    
    CL = os.getcwd()
    
    FolderName = ImportName
    
    i = 0    
    for arg in InstallName:
        if i == 0:
            FolderName = arg
        else:
            break
        i = i + 1
    
    if os.name == 'nt':
        os.chdir(os.path.expanduser("~") + '\\.local\\pipx\\venvs\\' + FolderName + '\\Lib\\site-packages') 
    else:
        os.chdir(os.path.expanduser("~") + '/.local/pipx/venvs/' + FolderName + '/lib64/python3.8/site-packages') 
    
    ImportName = __import__(ImportName)
    
    os.chdir(CL)
    
    return ImportName
