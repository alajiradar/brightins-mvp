import streamlit as st
import streamlit.components.v1 as components
from openai_service import generate_social_posts

# Sanya fasalin shafin yanar gizo na Brightins
st.set_page_config(page_title="Brightins MVP", page_icon="✨", layout="wide")

# Babban Sashen Suna (Header)
st.title("Brightins 🚀")
st.subheader("Your Global AI Marketing Employee")
st.write("---")

# Raba shafin gida biyu (Hagu don Shigar da Bayani, Dama don Nuna Sakamako)
col1, col2 = st.columns([1, 1.2])

# BANGAREN HAGU: INPUTS
with col1:
    st.markdown("### 1. Describe Your Business")
    business_description = st.text_area(
        "Tell us about your business or product",
        placeholder="e.g., We sell premium organic coffee blends online to customers worldwide...",
        height=150
    )
    
    st.markdown("### 2. Choose Tone")
    tone = st.selectbox(
        "Select the tone you want",
        ["Professional", "Aggressive Sales", "Luxury", "Friendly", "Creative"]
    )
    
    st.markdown("### 3. Business Goal")
    business_goal = st.selectbox(
        "What do you want to achieve?",
        ["Increase Sales", "Brand Awareness", "Get Leads", "Educate Audience"]
    )
    
    st.write("")
    # Babban maɓallin tura aiki
    generate_button = st.button("✨ Generate Marketing Content", use_container_width=True)
    
    st.write("")
    st.info("💡 **Tip:** Write in any language (Hausa, English, French, etc.). Brightins will automatically detect it and generate content in the same language.")

# BANGAREN DAMA: OUTPUTS (Sakamako)
with col2:
    st.markdown("### 📋 Your Generated Content")
    
    # Amfani da Session State don adana bayanan ko da an danna wani abu daban
    if generate_button:
        with st.spinner("AI Employee is thinking..."):
            # Kira gurbin openai_service (Dummy Data)
            posts = generate_social_posts(business_description, tone, business_goal)
            st.session_state['brightins_content'] = posts
            st.session_state['has_generated'] = True

    # Idan an riga an samar da data, nuna ta anan
    if st.session_state.get('has_generated', False):
        posts = st.session_state['brightins_content']
        
        # Samar da Shafukan Tabs guda uku madaidaita
        tab1, tab2, tab3 = st.tabs(["📊 Facebook Post", "📸 Instagram Caption", "𝕏 X (Twitter) Post"])
        
        # 1. FACEBOOK TAB
        with tab1:
            fb_content = posts.get("facebook", "No Facebook content generated.")
            st.markdown("#### Facebook Content")
            st.info(fb_content)
            
            # Maɓallin Copy na Facebook ta amfani da JavaScript (Hidden Textarea method don magance matsalolin lissafin rubutu)
            components.html(f"""
                <textarea id="fb_text" style="display:none;">{fb_content}</textarea>
                <button onclick="var text = document.getElementById('fb_text').value; navigator.clipboard.writeText(text); alert('🚀 Facebook Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; 
                    padding: 12px 20px; border-radius: 6px; cursor: pointer; 
                    font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Facebook Post</button>
            """, height=55)
            
            st.download_button("📥 Download Facebook Post", fb_content, file_name="facebook_post.txt", use_container_width=True)
        
        # 2. INSTAGRAM TAB
        with tab2:
            insta_content = posts.get("instagram", "No Instagram content generated.")
            st.markdown("#### Instagram Caption")
            st.info(insta_content)
            
            # Maɓallin Copy na Instagram
            components.html(f"""
                <textarea id="insta_text" style="display:none;">{insta_content}</textarea>
                <button onclick="var text = document.getElementById('insta_text').value; navigator.clipboard.writeText(text); alert('📸 Instagram Caption Copied!')" style="
                    background-color: #7f56da; color: white; border: none; 
                    padding: 12px 20px; border-radius: 6px; cursor: pointer; 
                    font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Instagram Caption</button>
            """, height=55)
            
            st.download_button("📥 Download Instagram Caption", insta_content, file_name="instagram_caption.txt", use_container_width=True)
        
        # 3. X (TWITTER) TAB
        with tab3:
            # Anan an gyara mabuɗin zuwa 'twitter' don ya dace da abin da ke cikin openai_service.py
            x_content = posts.get("twitter", "No X content generated.")
            st.markdown("#### X (Twitter) Post")
            st.info(x_content)
            
            # Maɓallin Copy na X Post
            components.html(f"""
                <textarea id="x_text" style="display:none;">{x_content}</textarea>
                <button onclick="var text = document.getElementById('x_text').value; navigator.clipboard.writeText(text); alert('𝕏 X Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; 
                    padding: 12px 20px; border-radius: 6px; cursor: pointer; 
                    font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy X Post</button>
            """, height=55)
            
            st.download_button("📥 Download X Post", x_content, file_name="x_post.txt", use_container_width=True)
            
    else:
        # Sakon farko kafin a danna button
        st.write("Your multi-platform marketing content will appear here after you hit the generate button.")