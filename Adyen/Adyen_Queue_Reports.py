import requests
from datetime import datetime, date, timedelta
from Session_Variables import cookies,headers,number_of_days,end_date,report_generation_url

def json_request(day_of_report:str) -> dict:
    post_request = {
    'parameters': {
    },
    'format': 'CSV',
    }
    post_request['parameters']['reportdate']=day_of_report
    return post_request

def queue_report_generation(json_data:dict) -> any :
    response = requests.post(
        report_generation_url,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response

def queue_all_reports(end_date:str, number_of_days:int):
    success_count=0
    failure_count=0
    end_date_obj=datetime.strptime(end_date,"%Y-%m-%d")
    start_date_delta = timedelta(days=number_of_days)
    start_date = end_date_obj - start_date_delta

    print('Start_date:' + start_date.strftime("%Y-%m-%d"))
    date_of_report=start_date
    delta = timedelta(days=1)
    while date_of_report <= end_date_obj:
        print("Queuing day: %s" %date_of_report)
        json_data = json_request(date_of_report.strftime("%Y-%m-%d"))
        response_code:int = queue_report_generation(json_data).status_code 
        if response_code==200 or response_code==204:
            success_count+=1
        else:
            failure_count+=1
        date_of_report += delta

    print("Queued Successes: %s" % success_count)
    print("Queued Failures: %s" % failure_count)


##
##
## This section will queue 'number_of_days' days of reports to be generated by Adyen
## This needs to be run first for data to be extracted.

start_date_delta = timedelta(days=number_of_days)
start_date = datetime.strptime(end_date,"%Y-%m-%d") - start_date_delta
queue_all_reports(end_date,number_of_days)

#If a day is not available OR already has a generated report you will get a failure
#Successes indicate new report queued
