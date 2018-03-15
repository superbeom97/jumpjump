from sklearn import model_selection, svm, metrics
## CSV 파일을 읽어 들이고 가공하기 --- (※1)
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}
data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")
## 학습하기 --- (※2)
clf = svm.SVC()
clf.fit(data["images"], data["labels"])
## 예측하기 --- (※3)
predict = clf.predict(test["images"])
## 결과 확인하기 --- (※4)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)

"""
             precision    recall  f1-score   support

          0       0.87      0.93      0.90        42
          1       0.81      1.00      0.89        67
          2       0.84      0.69      0.76        55
          3       0.87      0.57      0.68        46
          4       0.76      0.75      0.75        55
          5       0.63      0.80      0.71        50
          6       0.97      0.67      0.79        43
          7       0.74      0.86      0.79        49
          8       0.91      0.72      0.81        40
          9       0.71      0.81      0.76        54

avg / total       0.80      0.79      0.79       501
"""
## recall : 재현율 - 다시 실행했을 때, precision이 그대로 재현될 확률
## precision = 0.87, recall = 0.93 -> 다시 실행했을 때, precision이 그대로 0.87 나올 확률이 0.93이다.