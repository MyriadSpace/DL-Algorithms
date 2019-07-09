import subprocess

cmd_list = [
    'sudo apt install virtualenv',
    'sudo apt install git',
    'sudo apt install python3-tk',
    'virtualenv -p python3 ~/multicamp',
    'source ~/multicamp/bin/activate',
    'pip3 install --upgrade tensorflow matplotlib ipykernel jupyter music21 gym',
    'python3 -m ipykernel install --user',
    'git clone https://github.com/aidentify/lecture',
]

for cmd in cmd_list:
    install_proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    while install_proc.poll() is None:
        out = install_proc.stdout.readline()
        print(out.decode('utf-8'), end='')
