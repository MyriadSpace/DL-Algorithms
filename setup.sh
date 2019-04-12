# !/usr/bin/env bash
# Install virtualenv on local pc
echo passwd | sudo -S -u multi apt-get install virtualenv

# Install python3 in a directory named multicamp
virtualenv -p python3 ~/multicamp

# Activate "multicamp" virtualenv
sh "$HOME/multicamp/bin/activate"

# Install tensorflow, matplotlib, ipykernel, jupyter keras music21 gym readchar on the current virtualenv
$HOME/multicamp/bin/pip3 install --upgrade tensorflow matplotlib ipykernel jupyter keras music21 gym readchar

# Add python3 kernel to Jupyter
$HOME/multicamp/bin/python3 -m ipykernel install --user

# Run jupyternotebook server on local pc 
# cd lecture
# jupyter notebook
echo passwd | sudo -S -u multi apt-get install python3-tk

#-----------------------------------------------------#
# [Ref] Deactivate current virtualenv ("multicamp")
# On terminal, run "deactivate"
#-----------------------------------------------------#

#-----------------------------------------------------------------------------------------------#
# [Ref] When got dpkg error
#
# Problem) When installing packages with apt, got message like :
# E: Could not get lock /var/lib/dpkg/locUnpacking python3-tk (3.5.1-1) ...
# k - open (11: Resource temporarily unavailable)
# E: Unable to lock the administration directory (/var/lib/dpkg), is another process using it?
# E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
# E: Unable to lock directory /var/lib/apt/lists/
#
# Solution)
# 1. Find pid of apt processes
#   ps -A | grep apt
# 2. Kill apt processes by pid
#   sudo kill -9 "processnumber(pid number from 1.)"
# 3. Delete the lock files
#   sudo rm /var/lib/dpkg/lock
# 4. Reconfigure packages
#   sudo dpkg --configure -a
# 5. update packages
#   sudo apt update
#-----------------------------------------------------------------------------------------------#
