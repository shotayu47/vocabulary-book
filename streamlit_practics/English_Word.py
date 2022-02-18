from streamlit import caching
import streamlit as st
import numpy as np
import pandas as pd
import time

@st.cache(allow_output_mutation=True)
def cache_word():
    word = {} # 英語：key, 日本語：value
    return word

def cache_en():
    en = []
    return en

def cache_jp():
    jp = []
    return jp


st.title('英単語帳')
word = cache_word()
en = cache_en()
jp = cache_jp()

en_input = st.sidebar.text_input('English')
jp_input = st.sidebar.text_input('日本語')

if st.sidebar.checkbox('clear'):
    caching.clear_cache()
    word = cache_word()
elif en_input and jp_input:
    en.append(en_input)
    jp.append(jp_input)
    if en and jp:
        if len(en) == len(jp):
            word[en[-1]] = jp[-1]

if st.sidebar.checkbox('delete'):
    en_delete = st.sidebar.selectbox('削除する単語を選択して下さい', options=list(word.keys()))
    if st.sidebar.button('Delete'):
        jp_delete = word.pop(en_delete)
        st.sidebar.success(f'Delete EN : {en_delete}, JP : {jp_delete}')

if st.sidebar.checkbox('change', 'Yes'):
    which_lan = st.sidebar.selectbox('変更する言語を選択して下さい', options=['English', '日本語'])
    if which_lan == 'English':
        en_change_from = st.sidebar.selectbox('変更する単語を選択して下さい', options=list(word.keys()))
        if en_change_from:
            en_change_to = st.sidebar.text_input('何に変更しますか')
            if st.sidebar.button('Change'):
                word[en_change_to] = word.pop(en_change_from)
                st.sidebar.success(f'Change {en_change_from} to {en_change_to}')
    elif which_lan == '日本語':
        jp_change_from = st.sidebar.selectbox('変更する訳を選択して下さい', options=list(word.values()))
        if jp_change_from:
            en_stock = word.get(jp_change_from)
            jp_change_to = st.sidebar.text_input('何に変更しますか')
            if st.sidebar.button('Change'):
                word[en_stock] = jp_change_to
                st.sidebar.success(f'Change {jp_change_from} to {jp_change_to}')
df = pd.DataFrame({
    'English':list(word.keys()),
    '日本語': list(word.values())
})


st.table(df)
