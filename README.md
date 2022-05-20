"# fly_company" 

Welcome to this project, a platform that simulates the purchasing airline tickets and subsequently saving them in a blockchain.
Tools used: Python, Django, MongoDB, Truffle, Solidity.

Requirements to be installed: Python(i used 3.10.2), MongoDB, Node.js(last version), Truffle(installed via "npm install -g truffle"), Ganache (installed via "npm install -g ganache").



Steps for run the project (Windows):


- download the project

- open the console inside the folder "fly_company-main"

- create a virtual environment -> "python -m venv myvenv"

- run the virtual environment -> "myvenv\Scripts\activate"

- install requirements.txt -> "pip install -r requirements.txt"

- "python manage.py makemigrations"

- "python manage.py migrate"

- "python manage.py makemigrations app"

- "python manage.py migrate app"



Run the blockchain:

- open the console inside the folder "smart_contract";

- run the chain with "truffle develop";

- deploy the contract with "migrate";

- (optional)launch automatic tests "test"




- run the project -> "python manage.py runserver"

