# elios-take-home
Take home project for Elios Technology


## Running
1. Clone repo: git clone git@github.com:jalexanderbryant/elios-take-home.git elios-demo
2. cd into elios-demo
3. (optional) Create and activate a python virtual environment
4. Install Requirements:  pip install -r requirements.txt
5. Setup database: python database.py
6. Parse Data and populate database: python parse_data.py
7. Start Flask Server: ./deploy.sh
8. Start React App:
** Open a new terminal
** cd elios_app/client
** install requirements: npm install 
** start front end server (if prompted, enter 'y' to start app on another port): npm start
** Open browser and navigate to: localhost:3001/
