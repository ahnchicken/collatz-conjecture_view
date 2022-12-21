import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("콜라츠 추측")
st.write('## 수학탐구 10815안희준')
x = st.number_input('시작할수를 선택해주세요.(2이상)',2,)
st.write("시작수:", x)

data=[]

m = x
data.append(x)
while x>1:
    if x%2==1:
        x = x*3+1
        data.append(x)
        if x>m:
            m = x
    elif x%2==0:
        x = x/2
        data.append(x)

dataframe = pd.DataFrame(np.array(data),columns=['콜라츠 추측의 우박수'])
st.write('넣은수의 변동:')
st.line_chart(dataframe)
st.write('우박수의 최대값: ',m)


st.write('##### 콜라츠 추측은 짝수면 1/2를 곱하고, 홀수면 3n+1을 하는 함수 g가 주어지고, 모든 n에 대해 이것이 1에 수렴하는지 묻는 문제 이다.')


