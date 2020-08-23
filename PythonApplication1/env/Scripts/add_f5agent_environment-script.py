#!"C:\Users\Akash Prasad\source\repos\PythonApplication1\PythonApplication1\env\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'f5-openstack-lbaasv2-driver==12.0.0','console_scripts','add_f5agent_environment'
__requires__ = 'f5-openstack-lbaasv2-driver==12.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('f5-openstack-lbaasv2-driver==12.0.0', 'console_scripts', 'add_f5agent_environment')()
    )
