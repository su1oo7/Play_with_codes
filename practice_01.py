"""
3 ≤ name의 길이 = yearning의 길이≤ 100
3 ≤ name의 원소의 길이 ≤ 7
name의 원소들은 알파벳 소문자로만 이루어져 있습니다.
name에는 중복된 값이 들어가지 않습니다.
1 ≤ yearning[i] ≤ 100
yearning[i]는 i번째 사람의 그리움 점수입니다.
3 ≤ photo의 길이 ≤ 100
1 ≤ photo[i]의 길이 ≤ 100
3 ≤ photo[i]의 원소(문자열)의 길이 ≤ 7
photo[i]의 원소들은 알파벳 소문자로만 이루어져 있습니다.
photo[i]의 원소들은 중복된 값이 들어가지 않습니다.
"""
## mine
def solution(name, yearning, photo):
    mem = dict()
    for i, n in enumerate(name):
        mem[n] = yearning[i]
    def point(list):
        return sum([mem[p] if p in mem.keys() else 0 for p in list])
    
    answer = [point(x) for x in photo]
    return answer
	
## betters 

def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]
# list에 원자가 없으면 에러나는 게 어떻게 했나했더니 if j in 이름 => else는 자동 None return
	
def solution(name, yearning, photo):
    score_dict = dict(zip(name,yearning))
    return [sum(map(lambda x: score_dict[x] if x in score_dict else 0,p)) for p in photo]
# zip으로 묶는거 아는데 안쓴거...습관 ㄱ 
# 단순화가 습관화 된 사람인 듯 , zip이랑 map 사용이 자연스러	
