import streamlit as st
import datetime

st.title("EC2 배포 실습 앱 🚀")
st.write("이 앱은 AWS Learner Lab EC2 환경에 배포된 Streamlit 앱입니다.")
st.write("아래에 텍스트를 입력하고 버튼을 눌러보세요!")

# 1. 새로운 기능: 드롭다운 메뉴 (Selectbox) 추가
user_mood = st.selectbox(
    "오늘의 코딩 기분은 어떠신가요?",
    ("최고예요! 😆", "그저 그래요 🙂", "조금 피곤해요 😴", "코딩이 너무 재밌어요! 💻")
)

# 2. 기존 기능: 텍스트 입력창
user_input = st.text_input("이름이나 짧은 메시지를 입력해 주세요:")

# 3. 버튼 및 결과 출력
if st.button("실행하기"):
    if user_input:
        st.success(f"환영합니다, '{user_input}'님! 앱이 정상적으로 작동하고 있습니다. 🎉")
        
        # 4. 새로운 기능: 조건에 따른 화면 애니메이션 효과
        if user_mood == "코딩이 너무 재밌어요! 💻":
            st.balloons() # 화면 아래에서 위로 풍선이 올라가는 효과
        elif user_mood == "최고예요! 😆":
            st.snow()     # 화면 위에서 아래로 눈이 내리는 효과

        # 터미널에 보여질 로그 출력 (기분 정보 추가)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] 로그: {user_input}님 접속 완료 -> 기분 상태: {user_mood}")
    else:
        st.warning("메시지를 먼저 입력해 주세요!")
        print("로그: 빈 입력값으로 버튼이 클릭되었습니다.")