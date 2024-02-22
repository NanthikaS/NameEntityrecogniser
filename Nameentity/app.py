import streamlit as st
import spacy
import spacy_streamlit as spt

nlp=spacy.load('en_core_web_sm')

st.title('NER WebApp')
menu_items=['Tokenizer','NER']
choice=st.sidebar.selectbox('Menu Items',menu_items)

if (choice=='Tokenizer'):
    st.subheader('word Tokenization')
    raw_text=st.text_area('Text To Tokenizer','Enter Text here')
    docs=nlp(raw_text)
    if st.button('Tokenize'):
        spt.visualize_tokens(docs)

elif(choice== 'NER'):
    st.subheader('NER')
    raw_text=st.text_area('Enter text to get the named entities','Enter Text here')
    docs=nlp(raw_text)
    if st.button('NErecognize'):
        spt.visualize_ner(docs)