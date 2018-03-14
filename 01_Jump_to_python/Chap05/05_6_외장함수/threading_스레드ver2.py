import threading
import time

class MyTread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg # 인자로 들어온 msg를 MyTread의 멤버 변수로 할당하는
        self.daemon = True # daemon = True로 설정하지 않으면(False로 하거나 아예 적지 않으면)
                          # 메인 프로그램이 종료되어도 스레드는 계속 실행된다.

    def run(self): # run이 아닌 다른 이름으로 설정하면 스레드는 작동하지 않고 메인 프로그램만 실행된다.
        while True:
            time.sleep(1)
            print(self.msg)

for msg in ['you', 'need', 'python']:
    t = MyTread(msg)
    t.start() # t.start()를 입력하면 run이 호출되는

for i in range(100):
    time.sleep(0.1)
    print(i)