def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 값이 아닙니다. 다시 혀라잉!!!")
        return
    else:
        result = sum(a, b)
    return result

if __name__ == "__main__":   # 여기(mod1)에서는 얘가 메인이야,, 근데 mod1_test에서 실행하면, mod1_test 입장에선
                            # mod1_test가 메인이 되는 거지. 그래서 mod1_test에서는 실행되지 않고 여기서만 실행되는 거야!
    print(sum(1,2))
    print(safe_sum(1, "hello"))