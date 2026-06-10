import streamlit as st
import time

# 1. PAGE INITIALIZATION & CONFIG
st.set_page_config(page_title="Brightins - Your AI Marketing Employee", page_icon="✨", layout="wide")

# Hide Default Streamlit Elements for professional look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.block-container {padding-top: 2rem; padding-bottom: 2rem;}
    </style>
""", unsafe_allow_html=True)

# 2. CUSTOM CSS TO MATCH MOCKUP LUXURY UI
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [data-testid="stSidebar"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    div[data-testid="stSidebarUserContent"] {
        padding-top: 1.5rem;
    }
    .sidebar-brand {
        font-size: 26px; font-weight: 700; color: #4F46E5; margin-bottom: 2px; display: flex; align-items: center; gap: 8px;
    }
    .sidebar-sub {
        font-size: 13px; color: #6B7280; margin-bottom: 2rem;
    }
    .nav-item {
        padding: 10px 14px; border-radius: 8px; font-weight: 500; font-size: 15px; margin-bottom: 6px; display: flex; align-items: center; gap: 10px; cursor: pointer;
    }
    .nav-active {
        background-color: #EEF2FF; color: #4F46E5;
    }
    .nav-inactive {
        color: #374151;
    }
    .pro-card {
        background-color: #F9FAFB; border: 1px solid #E5E7EB; padding: 16px; border-radius: 12px; margin-top: 4rem; text-align: left;
    }
    .pro-title {
        font-weight: 600; font-size: 14px; color: #111827; margin-bottom: 4px; display: flex; align-items: center; gap: 6px;
    }
    .pro-desc {
        font-size: 12px; color: #6B7280; margin-bottom: 12px;
    }
    .pro-btn {
        background: #6D31ED; color: white; border: none; padding: 8px; width: 100%; border-radius: 6px; font-size: 13px; font-weight: 500; text-align: center;
    }

    /* Main Page Elements */
    .main-header {
        font-size: 28px; font-weight: 700; color: #111827; margin-bottom: 4px;
    }
    .main-subtitle {
        font-size: 15px; color: #4B5563; margin-bottom: 2rem;
    }
    
    /* Section Headers */
    .section-title {
        font-size: 15px; font-weight: 600; color: #111827; margin-bottom: 4px;
    }
    .section-desc {
        font-size: 13px; color: #6B7280; margin-bottom: 10px;
    }

    /* Badges & Tips */
    .badge-lang {
        background-color: #DCFCE7; color: #15803D; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; float: right;
    }
    .tip-box {
        background-color: #F0FDF4; border: 1px solid #DCFCE7; padding: 12px; border-radius: 8px; margin-top: 15px; font-size: 13px; color: #166534; display: flex; gap: 8px;
    }
    
    /* Output Result Cards */
    .result-card {
        background: white; border: 1px solid #E5E7EB; border-radius: 12px; padding: 16px; margin-bottom: 16px; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    }
    .card-header {
        display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #F3F4F6; padding-bottom: 10px; margin-bottom: 12px;
    }
    .card-title {
        font-weight: 600; font-size: 14px; color: #111827; display: flex; align-items: center; gap: 8px;
    }
    
    /* Footer Status */
    .status-bar {
        background-color: #F0FDF4; border: 1px solid #DCFCE7; padding: 10px 16px; border-radius: 8px; font-size: 13px; color: #166534; display: flex; justify-content: space-between; align-items: center; margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION CONTEXT
with st.sidebar:
    st.markdown('<div class="sidebar-brand">✨ Brightins</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Your Global AI Marketing Employee</div>', unsafe_allow_html=True)
    
    # Navigation Links
    st.markdown('<div class="nav-item nav-active">⚡ Generate Content</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item nav-inactive">📂 My History</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item nav-inactive">🔖 Saved Content</div>', unsafe_allow_html=True)
    
    # Pro Upgrade Block
    st.markdown("""
        <div class="pro-card">
            <div class="pro-title">⭐ Upgrade to Pro</div>
            <div class="pro-desc">Unlock more features, templates, and automation.</div>
            <div class="pro-btn">Coming Soon</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Footer
    st.markdown("<br><br><p style='font-size:11px; color:#9CA3AF; margin-bottom:0px;'>© 2026 Brightins<br>All rights reserved.</p>", unsafe_allow_html=True)

