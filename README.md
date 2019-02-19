# elios-take-home
Take home project for Elios Technology


## Running
Note: Steps 5 and 6 can be skipped; App already points to a Postgres database with AWS RDS.
1. Clone repo: git clone git@github.com:jalexanderbryant/elios-take-home.git elios-demo
2. cd into elios-demo
3. (optional) Create and activate a python virtual environment
4. Install Requirements:  pip install -r requirements.txt
5. Setup database: python database.py
6. Parse Data and populate database: python parse_data.py
7. Start Flask Server: ./deploy.sh
8. Start React App:
** Open a new terminal window
** cd elios_app/client
** install requirements: npm install 
** start front end server (if prompted, enter 'y' to start app on another port): npm start
** Open browser and navigate to: localhost:3001/

## Scoring Description
Equation: Risk = SUM( S*W(points in category) )
S = Severity
W = Weight (for category)

### Categories Factored into Score:
Social Media Accounts - 1 point/account
Email - 1 point/account
Phone - 1 point/account
Criminal Record - 2 points/offense if case was resulted in a Guilty verdict. 1 point otherwise
Civil Suits - 2 points/offense if case resulted in judgement against employee ("Judgment entered on Consent"). 1 point/offense if discharged, dismissed, or transferred.
Properties - 1 point/property
Addresses - 1 point/address

### Weights per Category
Social Media - 0.1
Email - 0.1
Phone - 0.025
Criminal Record = 0.4
Civil - 0.3
Properties - 0.05
Addresses - 0.025

### Severity by Category
Social Media - Medium
Emails - Medium
Phone - Low
Criminal Record - Very High
Civil Suits - High
Properties - Low
Addresses - Low
