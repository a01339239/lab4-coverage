#!/bin/bash

# Clone or get repo
if [ -d "./lab4-coverage" ] 
then 
    echo "Repo already exists."
else 
    echo "Cloning repo."
    git clone https://github.com/a01339239/lab4-coverage.git
fi

# Verify python3 and pip3 is installed
if which python3 > /dev/null 2>&1
then
    echo "Python3 is installed."
else
    echo "Python3 is not installed. Exiting."
    exit 1
fi

if which pip3 > /dev/null 2>&1
then
    echo "Pip3 is installed."
else 
    echo "Pip3 is not installed. Exiting."
    exit 1
fi

# Create venv and install dependencies
if python3 -m venv venv > /dev/null 2>&1
then 
    echo "Virtual env created."
else
    echo "Virtual env is not installed. Exiting."
    exit 1
fi
source ./venv/bin/activate

if [ -f "./lab4-coverage/reqs.txt" ]
then 
    echo "Reqs file found! Installing dependencies."
    pip3 install -r ./lab4-coverage/reqs.txt
else 
    echo "No reqs file found."
fi

#  Install and run prospector
if pip3 install prospector > /dev/null 2>&1 
then
    echo "Prospector installed."
else 
    echo "Prospector failed to be installed. Exiting."
    exit 1
fi

echo "Running prospector."
prospector ./lab4-coverage -o text:report.txt

echo "Report of results. Stored in report.txt."
cat report.txt

exit 0
