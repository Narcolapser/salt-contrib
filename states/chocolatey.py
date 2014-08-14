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
    

def _find_chocolatey():
    '''
    Returns the full path to chocolatey.bat on the host. Direct copy from the chocolatey module.
    '''
    choc_defaults = ['C:\\Chocolatey\\bin\\chocolatey.bat',
                    'C:\\ProgramData\\Chocolatey\\bin\\chocolatey.exe', ]

    choc_path = __salt__['cmd.which']('chocolatey.exe')
    if not choc_path:
        for choc_dir in choc_defaults:
            if __salt__['cmd.has_exec'](choc_dir):
                choc_path = choc_dir

    return choc_path

def chocolatey(name, force=False):
    '''
    Bootstrap wrapper. Basically include this in your state and your minion will make sure that
    chocolatey is installed.
    '''
    choco_path = _find_chocolatey()

    if choco_path:
        ret = {'name': name,
            'result': True,
            'changes': {},
            'comment': 'Chocolatey already installed. found at: {0}'.format(choco_path)}
        return ret

    ret = {'name': name,
        'result': False,
        'changes': {},
        'comment': ''}

    try:
        result = __salt__['chocolatey.bootstrap'](force)

    except CommandExecutionError as CEE:
        ret['comment'] = 'Error while executing boot strap process: {0}'.format(str(CEE))
        return ret

    except ComandNotFoundError as CNFE:
        ret['comment'] = 'failed to find Power shell, or power shell was not installed'
        return ret

    if result != 0:
        ret['comment'] = 
            'honestly not entirely sure what went wrong. But you might find something here:\n{0}'.format(result['stderr'])
        return ret
    
    ret['comment'] = result['stdout']
    ret['result'] = True
    ret['changes'] = {'chocolatey':'bootstrapped'}
    return ret

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
