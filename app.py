import streamlit as st
import datetime

# 1. 간단한 설명 문구
st.title("EC2 배포 실습 앱 🚀")
st.write("이 앱은 AWS Learner Lab EC2 환경에 배포된 Streamlit 앱입니다.")
st.write("아래에 텍스트를 입력하고 버튼을 눌러보세요!")

# 2. 텍스트 입력창
user_input = st.text_input("이름이나 짧은 메시지를 입력해 주세요:")

# 3. 버튼 및 간단한 결과 출력
if st.button("실행하기"):
    if user_input:
        # 화면(브라우저)에 보여지는 결과 출력
        st.success(f"환영합니다, '{user_input}'님! 앱이 정상적으로 작동하고 있습니다. 🎉")
        
        # [핵심] EC2 터미널에 보여질 로그 출력 (데모 영상용)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] 로그: 사용자 입력 처리 완료 -> 입력값: {user_input}")
    else:
        # 입력값이 없을 때의 예외 처리
        st.warning("메시지를 먼저 입력해 주세요!")
        print("로그: 빈 입력값으로 버튼이 클릭되었습니다.")