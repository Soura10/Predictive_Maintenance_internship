echo [$(date)]: "START"
echo [$(date)]: "Creating environment with python 3.8 version"
conda create --prefix ./rul python==3.8 -y
echo [$(date)]: "activating the environment"
source activate ./rul
echo [$(date)]: "installing the requirements"
pip install -r requirements.txt
echo [$(date)]: "END"