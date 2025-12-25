import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
import os

# 1. Page Configuration for RTL (Right-to-Left)
st.set_page_config(page_title="Urdu AI Assistant", layout="wide")
st.markdown("""
    <style> 
    .stTextInput, .stTextArea, .stMarkdown { direction: rtl; text-align: right; } 
    </style>
    """, unsafe_allow_html=True)

st.title("اردو AI اسسٹنٹ 📝")
st.write("اپنی اردو پی ڈی ایف اپ لوڈ کریں اور سوال پوچھیں۔")

# 2. API Key setup
api_key = os.getenv("OPENAI_API_KEY") or st.sidebar.text_input("OpenAI API Key درج کریں", type="password")

if not api_key:
    st.warning("براہ کرم سائیڈ بار میں اپنی API کلید درج کریں۔")
    st.stop()

# 3. File Uploader
uploaded_file = st.file_uploader("اردو پی ڈی ایف فائل منتخب کریں", type="pdf")

if uploaded_file:
    with open("temp_urdu.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # 4. Extract Text
    loader = PyPDFLoader("temp_urdu.pdf")
    pages = loader.load_and_split()
    
    # Extract text from first 2 pages
    raw_text = " ".join([p.page_content for p in pages[:2]])
    normalized_text = raw_text
    
    st.success(f"فائل کامیابی کے ساتھ لوڈ ہو گئی ہے! ({len(pages)} صفحات)")

    # 5. Chat Interface
    user_query = st.text_input("اپنا سوال یہاں لکھیں:")
    
    if user_query:
        # OpenAI Model
        llm = ChatOpenAI(
            model="gpt-4o",
            api_key=api_key,
            temperature=0.4
        )
        
        prompt = f"""
        آپ ایک ماہر اردو اسسٹنٹ ہیں۔ نیچے دیے گئے متن کی بنیاد پر سوال کا جواب اردو میں دیں۔
        متن: {normalized_text}
        سوال: {user_query}
        جواب:
        """
        
        with st.spinner("جواب تیار کیا جا رہا ہے..."):
            response = llm.invoke(prompt)
            st.markdown(f"### جواب:\n {response.content}")