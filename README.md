This script will allow us to mock an existing user browser session in Python. 

This is done by the following steps:

1. Have user log into Adyen with their own credentials
2. Once logged into Adyen, open the browser’s “dev tools”. The following screenshot shows 
    
    ![Screenshot 2024-08-14 at 10.19.04 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/fbd6cb23-eafe-441f-9603-96b66e9a30d4/Screenshot_2024-08-14_at_10.19.04_AM.png)
    
3. You will see dev tools either as a sidebar or new window
4. Select the “network” tab
    
    ![Screenshot 2024-08-14 at 10.21.07 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/df7e020e-109f-4767-a353-4a6b4545c731/Screenshot_2024-08-14_at_10.21.07_AM.png)
    
5. Once in network tab select the black / white circle icon (it will turn red) indicating it is recording:
    
    ![Screenshot 2024-08-14 at 10.21.43 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/d39390f0-e3e0-41af-89b7-baafd1652dde/Screenshot_2024-08-14_at_10.21.43_AM.png)
    
6. Select filter (indicated by the funnel icon)→ and check “Fetch/XHR” these are the network calls the website is using to load data
    
    ![Screenshot 2024-08-14 at 10.22.18 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/57c9e6d2-2fbf-471e-8f52-c5510eb68509/Screenshot_2024-08-14_at_10.22.18_AM.png)
    
7. Select any network call and right click “Copy as cURL”
    
    ![Screenshot 2024-08-14 at 10.23.11 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/aaacdbb7-eac0-4b41-94f6-ed8b92348539/Screenshot_2024-08-14_at_10.23.11_AM.png)
    
8. This will copy to your clipboard a copy of this network call
9. I like to use “https://curlconverter.com/” to convert a cURL command to Python:
    
    ![Screenshot 2024-08-14 at 10.25.29 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/163c660a-f19e-490a-b515-f5e15d14bd0f/Screenshot_2024-08-14_at_10.25.29_AM.png)
    
10. In the outputted Python copy ONLY the “cookies = {….}” and “header = {…}” content into ***“Session_Variables.py”***
    1. These values only contain details of your currently logged in web session. Things like a token (JSESSIONID) that validates your session is logged in, CompanyID for lookup, and details of the “browser” and site we are using.
11. Replace the cookie and header values with your own current values
    
    ![Screenshot 2024-08-14 at 10.26.56 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891746d-2b48-47bc-8992-9e2d9d18ce67/7bd49daa-507a-4a6a-bc5a-84bf1a36ad94/Screenshot_2024-08-14_at_10.26.56_AM.png)
    
12. Set the “number_of_days” we want to pull data for these manual reports
    1. Needs to be integer of how many days
13. Specify what the last day to generate for will be “end_date” - many clients enabled this report start on “some day” but data before this day will require manual generation.
14. Setup your base download url:
    1. To find base url for example:
    2. https://ca-test.adyen.com/ca/ca/overview/default.shtml
    3. Our base URL would be [ca-test.adyen.com](https://ca-test.adyen.com/ca/ca/overview/default.shtml)
15. These files were written w/ Python 3.10.13
16. Python 3.10.x should installed
    1. Mac:
        1. Ensure your system has Homebrew installed for package management. It can be found at [https://brew.sh](https://brew.sh/)
        2. Use the following homebrew command to install the Python version
            1. `brew install python@3.10`
        3. Modify your shell RC script (like `~/.zshrc`) by adding each of the following items on their own line:
            1. export PATH=/opt/homebrew/bin/python3.10:$PATH
            2. alias python="/opt/homebrew/bin/python3.10”
            3. alias pip="/opt/homebrew/bin/pip3.10”
        4. Close and re-open the terminal, which should make the previously set variables available use
            1. This can be confirmed by typing “which python”, and the terminal should return the above path to python (”/opt/homebrew/bin/python3.10”)
    2. PC
        1. The relevant version of python can be found at https://www.python.org/downloads/release/python-31011/
        2. Determine if you are running a 32-bit or a 64-bit architecture
        3. Select the appropriate package and install it
        4. Validate after installation completes by running “python” in your terminal
        
        <aside>
        💡 Python 3.10.13 (main, Aug 24 2023, 12:59:26) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>..
        
        </aside>
        
        1. Type “exit()” to quit.
17. Make sure any required dependencies are installed
    1. `pip install requests`
18. Run “python Adyen_Queue_Reports.py” by running `python Adyen_Queue_Reports.py` - first - 
    1. This will request Adyen to prepare the data 
    2. This can take some time for them to actually create data
    3. “Queued Failure”can mean no data available or already generated
19. Run “python Adyen_Download_Reports.py” second
    1. Will pull each available day between end_date and “number_of_days” before
20. Confirm that the downloads were successful by manually downloading one of the reports, and comparing it to the matching report found in the folder where script downloaded the bulk files.

Files required for Adyen:
- Session_Variables.py
    - This file contains variables (session, header) and date ranges to pull data for locally.
- Adyen_Queue_Reports.py
    - This report will act like an existing logged in session, and run the same API calls the website does to ask Adyen to manual generate reports for all the given days (end_date subtracting number of days)
- Adyen_Download_Reports.py
    - Once the above script has run, and queued all files, this will generate a list of all available files to download
    - All files will be downloaded in the same location as this script as CSV with format matching Adyens report.