# 4. MAIN PAGE CONTENT HEADER
st.markdown('<div class="main-header">Welcome to Brightins 👋</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Create powerful marketing content for your business in any language.</div>', unsafe_allow_html=True)

# Split screen into two columns like the layout mockup
col_input, col_output = st.columns([1, 1.3], gap="large")

# --- LOCAL AI SIMULATOR FOR MOCKUP ---
def generate_posts_mockup(desc, tone, goal):
    time.sleep(1.0)
    # Default fallback string if text is empty
    input_text = desc if desc.strip() else "premium coffee blends"
    
    hausa_keywords = ["takalma", "saida", "kano", "turare", "yadi", "shadda", "kaya", "kudi", "ina"]
    is_hausa = any(w in input_text.lower() for w in hausa_keywords)
    
    if is_hausa:
        return {
            "lang": "Hausa",
            "fb": f"Nuna kanka da kamshi mai ɗaukar hankali! ✨\n\nMuna da tarin sababbin samfura masu inganci na musamman da suka fito daga garin saunƙar kasuwanci.\n\nZiyarci shagonmu ko tuntube mu yanzu domin mallakar naku! 💎\n\n#Kasuwanci #Kano #Inganci #Tone_{tone}",
            "ig": f"Kamshi yana magana kafin ka faɗi komai. 🌸\n\nSabbin samfuranmu sun isa domin ba ku gamsuwa ta gari kowane lokaci.\n\nKada ku bari a ba ku labari! 📥 Turo saƙo yanzu.\n\n#Luxury #Kano #BrandGoal_{goal}",
            "x": f"Inganci da dacewa duka a wuri guda! 🚀\n\nMallaki ingantaccen samfuri dake yanka tasiri a kasuwa yanzu.\n\nTuntube mu a yau! 🔥 #BrightinsAI #Arewa"
        }
    else:
        return {
            "lang": "English",
            "fb": f"Elevate your lifestyle with premium quality! 🚀\n\nDiscover our newly launched updates on '{input_text}' tailored specially for your satisfaction and luxury taste.\n\nClick the link or send a DM to order today! ✨\n\n#BusinessGrowth #PremiumQuality #Tone_{tone}",
            "ig": f"Quality meets absolute excellence. ✨\n\nHere is why everyone is talking about '{input_text}'. It is engineered to give you the perfect result you deserve.\n\nGet yours now! 📥 #Luxury #Innovation #Goal_{goal}",
            "x": f"Looking for the ultimate experience? Look no further! 💎\n\nIntroducing our top-tier '{input_text}' built for durability and success. #Brightins"
        }

# 5. LEFT COLUMN: INPUT PANEL
with col_input:
    st.markdown('<div class="section-title">1. Describe Your Business</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Tell us about your business or product</div>', unsafe_allow_html=True)
    
    # Global approach: Empty input field with a clear English Placeholder
    biz_description = st.text_area(
        "Biz Desc", 
        value="", 
        placeholder="e.g., We sell premium organic coffee blends online to customers worldwide...", 
        height=110, 
        label_visibility="collapsed"
    )
    
    st.markdown('<div class="section-title">2. Choose Tone</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Select the tone you want</div>', unsafe_allow_html=True)
    selected_tone = st.selectbox("Tone Select", ["Luxury 💎", "Professional 💼", "Aggressive Sales 🚨", "Friendly 😊"], label_visibility="collapsed")
    
    st.markdown('<div class="section-title">3. Business Goal</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">What do you want to achieve?</div>', unsafe_allow_html=True)
    selected_goal = st.selectbox("Goal Select", ["Increase Sales 📈", "Brand Awareness 🌍", "Get Leads 🎯"], label_visibility="collapsed")
    
    # Auto Language Badge UI Simulated
    st.markdown('<br><span class="section-title">Language</span>'
                '<span class="badge-lang">Auto-Detect</span>', unsafe_allow_html=True)
    st.write("")
    
    generate_click = st.button("✨ Generate Marketing Content", use_container_width=True)
    
    # Tip Box
    st.markdown("""
        <div class="tip-box">
            💡 <b>Tip: Write in any language.</b> Brightins will detect the language and generate content in the same language.
        </div>
    """, unsafe_allow_html=True)

