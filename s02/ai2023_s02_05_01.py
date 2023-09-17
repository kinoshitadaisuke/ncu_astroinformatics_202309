#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 14:37:49 (CST) daisuke>
#

# importing shutil module
import shutil

# finding the location of executable "sh"
location_sh = shutil.which ('sh')

# printing location of executable "sh"
print (f'location of command "sh"         = "{location_sh}"')

# finding the location of executable "xterm"
location_xterm = shutil.which ('xterm')

# printing location of executable "xterm"
print (f'location of command "xterm"      = "{location_xterm}"')

# finding the location of executable "emacs"
location_emacs = shutil.which ('emacs')

# printing location of executable "emacs"
print (f'location of command "emacs"      = "{location_emacs}"')

# finding the location of executable "python3.10"
location_python310 = shutil.which ('python3.10')

# printing location of executable "python3.10"
print (f'location of command "python3.10" = "{location_python310}"')
