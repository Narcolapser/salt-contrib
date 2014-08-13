# -*- coding: utf-8 -*-
'''
Manage packages for windows through the use of Chocolatey. Hopefully some day this will be able
to replace win_pkg.
'''
def __virtual__():
    '''
    Load this state if the reg module exists
    '''
    return 'chocolatey' if 'chocolatey.install' in __salt__ else False
    

def chocolatey(name, present=True):
    '''
    Bootstrap wrapper. Basically include this in your state and your minion will make sure that
    chocolatey is installed.
    '''
    pass

def install(name, version=None, source=None, force=False):
    '''
    this method not only install software, but it also wraps the update process. If no version is
    specified it will automatically assume the most recent version. In which case it will do its
    best to keep software up to date. if a version is specified then it will not do updates 
    automatically.
    '''
    pass

def windows_features(name, enabled=False):
    '''
    this method takes a windows feature named and toggles it between enabled or disabled.
    '''
    pass

def remove(name, version=None):
    '''
    this method ensures that certain packages are not installed. this can be useful for ensuring 
    that legally questionable software like "YAR-PIRACY-FTW!" or security hazards are removed.
    '''
    pass
