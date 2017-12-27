money=100
if money:
    print("택시를 타고 가라")
print("다왔다")
#else:
#   print("걸어 가라")


money=100
if money:
    print("택시를 타고 가라")
#print("다왔다")  -> #를 뺀다고 생각하면(틀린 문장으로 저장시 commit push 안 돼서)
else:
    print("걸어 가라")

# 뒤에  'else:'가 없으면 if문이랑 상관없이 print()앞에 공백이 없어도 독립적이 되기 때문에 실행 됨(에러x)
# 'else:'가 있을 때는, print() 앞에 공백이 없으면 에러