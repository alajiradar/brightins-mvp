import streamlit as st
import streamlit.components.v1 as components
from openai_service import generate_social_posts

st.set_page_config(page_title="Brightins MVP", page_icon="🚀", layout="wide")

st.title("Brightins 🚀")
st.subheader("Your Global AI Marketing Employee")
st.write("---")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 1. Describe Your Business")
    st.caption("Tell us about your business or product")
    business_description = st.text_area(
        "Business Description",
        placeholder="e.g., We sell premium organic coffee blends online to customers worldwide...",
        label_visibility="collapsed"
    )
    
    st.markdown("### 2. Choose Tone")
    st.caption("Select the tone you want")
    tone = st.selectbox(
        "Tone", 
        ["Professional", "Aggressive Sales", "Friendly", "Humorous", "Luxury"],
        label_visibility="collapsed"
    )
    
    st.markdown("### 3. Business Goal")
    st.caption("What do you want to achieve?")
    business_goal = st.selectbox(
        "Goal", 
        ["Increase Sales", "Brand Awareness", "Get Leads"],
        label_visibility="collapsed"
    )
    
    st.markdown("### 4. Content Length")
    st.caption("Select the length of your post")
    content_length = st.selectbox(
        "Length", 
        ["Short", "Medium", "Long"],
        label_visibility="collapsed"
    )
    
    st.markdown("### 5. Call-To-Action Style")
    st.caption("Select your preferred CTA style")
    cta_style = st.selectbox(
        "CTA", 
        ["Soft CTA", "Strong Sales CTA", "WhatsApp CTA", "DM CTA"],
        label_visibility="collapsed"
    )
    
    st.write("")
    generate_button = st.button("🚀 Generate Marketing Content", use_container_width=True)

with col2:
    st.markdown("### 📋 Your Generated Content")
    
    if generate_button:
        if not business_description.strip():
            st.error("Please enter your business description first!")
        else:
            with st.spinner("Brightins AI is thinking... Please wait..."):
                posts = generate_social_posts(business_description, tone, business_goal, content_length, cta_style)
                st.session_state['brightins_posts'] = posts
                st.session_state['data_ready'] = True

    if st.session_state.get('data_ready', False):
        posts = st.session_state['brightins_posts']
        
        tab1, tab2, tab3, tab4 = st.tabs(["📘 Facebook Post", "📸 Instagram Caption", "🐦 X (Twitter) Post", "🎥 TikTok Script"])
        
        with tab1:
            st.text_area("Facebook Content", posts["facebook"], height=200, label_visibility="collapsed")
            components.html(f"""
                <textarea id="fb_text" style="display:none;">{posts["facebook"]}</textarea>
                <button onclick="var text = document.getElementById('fb_text').value; navigator.clipboard.writeText(text); alert('🚀 Facebook Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Facebook Post</button>
            """, height=55)
            
        with tab2:
            st.text_area("Instagram Content", posts["instagram"], height=200, label_visibility="collapsed")
            components.html(f"""
                <textarea id="ig_text" style="display:none;">{posts["instagram"]}</textarea>
                <button onclick="var text = document.getElementById('ig_text').value; navigator.clipboard.writeText(text); alert('📸 Instagram Caption Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Instagram Caption</button>
            """, height=55)
            
        with tab3:
            st.text_area("X Content", posts["twitter"], height=150, label_visibility="collapsed")
            components.html(f"""
                <textarea id="x_text" style="display:none;">{posts["twitter"]}</textarea>
                <button onclick="var text = document.getElementById('x_text').value; navigator.clipboard.writeText(text); alert('𝕏 X Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy X Post</button>
            """, height=55)
            
        with tab4:
            st.text_area("TikTok Content", posts["tiktok"], height=220, label_visibility="collapsed")
            components.html(f"""
                <textarea id="tt_text" style="display:none;">{posts["tiktok"]}</textarea>
                <button onclick="var text = document.getElementById('tt_text').value; navigator.clipboard.writeText(text); alert('🎥 Video Script Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Video Script</button>
            """, height=55)
    else:
        st.write("Your multi-platform marketing content will appear here after you hit the generate button.")