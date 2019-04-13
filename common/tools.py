# -*- coding: utf-8 -*-
#######################
# common.tools
#######################

import os

def exec_cmd(command):
    if os.system(command)==0:
        return True
    else:
        return False
