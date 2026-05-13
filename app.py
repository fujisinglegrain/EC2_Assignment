import streamlit as st
import datetime
import random # [새로 추가됨] 랜덤 숫자를 만들기 위한 파이썬 기본 도구

st.title("EC2 배포 실습 앱 🚀")
st.write("AWS Learner Lab EC2 환경에 배포된 Streamlit 앱입니다.")
st.divider()

# ==========================================
# 기능 1: 텍스트 입력 (로그 형식 A)
# ==========================================
st.subheader("1. 인사말 남기기")
user_input = st.text_input("이름이나 짧은 메시지를 입력해 주세요:")

if st.button("메시지 전송"):
    if user_input:
        st.success(f"환영합니다, '{user_input}'님!")
        
        # [로그 형식 A]
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] [메시지 수신] 사용자 입력 내용: {user_input}")
    else:
        st.warning("메시지를 입력해 주세요.")

st.divider()

# ==========================================
# 기능 2: 행운의 숫자 뽑기 (로그 형식 B)
# ==========================================
st.subheader("2. 오늘의 행운의 숫자 뽑기 🎲")
st.write("버튼을 누르면 1부터 100 사이의 랜덤 숫자를 시스템이 생성합니다.")

if st.button("숫자 뽑기"):
    # 1. 1부터 100 사이의 무작위 숫자 하나를 생성
    lucky_number = random.randint(1, 100)
    
    # 2. UI 화면: 결과 출력
    st.info(f"🎉 짠! 생성된 행운의 숫자는 **{lucky_number}** 입니다!")
    
    # (보너스) 숫자가 90 이상이면 풍선 효과 추가
    if lucky_number >= 90:
        st.balloons()

    # 3. 터미널 로그: 기능 1과는 다른 형태의 작동 로그 출력
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] [시스템 동작] 무작위 숫자 생성기 가동 -> 결과값: {lucky_number}")