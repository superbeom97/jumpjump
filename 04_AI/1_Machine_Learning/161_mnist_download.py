import urllib.request as req
import gzip, os, os.path

savepath = "./mnist"    ## (※) 여기서 '.'은 현재 디렉터리 // '..'는 상위 디렉터리 (※)
baseurl = "http://yann.lecun.com/exdb/mnist"
files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"]

## 다운로드
if not os.path.exists(savepath): os.mkdir(savepath)     ## os.path.exists() : 파일이 존재하는지
for f in files:
    url = baseurl + "/" + f
    loc = savepath + "/" + f
    print("download : ", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)   ## urlretrieve(A, B) : url로 표기된 네트워크 객체를 지역파일로 가져오는 함수
                                    ## ↳ A(url)로 접근, 다운로드 후, B로 저장해라

## GZip 압축 해제
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz", "")    ## 압축 해제 후, 저장할 이름 명명
    print("gzip : ", f)
    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("OK")


### (※) '.'은 현재 디렉터리 // '..'는 상위 디렉터리 (※)

## 1. 같은 디렉터리에 있는 파일에 접근할 경우
## /01_ML/161_MN.py(현재 위치)
##       / olpl.pmg     에 접근하고자 할 때
## ↳ './olpl.pmg'(이건 100%) 또는 'olpl.pmg'(이건 운영체제에 따라 될 수도, 안 될 수도)

## 2. 상위 디렉터리에 있는 다른 하위 디렉터리에 있는 파일에 접근할 경우
## /01_ML/161_MN.py(현재 위치)
## /Imaglist/olpl.pmg   에 접근하고자 할 때
## ↳ '../Imaglist/olpl.pmg'

## 3. 하위 디렉터리에 있는 파일에 접근할 경우
## /01_ML/161_MN.py(현재 위치)
##       /mnist/olpl.pmg
## ↳ './mnist/olpl.pmg'
