import requests
from datetime import datetime, date, timedelta
from Session_Variables import cookies,headers,end_date,number_of_days,list_all_downloads_url

#Given a json {'startdate':'YYYY-MM-DD','enddate':'YYYY-MM-DD'}
def list_all_downloads(params:dict) -> any:
    response = requests.get(
       list_all_downloads_url,
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response

def get_file_download_links(file_list_resp:dict) -> list:
    download_array = []
    for item in download_list:
        file_dict={}
        file_dict['fileName']=item['fileName']
        file_dict['link']=item['links']['download']
        download_array.append(file_dict)
    return download_array


##Determine first date to download
start_date_delta = timedelta(days=number_of_days)
start_date = datetime.strptime(end_date,"%Y-%m-%d") - start_date_delta

##
##This section - after all the above reports have been created (can take time)
## Will query for all the available files and iterate through downloading them
##
params = {
    'startdate': start_date.strftime("%Y-%m-%d"),
    'enddate': end_date,
}


download_list=list_all_downloads(params).json()
print(params)
list_of_files=get_file_download_links(download_list)
print(list_of_files)
print("There are %s files to download" % len(list_of_files))

for file in list_of_files:
    download_params = {
    'includefailed': 'true',
    }
    response = requests.get(file['link'],
    params=params,
    cookies=cookies,
    headers=headers,
)
    print("Writing file: %s" %file['fileName'])
    file = open(file['fileName'], "w")
    file.write(response.text)
    file.close()
