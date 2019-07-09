import subprocess

install_cmd_list = [
    'echo passwd | sudo -S apt -y install virtualenv',
    'echo passwd | sudo -S apt -y install git',
    'echo passwd | sudo -S apt -y install python3-tk',
    'virtualenv -p python3 /home/user/multicamp',
    'source /home/user/multicamp/bin/activate',
    'pip install --upgrade tensorflow matplotlib ipykernel jupyter music21 gym',
    'python3 -m ipykernel install --user',
    'git clone https://github.com/aidentify/lecture',
]

for install_cmd in install_cmd_list:
    install_proc = subprocess.Popen(install_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    while install_proc.poll() is None:
        out = install_proc.stdout.readline()
        print(out.decode('utf-8'), end='')
