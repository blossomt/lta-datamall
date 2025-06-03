import os
from requests import get
from csv import DictWriter
from datetime import date 

key = os.environ['ACCOUNTKEY']
method = 'GET'
headers = { 'AccountKey' : key,
            'accept' : 'application/json'}

#Get all data when API limits to 500 rows
def get_all_data(base_uri,output_file):
    end = False
    n = 0
    result_arr = []
    while end == False:
        uri = base_uri+"?$skip="+str(n)
        response = get(uri, headers=headers)
        if response.status_code == 200:
#             print("Getting rows "+str(n)+"+...")
            jsonObj = response.json()
            nrow = len(jsonObj['value'])
            result_arr.extend(jsonObj['value'])
            if nrow < 500:
                end = True
            n += nrow
        else:
            print("Failed to request with error "+str(response.status_code))
            end = True
    #Write list
    with open(output_file,'w',encoding='utf-8') as f:
        title = [*result_arr[0].keys()]
        cw = DictWriter(f,title,delimiter=",")
        cw.writeheader()
        cw.writerows(result_arr)
    print("Total rows: "+str(n))

today = date.today().strftime("%Y%m%d")

#Bus service
bus_svc_uri = "https://datamall2.mytransport.sg/ltaodataservice/BusServices"
#Bus route
bus_route_uri = "https://datamall2.mytransport.sg/ltaodataservice/BusRoutes"
#Bus stop coordinates
bus_stop_uri = "https://datamall2.mytransport.sg/ltaodataservice/BusStops"

print(today)
get_all_data(bus_stop_uri,os.path.join('output',today+'bus_stop.csv'))
get_all_data(bus_svc_uri,os.path.join('output',today+'bus_service.csv'))
get_all_data(bus_route_uri,os.path.join('output',today+'bus_route.csv'))
