from pprint import pprint  ## print할 때 사용하면, 그 형식 그대로 보여줌 (예, json 파일)

### 1. 리스트 내에서 서로 비교할 때 사용!!
## if change_num_index == len(change_num_ls) - 1:      # step_by가 리스트 change_num_ls의 마지막 자릿 수인지 확인
## for next_step_by in change_num_ls[(change_num_index+1):]:
#    ↳ step_by 다음 인덱스들을 가져오는 코드
#    ↳ step_by(리스트 change_num_ls의 하나)를 리스트 change_num_ls의 나머지들과 비교하기 위해

## 예 1
change_num_ls = []
change_num_index = -1
mul_count_ls = []
for step_by in change_num_ls:
    mul_count = 1
    change_num_index += 1
    if len(step_by) == 8:
        if change_num_index == len(change_num_ls) - 1:      ## step_by가 리스트 change_num_ls의 마지막 자릿 수인지 확인
            mul_count_ls.append("%s     No duplicates" % step_by)
            break   ## step_by가 리스트 change_num_ls의 마지막 자릿 수 일 때는 비교 대상이 없으니, 종료해라
        del_index = 0
        for next_step_by in change_num_ls[(change_num_index+1):]:      ## step_by 다음 인덱스들을 가져오는 코드 ↴
            del_index += 1      ## step_by(리스트 change_num_ls의 하나)를 리스트 change_num_ls의 나머지들과 비교하기 위해
            if step_by == next_step_by:
                mul_count += 1
                change_num_ls[del_index] = next_step_by + "%s" % del_index

## 예 2
def Only_One(sort_news):
    index_count = -1
    for compa in sort_news:
        index_count += 1
        if index_count == len(sort_news) - 1:
            break
        for next_compa in sort_news[(index_count):]:
            if compa[1] == next_compa[1]:
                del sort_news[(index_count+1)]