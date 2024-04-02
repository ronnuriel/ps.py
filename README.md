# ps.py
ps.py is a cli that helps you manage python processes, find them, kill or restart.

### prerequisites:
Installed Python env </br>
Installed pip

To setup the ps command, it is recommended to add the containing directory to the PATH environment variable.

#### Then run:

pip install -r requirements.txt

### usage:</br>
ps.py --help </br>
ps.py (shows all running python processes)</br>
ps.py <process_name> --kill (kills running processes with the given name)</br>
ps.py <process_name> --restart (restarts all rinning processes with the given name)</br>
in case that name is not provided, the cli will perform the action on all running Python processes</br>

# How to install:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

pip install -e .
```

# Troubleshooting:
```bash
python3 -m pip install --upgrade pip
pip install -e .
```

# How to run:
```bash
newps --help
```
