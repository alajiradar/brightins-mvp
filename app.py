import streamlit as st
import streamlit.components.v1 as components
import time

# 1. SET PAGE CONFIGURATION (Changes Browser Tab Title to Brightins)
st.set_page_config(page_title="Brightins", page_icon="🚀", layout="wide")

# 2. INJECT WEB APP META TAGS (Forces Mobile Browsers to recognize it as "Brightins")
st.markdown("""
    <head>
        <title>Brightins</title>
        <meta name="apple-mobile-web-app-title" content="Brightins">
        <meta name="application-name" content="Brightins">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="theme-color" content="#7f56da">
    </head>
""", unsafe_allow_html=True)

# Hide Streamlit Default Menu and Footer for pure branding experience
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 3. FREE LOCAL AI SIMULATOR ENGINE (Smart Simulation without Length & CTA parameters)
def generate_social_posts_local(business_description, tone, business_goal):
    time.sleep(1.2) # Realism delay
    
    desc = business_description.strip() if business_description.strip() else "our premium products"
    desc_lower = desc.lower()
    
    # Simple Auto-detect Hausa
    hausa_keywords = ["takalma", "saida", "kano", "turare", "yadi", "shadda", "atamfa", "kaya", "kudi", "maka", "kuna", "mun", "ina", "tsada", "bunkasa", "kasuwanci"]
    is_hausa = any(word in desc_lower for word in hausa_keywords)
    
    if is_hausa:
        cta_text = "Turo mana saƙon gaggawa (DM) yanzu a nan don ka mallaki naka! 📥"
        body_text = f"Kuna neman mafi kyau? Ga cikakken bayani akan {desc}. Muna tabbatar muku da inganci da gaskiya a kowane lokaci domin gamsuwarku."
        hashtags = "#Kasuwanci #Kano #Inganci #Arewa"
        
        fb = f"🚀 [Brightins AI Engine - Tone: {tone}]\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        ig = f"✨ Kasuwancinmu na gari (Goal: {business_goal}) ✨\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        tw = f"{body_text}\n\n{cta_text} {hashtags}"
        tt = f"🎥 [TikTok/Shorts Script - Daƙiƙa 60]\nTone: {tone}\n\n[0-15s - HOOK]: 'Tsaya ka saurara! Idan kana son bunkasa kasuwancinka a Intanet, wannan bidiyon naka ne!'\n\n[15-45s - BODY]: 'Ga babban dalilin da ya sa kowa ke magana akan {desc}. Yana da sauƙi da inganci.'\n\n[45-60s - CTA]: '{cta_text}'"
    
    else:
        cta_text = "Send us a Direct Message (DM) right now to place your order! 📥"
        body_text = f"Looking for the ultimate solution to elevate your lifestyle? Introducing '{desc}'. Crafted with precision and engineered to deliver top-notch results just for you."
        hashtags = "#BusinessGrowth #PremiumQuality #Innovation"
        
        fb = f"🚀 [Brightins AI Generated Post]\nTone: {tone} | Goal: {business_goal}\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        ig = f"✨ Quality meets excellence. ✨\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        tw = f"{body_text}\n\n{cta_text} {hashtags}"
        tt = f"🎥 [TikTok/Shorts Script - 60 Seconds]\nTone: {tone}\n\n[0-15s - HOOK]: 'Stop scrolling if you want to elevate your business today!'\n\n[15-45s - BODY]: 'Here is why everyone is talking about {desc}. It is simple, effective, and designed just for you.'\n\n[45-60s - CTA]: '{cta_text}'"

    return {"facebook": fb, "instagram": ig, "twitter": tw, "tiktok": tt}

# 4. STREAMLIT UI LAYOUT
st.title("Brightins 🚀")
st.subheader("Your Global AI Marketing Employee")
st.write("---")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 1. Describe Your Business")
    st.caption("Tell us about your business, products or services")
    business_description = st.text_area(
        "Business Description",
        value="",
        placeholder="e.g., We sell premium organic coffee blends online to customers worldwide...",
        label_visibility="collapsed"
    )
    
    st.markdown("### 2. Choose Tone")
    st.caption("Select the emotional tone for your marketing copy")
    tone = st.selectbox(
        "Tone", 
        ["Professional", "Aggressive Sales", "Friendly", "Humorous", "Luxury"],
        label_visibility="collapsed"
    )
    
    st.markdown("### 3. Business Goal")
    st.caption("What is the main objective of this content?")
    business_goal = st.selectbox(
        "Goal", 
        ["Increase Sales", "Brand Awareness", "Get Leads"],
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
            with st.spinner("Brightins AI Engine is analyzing..."):
                posts = generate_social_posts_local(business_description, tone, business_goal)
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
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 10px;
                ">📋 Copy Facebook Post</button>
            """, height=50)
            st.download_button(
                label="📥 Download Facebook Post",
                data=posts["facebook"],
                file_name="brightins_facebook.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        with tab2:
            st.text_area("Instagram Content", posts["instagram"], height=200, label_visibility="collapsed")
            components.html(f"""
                <textarea id="ig_text" style="display:none;">{posts["instagram"]}</textarea>
                <button onclick="var text = document.getElementById('ig_text').value; navigator.clipboard.writeText(text); alert('📸 Instagram Caption Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 10px;
                ">📋 Copy Instagram Caption</button>
            """, height=50)
            st.download_button(
                label="📥 Download Instagram Caption",
                data=posts["instagram"],
                file_name="brightins_instagram.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        with tab3:
            st.text_area("X Content", posts["twitter"], height=150, label_visibility="collapsed")
            components.html(f"""
                <textarea id="x_text" style="display:none;">{posts["twitter"]}</textarea>
                <button onclick="var text = document.getElementById('x_text').value; navigator.clipboard.writeText(text); alert('𝕏 X Post Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 10px;
                ">📋 Copy X Post</button>
            """, height=50)
            st.download_button(
                label="📥 Download X Post",
                data=posts["twitter"],
                file_name="brightins_x_post.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        with tab4:
            st.text_area("TikTok Content", posts["tiktok"], height=220, label_visibility="collapsed")
            components.html(f"""
                <textarea id="tt_text" style="display:none;">{posts["tiktok"]}</textarea>
                <button onclick="var text = document.getElementById('tt_text').value; navigator.clipboard.writeText(text); alert('🎥 Video Script Copied!')" style="
                    background-color: #7f56da; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 10px;
                ">📋 Copy Video Script</button>
            """, height=50)
            st.download_button(
                label="📥 Download TikTok Script",
                data=posts["tiktok"],
                file_name="brightins_tiktok_script.txt",
                mime="text/plain",
                use_container_width=True
            )
    else:
        st.write("Your multi-platform marketing content will appear here after you hit the generate button.")

# --- FOOTER SECTION ---
st.markdown("<br><br><hr><p style='text-align: center; color: gray; font-size: 14px;'>© 2026 Brightins AI Enterprise. All Rights Reserved.</p>", unsafe_allow_html=True)