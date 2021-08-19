# 정규표현식을 알면 쉬운 문제, 모르면 절대 못푸는 문제!!


# 정규표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어.
# --> 정규식을 이용하면 문자열 매칭 관련 문제를 간단히 해결 할 수 있다!!

# python의 정규표현식 모듈
import re


def solution(word, pages):
    answer = 0

    # meta태그 안에 들어있는 링크, 즉 자기자신의 주소를 받아올 수 있는 패턴 객체
    meta_parser = re.compile('<meta property="og:url" content="(.+?)"/>')

    # a태그 안에 들어있는 링크를 모두 가져오는 패턴 객체
    a_parser = re.compile('<a href="(.+?)">')

    # 모든 페이지의 정보를 저장하는 리스트
    page_matching_grades = []


    # 각각의 페이지마다 확인하는 루프
    for page in pages:
        page_data = {}

        # 현재 주소는 길이 1짜리 리스트로 반환되므로 [0]을 통해 접근해줘야된다!
        site_name = meta_parser.findall(page)[0]

        # 외부 링크로 연결되는 링크를 리스트형태로 반환
        anchors = a_parser.findall(page)

        # sub --> replace함수이다.
        # page.lower()이라는 문자열에서 알파벳이 아닌 문자들을 .으로 교체!
        page = re.sub("[^a-z]", ".", page.lower())


        # 일치하는 단어의 수
        word_num = 0

        # 길이 1 이상의 알파벳으로 이루어진 단어들을 뽑아서 리스트 형태로 만들어줌
        WORDS = re.findall("[a-z]+", page)
        for WORD in WORDS:
            
            # 그렇게 뽑아진 단어들과, 현재 일치여부를 알고싶은 문자와 일치하면 word_num += 1
            if WORD == word.lower():
                word_num += 1
        
        
        page_data["site_name"] = site_name  # 사이트 이름
        page_data["anchors"]  = anchors     # 외부 링크 리스트
        page_data["word_num"]  = word_num   # 기본 점수
        page_data["link_grade"] = 0         # 링크 점수
 

        page_matching_grades.append(page_data)


    # result[i] : i+1번째 주소의 매칭 점수를 저장하는 리스트
    result = [0 for _ in range(len(pages))]

    
    for page in page_matching_grades:
        for loopPage in page_matching_grades:

            # 현재 페이지이면 무시하기!
            if page == loopPage:
                continue

            # 현재 확인하고 loopPage의 외부링크중 page와 연결되는 것이 있으면,
            # page의 링크점수를 더해준다!
            for anchor in loopPage["anchors"]:
                if anchor == page["site_name"]:
                    page["link_grade"] += loopPage["word_num"] / len(loopPage["anchors"])

    # 매칭점수를 저장하는 루프
    for idx, page in enumerate(page_matching_grades):
        result[idx] = page["word_num"] + page["link_grade"]



    # 매칭점수가 가장 큰 인덱스중에
    # 가장 먼저 발견되는 인덱스(앞에서부터 선형탐색하므로 최소 인덱스라는것이 보장됨)를 반환
    return result.index(max(result))
