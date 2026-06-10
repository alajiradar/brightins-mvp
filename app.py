import streamlit as st
import streamlit.components.v1 as components
import time

# 1. SET PAGE CONFIGURATION
st.set_page_config(page_title="Brightins MVP", page_icon="🚀", layout="wide")

# 2. FREE LOCAL AI SIMULATOR ENGINE (No OpenAI Key Required)
def generate_social_posts_local(business_description, tone, business_goal, content_length, cta_style):
    """
    Brightins Free Local AI Simulator 
    Runs 100% offline and free without OpenAI API Key.
    """
    time.sleep(1.5) # Fake AI processing delay for realistic feel
    
    desc = business_description.strip() if business_description.strip() else "our premium products"
    desc_lower = desc.lower()
    
    # Auto-detect Hausa keywords from description
    hausa_keywords = ["takalma", "saida", "kano", "turare", "yadi", "shadda", "atamfa", "kaya", "kudi", "maka", "kuna", "mun", "ina", "tsada", "bunkasa", "kasuwanci"]
    is_hausa = any(word in desc_lower for word in hausa_keywords)
    
    if is_hausa:
        cta_dict = {
            "Soft CTA": "Muna son jin ra'ayoyinku a sashen comment! 👇",
            "Strong Sales CTA": "YI MAZA KA SAYI NAKA YANZU! Kaya sun kusa ƙarewa, kada a ba ka labari! 🚨",
            "WhatsApp CTA": "Latsa nan domin yin magana da mu kai tsaye a WhatsApp: https://wa.me/2348000000000 📲",
            "DM CTA": "Turo mana saƙon gaggawa (DM) yanzu a nan don ka mallaki naka! 📥"
        }
        length_intro = {
            "Short": f"Gajeren tallanmu akan: {desc}.",
            "Medium": f"Kuna neman mafi kyau? Ga cikakken bayani akan {desc}. Muna tabbatar muku da inganci da gaskiya a kowane lokaci domin gamsuwarku.",
            "Long": f"Barka da zuwa! Idan kuna neman inganci, ƙarko, da gamsuwa na gaskiya, wannan bayanin naku ne.\n\nAbubuwan da suka sa '{desc}' ya fita daban a kasuwa:\n1. Inganci na gaba-da-gaba (Premium Quality).\n2. Farashi mai sauƙi domin kowa.\n3. Amintaccen sabis da saurin tura kaya.\n\nKada ku sake a ba ku labari wajen neman kayan arziki."
        }
        hashtags = "#Kasuwanci #Kano #Inganci #Arewa"
        
        fb = f"🚀 [Brightins AI Engine - Tone: {tone}]\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        ig = f"✨ Kasuwancinmu na gari (Goal: {business_goal}) ✨\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        tw = f"{length_intro['Short'] if content_length == 'Long' else length_intro[content_length]}\n\n{cta_dict[cta_style]} {hashtags}"
        tt = f"🎥 [TikTok/Shorts Script - Daƙiƙa 60]\nTone: {tone}\n\n[0-15s - HOOK]: (Fito da fara'a da kuzari) 'Tsaya ka saurara! Idan kana son bunkasa kasuwancinka a Intanet, wannan bidiyon naka ne!'\n\n[15-45s - BODY]: 'Ga babban dalilin da ya sa kowa ke magana akan {desc}. Yana da sauƙi da inganci.'\n\n[45-60s - CTA]: '{cta_dict[cta_style]}'"
    
    else:
        cta_dict = {
            "Soft CTA": "Let us know your thoughts in the comments below! 👇",
            "Strong Sales CTA": "BUY NOW! Limited stock available. Don't miss out on this exclusive offer! 🚨",
            "WhatsApp CTA": "Chat with us directly on WhatsApp for instant orders: https://wa.me/2348000000000 📲",
            "DM CTA": "Send us a Direct Message (DM) right now to place your order! 📥"
        }
        length_intro = {
            "Short": f"Quick look at our premium product: {desc}.",
            "Medium": f"Looking for the ultimate solution to elevate your lifestyle? Introducing '{desc}'. Crafted with precision and engineered to deliver top-notch results just for you.",
            "Long": f"Welcome to the next level of excellence. If you value premium quality, long-lasting durability, and maximum satisfaction, you are in the right place.\n\nWhy choose '{desc}':\n1. Unmatched Premium Quality.\n2. Globally Trusted & Certified.\n3. Budget-Friendly & Highly Affordable.\n\nDon't compromise on your standards when you can have the very best today."
        }
        hashtags = "#BusinessGrowth #PremiumQuality #Innovation"
        
        fb = f"🚀 [Brightins AI Generated Post]\nTone: {tone} | Goal: {business_goal}\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        ig = f"✨ Quality meets excellence. ✨\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        tw = f"{length_intro['Short'] if content_length == 'Long' else length_intro[content_length]}\n\n{cta_dict[cta_style]} {hashtags}"
        tt = f"🎥 [TikTok/Shorts Script - 60 Seconds]\nTone: {tone}\n\n[0-15s - HOOK]: (Look directly at the camera with energy) 'Stop scrolling if you want to elevate your business today!'\n\n[15-45s - BODY]: 'Here is why everyone is talking about {desc}. It is simple, effective, and designed just for you.'\n\n[45-60s - CTA]: '{cta_dict[cta_style]}'"

    return {"facebook": fb, "instagram": ig, "twitter": tw, "tiktok": tt}

# 3. STREAMLIT UI LAYOUT (Clean English Interface)
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
                # Call the local simulator directly (Bulletproof & Free)
                posts = generate_social_posts_local(business_description, tone, business_goal, content_length, cta_style)
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