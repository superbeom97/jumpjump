pocket=['paper','money','cellphone']
if 'money' in pocket:
    pass
    print("택시를 타고 가라")
else:
    pass


pocket=['paper','cellphone']
card=1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")


pocket=['paper','cellphone']
card=1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


pocket=['paper','cellphone']
card=1
if 'money' in pocket or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")