import urllib.request as req

local = "mushroom.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)         ## urlretrieve(A, B) : url로 표기된 네트워크 객체를 지역파일로 가져오는 함수
print("OK")                         ## ↳ A(url)로 접근, 다운로드 후, B로 저장해라