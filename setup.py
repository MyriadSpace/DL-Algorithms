import subprocess

dpkg_cmd_list = [
    'echo "passwd" | sudo -S rm /var/lib/dpkg/lock;',
    'echo "passwd" | sudo -S dpkg --configure -a;',
    'echo "passwd" | sudo -S apt update;'
]
dpkg_cmd = ''.join(dpkg_cmd_list)
dpkg_proc = subprocess.Popen(dpkg_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
while dpkg_proc.poll() is None:
    out = dpkg_proc.stdout.readline()
    print(out.decode('utf-8'), end='')

install_cmd_list = [
    'echo "passwd" | sudo -S apt -y install virtualenv git python3-tk;',
    'virtualenv -p python3 /home/user/multicamp;',
    '/home/user/multicamp/bin/activate;',
    'pip install --upgrade tensorflow matplotlib ipykernel jupyter music21 gym;',
    'python3 -m ipykernel install --user;',
    'git clone https://github.com/aidentify/lecture;',
]
install_cmd = ''.join(install_cmd_list)
install_proc = subprocess.Popen(install_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
while install_proc.poll() is None:
    out = install_proc.stdout.readline()
    print(out.decode('utf-8'), end='')
