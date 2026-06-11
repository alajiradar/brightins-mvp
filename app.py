import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Brightins - AI Marketing Employee",
    layout="wide"
)

# 2. INJECT CUSTOM CSS: Wannan shi ne zai tilasta kalar Purple a jikin kowane Button da layukan zagayawa (No more Red!)
st.markdown("""
    <style>
    /* Canza kalar manyan maballai (Primary Buttons) zuwa Purple */
    button[kind="primary"] {
        background-color: #7C3AED !important;
        color: white !important;
        border: 1px solid #7C3AED !important;
    }
    button[kind="primary"]:hover {
        background-color: #6D28D9 !important;
        color: white !important;
    }
    
    /* Canza kalar layin da ke zagaye akwatin rubutu lokacin da aka danna shi (Focus Border) */
    textarea:focus, select:focus, input:focus {
        border-color: #7C3AED !important;
        box-shadow: 0 0 0 1px #7C3AED !important;
    }
    
    /* Gyara launukan Tabs */
    button[data-baseweb="tab"] p {
        color: #0F172A !important;
    }
    button[aria-selected="true"] {
        border-bottom-color: #7C3AED !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. INITIALIZE SESSION STATE (Kwakwalwar Ajiya don kada rubutu ya riƙa ɓacewa)
if "generated" not in st.session_state:
    st.session_state.generated = False
    st.session_state.fb_content = ""
    st.session_state.ig_content = ""
    st.session_state.x_content = ""
    st.session_state.tiktok_content = ""

# 4. Sidebar Navigation
with st.sidebar:
    st.title("✨ Brightins")
    st.caption("Your Global AI Marketing Employee")
    st.write("") 
    
    st.button("🔮 Generate Content", use_container_width=True, type="primary")
    st.button("⏳ My History", use_container_width=True, disabled=True)
    st.button("💾 Saved Content", use_container_width=True, disabled=True)
    
    st.divider()
    st.caption("© 2026 Brightins. All rights reserved.")

# 5. Main Workspace Split (Left: Input, Right: Output)
col_input, col_output = st.columns([1, 1.3], gap="large")

# ================= LEFT COLUMN: INPUT =================
with col_input:
    st.header("Welcome to Brightins 👋")
    st.write("Create powerful marketing content for your business in any language.")
    
    st.subheader("1. Describe Your Business")
    business_description = st.text_area(
        label="Tell us about your business or product:",
        placeholder="Type here (e.g., 'I sell luxury perfumes in London' or any language you prefer...)",
        height=180
    )
    
    st.subheader("2. Choose Tone")
    tone = st.selectbox(
        label="Select the tone you want:",
        options=["Professional", "Friendly", "Luxury", "Aggressive Sales"]
    )
    
    st.subheader("3. Business Goal")
    goal = st.selectbox(
        label="What do you want to achieve?",
        options=["Increase Sales", "Brand Awareness", "Lead Generation", "Product Launch", "Customer Retention"]
    )
    
    st.write("") 
    generate_btn = st.button("✨ Generate Marketing Content", type="primary", use_container_width=True)
    
    st.info("💡 **Tip:** Write in any language. Brightins will automatically detect the language and generate content in the same language.")

# Trigger Generation State
if generate_btn:
    if not business_description.strip():
        st.error("Please provide a business description on the left side before generating.")
    else:
        # Adana sakamakon a cikin Session State don karka goge
        st.session_state.generated = True
        sample_hashtags = "\n\n#Business #Marketing #AI #SaaS #Growth #Brightins"
        
        st.session_state.fb_content = f"[Mock Facebook Post Content]\n\nTargeted Campaign for: {business_description}\nTone Settings: {tone}\nCampaign Objective: {goal}{sample_hashtags}"
        st.session_state.ig_content = f"[Mock Instagram Caption]\n\nPremium quality tailored directly for you! ✨\nDesigned for: {business_description}\nTone: {tone}{sample_hashtags}"
        st.session_state.x_content = f"[Mock X Post]\n\nTransforming results through smart automation. Let's make it happen. 🔥{sample_hashtags}"
        st.session_state.tiktok_content = (
            f"🎬 **[HOOK]:** Stop scrolling if you want to scale your business today!\n\n"
            f"📝 **[BODY]:** Here is exactly how our solution changes the game for you.\n\n"
            f"📣 **[CTA]:** Check the link in our description to get started now!\n\n"
            f"🏷️ **Tags:** {sample_hashtags.strip()}"
        )

# ================= RIGHT COLUMN: OUTPUT =================
with col_output:
    st.header("✨ Your Generated Content")
    st.write("AI-generated content tailored for your business.")
    
    # Bincika idan akwai ajiyeccen bayani a kwakwalwar shafi (Session State)
    if st.session_state.generated:
        st.success("Content generated successfully! Scroll through the tabs below.")
        
        tab_fb, tab_ig, tab_x, tab_tiktok = st.tabs([
            "📘 Facebook Post", 
            "📸 Instagram Caption", 
            "🐦 X (Twitter) Post", 
            "🎵 TikTok Script"
        ])
        
        with tab_fb:
            st.subheader("Facebook Post")
            # Lura: Streamlit yana da alamar "Copy" ta asali a saman kowane akwatin rubutu (Text Area) idan ka kai kursor kai
            st.text_area(label="FB text", value=st.session_state.fb_content, height=180, key="fb_text_area", label_visibility="collapsed")
            st.download_button("📥 Download File", data=st.session_state.fb_content, file_name="facebook_post.txt", mime="text/plain", key="btn_dl_fb", use_container_width=True)
            
        with tab_ig:
            st.subheader("Instagram Caption")
            st.text_area(label="IG text", value=st.session_state.ig_content, height=180, key="ig_text_area", label_visibility="collapsed")
            st.download_button("📥 Download File", data=st.session_state.ig_content, file_name="instagram_caption.txt", mime="text/plain", key="btn_dl_ig", use_container_width=True)
            
        with tab_x:
            st.subheader("X (Twitter) Post")
            st.text_area(label="X text", value=st.session_state.x_content, height=120, key="x_text_area", label_visibility="collapsed")
            st.download_button("📥 Download File", data=st.session_state.x_content, file_name="x_post.txt", mime="text/plain", key="btn_dl_x", use_container_width=True)
            
        with tab_tiktok:
            st.subheader("TikTok Video Script")
            st.text_area(label="TikTok text", value=st.session_state.tiktok_content, height=180, key="tk_text_area", label_visibility="collapsed")
            st.download_button("📥 Download Script", data=st.session_state.tiktok_content, file_name="tiktok_script.txt", mime="text/plain", key="btn_dl_tiktok", use_container_width=True)
    else:
        st.info("Provide your business profile details on the left and click 'Generate' to view your social media campaigns here.")