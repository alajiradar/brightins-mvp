import streamlit as st
import streamlit.components.v1 as components
from openai_service import generate_social_posts

st.set_page_config(page_title="Brightins MVP", page_icon="✨", layout="wide")

st.title("Brightins 🚀")
st.subheader("Your Global AI Marketing Employee")
st.write("---")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 1. Creative Inputs")
    business_description = st.text_area(
        "Describe Your Business / Samfurin Kasuwanci",
        placeholder="e.g., We sell organic coffee blends... (Ko ka rubuta da Hausa: Ina siyar da takalma a kano...)",
        height=120
    )
    
    tone = st.selectbox("Select Tone", ["Professional", "Aggressive Sales", "Friendly", "Humorous", "Luxury"])
    business_goal = st.selectbox("Business Goal", ["Increase Sales", "Brand Awareness", "Get Leads"])
    
    # Sabbin Fasaloli (New Features)
    content_length = st.selectbox("Content Length", ["Short", "Medium", "Long"])
    cta_style = st.selectbox("Call-To-Action (CTA) Style", ["Soft CTA", "Strong Sales CTA", "WhatsApp CTA", "DM CTA"])
    
    st.write("")
    generate_button = st.button("✨ Generate Marketing Content", use_container_width=True)
    
    st.write("")
    st.info("💡 **Language Auto-Detect:** You don't need to select a language! Just write in Hausa or English, and Brightins will automatically generate the content in that language.")

with col2:
    st.markdown("### 📋 Your Generated Content")
    
    if generate_button:
        if not business_description.strip():
            st.error("⚠️ Please enter your business description first! / Da fatan za a bayyana kasuwancinka!")
        else:
            with st.spinner("AI Employee is creating your content..."):
                posts = generate_social_posts(business_description, tone, business_goal, content_length, cta_style)
                st.session_state['brightins_data'] = posts
                st.session_state['has_data'] = True

    if st.session_state.get('has_data', False):
        posts = st.session_state['brightins_data']
        
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Facebook", "📸 Instagram", "𝕏 X (Twitter)", "🎥 TikTok/Shorts Script"])
        
        with tab1:
            st.markdown("#### Facebook Post")
            st.info(posts["facebook"])
            components.html(f"""
                <textarea id="fb_text" style="display:none;">{posts["facebook"]}</textarea>
                <button onclick="var text = document.getElementById('fb_text').value; navigator.clipboard.writeText(text); alert('🚀 Facebook Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Facebook Post</button>
            """, height=55)
            
        with tab2:
            st.markdown("#### Instagram Caption")
            st.info(posts["instagram"])
            components.html(f"""
                <textarea id="insta_text" style="display:none;">{posts["instagram"]}</textarea>
                <button onclick="var text = document.getElementById('insta_text').value; navigator.clipboard.writeText(text); alert('📸 Instagram Caption Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Instagram Caption</button>
            """, height=55)
            
        with tab3:
            st.markdown("#### X (Twitter) Post")
            st.info(posts["twitter"])
            components.html(f"""
                <textarea id="x_text" style="display:none;">{posts["twitter"]}</textarea>
                <button onclick="var text = document.getElementById('x_text').value; navigator.clipboard.writeText(text); alert('𝕏 X Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy X Post</button>
            """, height=55)
            
        with tab4:
            st.markdown("#### TikTok & YouTube Shorts Video Script")
            st.info(posts["tiktok"])
            components.html(f"""
                <textarea id="tt_text" style="display:none;">{posts["tiktok"]}</textarea>
                <button onclick="var text = document.getElementById('tt_text').value; navigator.clipboard.writeText(text); alert('🎥 Video Script Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px;
                ">📋 Copy Video Script</button>
            """, height=55)
            
    else:
        st.write("Your multi-platform marketing content will appear here after you hit the generate button.")