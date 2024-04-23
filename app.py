import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

# 기본 텍스트 요소
st.title('this is the app title')
st.header('this is the header')
st.markdown('*this is the markdown*')
st.subheader('this is the subheader')
st.caption('this is the caption')
st.code('x=2024')
st.latex(r'''
a + a r^1 + a r^2''')

# 인풋 위젯
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('choose', ['A', 'B', 'C'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)