# 6. RIGHT COLUMN: OUTPUT PANEL (STACKED CARDS STYLE WITH COPY & DOWNLOAD)
with col_output:
    st.markdown('<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">'
                '<span style="font-size: 18px; font-weight: 700; color: #111827;">✨ Your Generated Content</span>'
                '</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 13px; color: #6B7280; margin-top: -5px; margin-bottom: 1.5rem;">AI-generated content tailored for your business</p>', unsafe_allow_html=True)
    
    # Trigger the simulation if clicked
    if generate_click:
        with st.spinner("Brightins AI Engine is writing..."):
            res = generate_posts_mockup(biz_description, selected_tone, selected_goal)
            st.session_state['mock_res'] = res
            st.session_state['mock_ready'] = True
    
    # Display outputs if ready
    if st.session_state.get('mock_ready', False):
        res_data = st.session_state['mock_res']
        
        # --- CARD 1: FACEBOOK ---
        st.markdown('<div class="result-card"><div class="card-header"><div class="card-title">📘 Facebook Post</div></div>', unsafe_allow_html=True)
        st.text_area("FB Txt", res_data["fb"], height=120, label_visibility="collapsed", key="fb_area")
        
        # Action Buttons side-by-side
        btn_fb_1, btn_fb_2 = st.columns(2)
        with btn_fb_1:
            if st.button("📋 Copy Post", key="cp_fb", use_container_width=True):
                st.toast("Copied to clipboard! 📋")
        with btn_fb_2:
            st.download_button(label="📥 Download Post", data=res_data["fb"], file_name="facebook_post.txt", mime="text/plain", use_container_width=True, key="dl_fb")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- CARD 2: INSTAGRAM ---
        st.markdown('<div class="result-card"><div class="card-header"><div class="card-title">📸 Instagram Caption</div></div>', unsafe_allow_html=True)
        st.text_area("IG Txt", res_data["ig"], height=120, label_visibility="collapsed", key="ig_area")
        
        # Action Buttons side-by-side
        btn_ig_1, btn_ig_2 = st.columns(2)
        with btn_ig_1:
            if st.button("📋 Copy Caption", key="cp_ig", use_container_width=True):
                st.toast("Copied to clipboard! 📋")
        with btn_ig_2:
            st.download_button(label="📥 Download Caption", data=res_data["ig"], file_name="instagram_caption.txt", mime="text/plain", use_container_width=True, key="dl_ig")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- CARD 3: X (TWITTER) ---
        st.markdown('<div class="result-card"><div class="card-header"><div class="card-title">𝕏 X (Twitter) Post</div></div>', unsafe_allow_html=True)
        st.text_area("X Txt", res_data["x"], height=90, label_visibility="collapsed", key="x_area")
        
        # Action Buttons side-by-side
        btn_x_1, btn_x_2 = st.columns(2)
        with btn_x_1:
            if st.button("📋 Copy Post", key="cp_x", use_container_width=True):
                st.toast("Copied to clipboard! 📋")
        with btn_x_2:
            st.download_button(label="📥 Download Post", data=res_data["x"], file_name="x_post.txt", mime="text/plain", use_container_width=True, key="dl_x")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- BOTTOM STATUS BAR ---
        st.markdown(f"""
            <div class="status-bar">
                <span>✅ Content generated successfully in <b>{res_data["lang"]}</b></span>
                <span style="color: #6B7280; font-size: 11px;">Just now</span>
            </div>
        """, unsafe_allow_html=True)
        
    else:
        st.info("Your beautifully formatted Facebook, Instagram, and X marketing posts will appear here sequentially after you hit the generate button.")