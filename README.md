# ps.py
ps.py is a cli that helps you manage python processes, find them, kill or restart.

prerequisites:
Installed Python env
Installed pip

To setup the ps command, it is recommended to add the containing directory to the PATH environment variable.

Then run:

pip install -r requirements.txt

usage:
ps.py --help
ps.py (shows all running python processes)
ps.py <process_name> --kill (kills running processes with the given name)
ps.py <process_name> --restart (restarts all rinning processes with the given name)
in case that name is not provided, the cli will perform the action on all running Python processes
