import google.generativeai as genai
GOOGLE_API_KEY='AIzaSyC06L2D9NIQfEXuIUOv0cpgrzf_wDVoGuI'
genai.configure(api_key=GOOGLE_API_KEY)
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import PIL.ImageChops
import pickle
def to_markdown(text):
    text=text.replace(".",' *')
    return Markdown(textwrap.indent(text,'>',predicate=lambda _:True))
model=genai.GenerativeModel('gemini-1.5-flash-8b-exp-0924')
#for m in genai.list_models():
    #if 'GenerateContent' in m.supported
 #   print(m)
#res=model.generate_content('find duplicates in string in python')
#print(res.text)    
#Save the model to disk
filename=r'C:\Users\91807\VSCodeProjects\PythonPractice\5.GEMINI MODELS\GmodelUsedinStreamLit.pkl'
with open(filename,'wb') as file:
    pickle.dump(model,file)
print('Genai model dumped into file:GmodelUsedinStreamLit.pkl')





