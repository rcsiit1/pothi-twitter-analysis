# Pothi Twitter Analysis

## Prerequistics
* Python 3.5+
* Virtualenv

## Installation

1. Clone the project on you r local machine
2. Add the necessary credentials to access the twitter api in **generate-report.py**
    ```bash
        APP_KEY = ''
        APP_SECRET = ''
        access_token= ''
        access_token_secret =''
    ``` 
3. Navigate to the project folder and activate the virtualenv
    ```bash
        cd pothi-twitter-analysis
        source bin/activate
    ```
4. Install all the dependencies by executing the following command
    ```bash
        pip3 install -r requirements.txt
    ```
5. Run the script and enter the search term to see the output tweet text
    ```bash
        python3 generate-report.py
    ```

