import streamlit as st
import numpy as np
#import pickle
import google.generativeai as genai
GOOGLE_API_KEY='AIzaSyC06L2D9NIQfEXuIUOv0cpgrzf_wDVoGuI'
genai.configure(api_key=GOOGLE_API_KEY)
import PIL.Image
import PIL.ImageChops

#gModel=pickle.load(open(r'c:/Users/91807/VSCodeProjects/PythonPractice/5.GEMINI MODELS\GmodelUsedinStreamLit.pkl','rb'))
gModel=genai.GenerativeModel('gemini-1.5-flash-latest')

st.title('GENAI APP')
st.write('This App Acts like Gen AI model')

prompt=st.text_input('Enter Your Quey:')
if st.button('Ask'):
    res=gModel.generate_content(prompt)
    st.success(res.text)
uploader=st.file_uploader("Choose a Image",type=['png','jpg','jpeg'])
#image_bytes=uploader.read()

#img=PIL.Image.open(uploader.name())
if uploader is not None:
    
    #st.write('If Loop')
    img=PIL.Image.open(uploader)                             
    #st.image(img)
    res=gModel.generate_content(img)
    st.write(res.text)
else:
    print('No File uploaded')

    