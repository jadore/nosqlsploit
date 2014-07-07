'''
Mst=>Update=>class
update!update!!
'''
from MstColor import *


seru = "http://mstoor.duapp.com/" #UPDATE SERVER HOST
nver = "20131026"                 #NOW VERSION


class update:
    '''mst update'''
    def start(self):
        '''.0.'''
        color.cprint("[*] UPDATE URL:",YELLOW)
        color.cprint("    MST::%s?do=download"%seru,CYAN)
        color.cprint("    PLU::%s"%seru,CYAN)


if __name__ == '__main__':
    print __doc__
else:
    update=update()
