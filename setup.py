import subprocess


dellock_proc = subprocess.Popen('echo "passwd" | sudo -S rm /var/lib/dpkg/lock', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
while dellock_proc.poll() is None:
    out = dellock_proc.stdout.readline()
    print(out.decode('utf-8'), end='')

reconf_proc = subprocess.Popen('echo "passwd" | sudo -S dpkg --configure -a', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
while reconf_proc.poll() is None:
    out = reconf_proc.stdout.readline()
    print(out.decode('utf-8'), end='')

update_proc = subprocess.Popen('echo "passwd" | sudo -S apt update', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
while update_proc.poll() is None:
    out = update_proc.stdout.readline()
    print(out.decode('utf-8'), end='')


install_cmd_list = [
    'echo "passwd" | sudo -S apt -y install virtualenv',
    'echo "passwd" | sudo -S apt -y install git',
    'echo "passwd" | sudo -S apt -y install python3-tk',
    'virtualenv -p python3 /home/user/multicamp',
    '/home/user/multicamp/bin/activate',
    'pip install --upgrade tensorflow matplotlib ipykernel jupyter music21 gym',
    'python3 -m ipykernel install --user',
    'git clone https://github.com/aidentify/lecture',
]

for install_cmd in install_cmd_list:
    install_proc = subprocess.Popen(install_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    while install_proc.poll() is None:
        out = install_proc.stdout.readline()
        print(out.decode('utf-8'), end='')
