## 문제의 조건을 빠짐없이 반영하기 위해 주석을 통해 요구조건을 보기쉽게 정리하는 습관을 들이는 것도 좋을 것 같다.
## 전체적인 로직이나 구현 방향을 미리 잡아놓고 출발하지 않으면 풀기가 굉장히 어려운 문제스타일이다.
## 미리 틀을 짜놓고 시작하는 것이 무조건 좋다!


## [x,y,a,b]
## --> (x,y)는 좌표
## --> a는 구조물 종류 : 0기둥, 1보
## --> b는 행동   종류 : 0삭제, 1설치


## 기둥은 바닥, 보의 한쪽 끝, 다른 기둥 위에!
## 보는 한쪽 끝이 기둥 위에, 양쪽끝이 다른 보에 연결되어 있어야함! (바닥 설치 불가)


## 유효한 기둥인지 보인지 check
def check(x, y, Type):
    global answer

    ## 기둥 check
    if Type == 0:

        ## 바닥인지, 보가 아래 있는지, 기둥이 아래 있는지
        if (y == 0) or ([x,y,1] in answer) or ([x-1,y,1] in answer) or ([x,y-1,0] in answer):
            return True

        else:
            return False



    ## 보 check
    elif Type == 1:

        ## 한쪽 끝이 기둥 위에 있는지, 양쪽 끝에 보가 있는지
        if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer) or ([x-1,y,1] in answer and [x+1,y,1] in answer):
            return True

        else:
            return False
        
        



def solution(n, build_frame):
    global answer
    answer = []

    N = len(build_frame)


    for cmd in build_frame:
        x, y, a, b = cmd

        ## 기둥
        if a == 0:

            ## 삭제
            if b == 0:

                ## 먼저 삭제후
                answer.remove([x, y, 0])

                ## 그 행동으로 인해 영향을 받을 가능성이 있는 구조물들의 유효성을 check
                need2Check = [[x,y+1,0], [x,y+1,1], [x-1,y+1,1]]

                removable = True
                for frame in need2Check:
                    if frame in answer:
                        if not check(*tuple(frame)):
                            removable = False
                            break

                ## 삭제했더니 유효하지 않은 블럭이 등장하면
                ## 다시 끼워넣기
                if not removable:
                    answer.append([x,y,0])
                            
                


            ## 설치
            elif b == 1:

                if check(x,y,0):
                    answer.append([x, y, 0])
                    



        ## 보
        elif a == 1:

            ## 삭제
            if b == 0:

                ## 먼저 삭제 후
                answer.remove([x,y,1])
                
                ## 그 행동으로 인해 영향을 받을 가능성이 있는 구조물들의 유효성을 check
                need2Check = [[x-1,y,1], [x,y,0], [x+1,y,0], [x+1,y,1]]

                removable = True
                for frame in need2Check:
                    if frame in answer:
                        if not check(*tuple(frame)):
                            removable = False
                            break

                ## 삭제했더니 유효하지 않은 블럭이 등장하면
                ## 다시 끼워넣기
                if not removable:
                    answer.append([x,y,1])

            ## 설치
            elif b == 1:

                if check(x,y,1):
                    answer.append([x,y,1])
    
    
    return sorted(answer)
