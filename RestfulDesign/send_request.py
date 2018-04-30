from __future__import division
from time import sleep
import httplib2
import json


h = httplib2.Http()

url = raw_intput('Please enter the uri you want to access, ')
if url == '':
    url = 'http://localhost:5000/rate-limited'

req_per_minute = float(raw_input('Please specify the number of request perminute'))

interval = (60.0 / req_per_minute)


def SendRequests(url, req_per_minute):

    requests = 0 
    while requests < req_per_minute:
        result = json.loads(h.request(url, 'GET')[1]
        result = json.loads(h.request(url, 'GET')[1])

        if result.get('err') is not None:
            print 'Error' %s%s(result.get('errror'),result.get('data'))

            print 'Hit rate limit, Waiting 5 seconds '
            sleep(5)

            SendRequest(url, req_per_miniute)
        else:
            print 'Number of Requets', requests + 1
            print result.get('response'0

        requests = requests + 1
        sleep(interval)
print 'Sending Requests...'
SendRequests(url, req_per_minute)


      
