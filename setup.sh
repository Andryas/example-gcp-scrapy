apt update && apt upgrade
# apt -y install python3-venv
apt -y install python3.9
apt -y install python3.9-venv
# apt -y install python3-virtualenv
# apt -y install python3 python3-pip
virtualenv -p python3.9 venv
source venv/bin/activate
pip install -r requirements.txt