import urllib.request
import json


service_ID = "16a84e54cca04421bbbd9e0d4d032e8f"
pindex = "1"
psize = "50"
type = "json"

# end_point = "http://data.daegu.go.kr/hub/foodally"
#
# parameters = "?KEY=" + service_ID
# parameters += "&pIndex=" + pindex
# parameters += "&pSize=" + psize
# parameters += "&Type=" + type
#
# url = end_point + parameters

url = "http://data.daegu.go.kr/UndergroundWaterConstruct?KEY=16a84e54cca04421bbbd9e0d4d032e8f&pIndex=1&pSize=50&SIGUN_CD=41310"

req = urllib.request.Request(url)


try:
    print("응답을 기다리자!!")
    response = urllib.request.urlopen(req)
    print("응답을 받았다아아아아아아~~~")
    if response.getcode() == 200:
        jsonResult = json.loads(response.read().decode('utf-8'))

    with open('Daegu_Restaurant_Info', 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
        print('Daegu_Restaurant_Info.json SAVED')

except Exception as e:
    print(e)