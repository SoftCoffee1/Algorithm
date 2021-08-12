# 누를 번호와, 현재 엄지의 위치가 주어졌을 때 이동거리를 반환
def distance(num, thumb):
    global keyPad

    return abs(keyPad[num][0] - thumb[0]) + abs(keyPad[num][1] - thumb[1])

    
    

def solution(numbers, hand):
    global keyPad
    answer = ''
    

    # 키패드 딕셔너리로 구현
    keyPad = {
        0 : (3,1),
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        5 : (1,1),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2)
        }
    

    leftThumb = [3,0]
    rightThumb = [3,2]


    for number in numbers:

        # 1,4,7은 왼손엄지가 누르기!
        if number == 1 or number == 4 or number == 7:

            leftThumb[0] = keyPad[number][0]
            leftThumb[1] = keyPad[number][1]
            
            answer += "L"


        # 3,6,9은 오른손엄지가 누르기!
        elif number == 3 or number == 6 or number == 9:

            rightThumb[0] = keyPad[number][0]
            rightThumb[1] = keyPad[number][1]
            
            answer += "R"


        # 2,5,8,0은 더 가까운 엄지가! 만약 거리가 같다면 hand가 결정!
        else:

            left = distance(number, leftThumb)
            right = distance(number, rightThumb)


            # 왼손이 더 가깝다면, 왼손으로 누르기!
            if left < right:
                leftThumb[0] = keyPad[number][0]
                leftThumb[1] = keyPad[number][1]
            
                answer += "L"


            # 오른손이 더 가깝다면, 오른손으로 누르기!
            elif left > right:
                rightThumb[0] = keyPad[number][0]
                rightThumb[1] = keyPad[number][1]
            
                answer += "R"

            # 거리가 같다면, hand가 결정!
            else:

                # 왼손잡이면 왼손엄지로!
                if hand == "left":
                    leftThumb[0] = keyPad[number][0]
                    leftThumb[1] = keyPad[number][1]
            
                    answer += "L"


                # 오른손잡이면 오른손엄지로!
                else:
                    rightThumb[0] = keyPad[number][0]
                    rightThumb[1] = keyPad[number][1]
            
                    answer += "R"
    
    return answer
