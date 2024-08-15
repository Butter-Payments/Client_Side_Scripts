cookies = {
    'OptanonAlertBoxClosed': '2024-08-13T14:40:07.567Z',
}

headers = {
    'accept': 'application/json, text/plain, */*',
}

base_url='ca-test.adyen.com'
report_generation_url=f'https://{base_url}/ca/ca/ui-api/reporting/v1/S3B-SDhuNiJcPVV8IzMjTX4yI1dFMSVuYEMqSw/reports/S3B-SDhuNiJcPVV8IzMjTX4yI1dFMSVuYEMqSw:queue'
list_all_downloads_url=f'https://{base_url}/ca/ca/ui-api/reporting/v1/S3B-SDhuNiJcPVV8IzMjTX4yI1dFMSVuYEMqSw/reports/S3B-SDhuNiJcPVV8IzMjTX4yI1dFMSVuYEMqSw/generated-reports',

number_of_days = 90 ##number of days to pull data for
end_date = '2024-08-13' ## last date to pull