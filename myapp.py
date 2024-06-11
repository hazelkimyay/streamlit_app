import streamlit as st
import random

# 메뉴 데이터베이스
menus = [
    {"name": "비빔밥", "type": "한식", "diet": "standard"},
    {"name": "된장찌개", "type": "한식", "diet": "standard"},
    {"name": "김치찌개", "type": "한식", "diet": "standard"},
    {"name": "초밥", "type": "일식", "diet": "standard"},
    {"name": "라멘", "type": "일식", "diet": "standard"},
    {"name": "파스타", "type": "양식", "diet": "standard"},
    {"name": "샐러드", "type": "양식", "diet": "vegetarian"},
    {"name": "채식 비빔밥", "type": "한식", "diet": "vegetarian"},
    {"name": "두부 스테이크", "type": "양식", "diet": "vegetarian"},
    {"name": "야채 라면", "type": "일식", "diet": "vegetarian"}
]

# 메뉴 추천 알고리즘
def recommend_menu(menus, cuisine_type, diet_preference):
    filtered_menus = [menu for menu in menus if
                      (cuisine_type == "상관없음" or menu["type"] == cuisine_type) and
                      (diet_preference == "상관없음" or menu["diet"] == diet_preference)]
    if filtered_menus:
        recommended_menu = random.choice(filtered_menus)
        return f"추천 메뉴: {recommended_menu['name']}"
    else:
        return "해당 조건에 맞는 메뉴가 없습니다."

# Streamlit 애플리케이션 시작
st.title("점심 메뉴 추천")
st.write("원하는 음식 종류와 식단 제약을 선택하세요.")

# 사용자 입력 받기
cuisine_type = st.selectbox("원하는 음식 종류를 선택하세요", ["한식", "일식", "양식", "상관없음"])
diet_preference = st.selectbox("식단 제약이 있습니까?", ["standard", "vegetarian", "상관없음"])

if st.button("추천받기"):
    recommendation = recommend_menu(menus, cuisine_type, diet_preference)
    st.write(recommendation)
