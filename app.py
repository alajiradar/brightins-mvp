import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Brightins - AI Marketing Employee",
    layout="wide"
)

# 2. INJECT SIMPLE & NEUTRAL CSS: Wannan shi ne zai kashe jan layi da kalar purple gaba ɗaya
st.markdown("""
    <style>
    /* Canza dukkan Primary Buttons zuwa kalar Slate mai sauƙi (Minimalist Dark Theme) */
    button[kind="primary"] {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 1px solid #1E293B !important;
        border-radius: 6px !important;
    }
    button[kind="primary"]:hover {
        background-color: #334155 !important;
        color: #FFFFFF !important;
    }
    
    /* KASHE JAN LAYI: Yanzu idan mutum ya danna akwatin rubutu, zai zagaye da kalar Slate mai sanyi */
    textarea:focus, select:focus, input:focus, 
    div[data-baseweb="textarea"]:focus-within, 
    div[data-baseweb="select"]:focus-within {
        border-color: #1E293B !important;
        box-shadow: 0 0 0 1px #1E293B !important;
    }
    
    /* Daidaita kalar tab indicators */
    button[aria-selected="true"] {
        border-bottom-color: #1E293B !important;
    }
    div[data-baseweb="tab-highlight"] {
        background-color: #1E293B !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. INITIALIZE SESSION STATE (Ajiye bayanan da aka samar domin kada su riƙa ɓacewa)
if "generated" not in st.session_state:
    st.session_state.generated = False
    st.session_state.fb_content = ""
    st.session_state.ig_content = ""
    st.session_state.x_content = ""
    st.session_state.tiktok_content = ""

# 4. Sidebar Navigation (Left Side Menu)
with st.sidebar:
    st.title("✨ Brightins")
    st.caption("Your Global AI Marketing Employee")
    st.write("") 
    
    st.button("🔮 Generate Content", use_container_width=True, type="primary")
    st.button("⏳ My History", use_container_width=True, disabled=True)
    st.button("💾 Saved Content", use_container_width=True, disabled=True)
    
    st.divider()
    st.caption("© 2026 Brightins. All rights reserved.")

# 5. Workspace Layout Grid (Hagu: Shigarwa, Dama: Fitarwa)
col_input, col_output = st.columns([1, 1.3], gap="large")

# ================= ƁANGAREN HAGU: USER INPUTS =================
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

# Kula da danna maballin Generate: Muna adana bayanan ne a state
if generate_btn:
    if not business_description.strip():
        st.error("Please provide a business description on the left side before generating.")
    else:
        st.session_state.generated = True
        sample_hashtags = "\n\n#Business #Marketing #AI #SaaS #Growth #Brightins"
        
        st.session_state.fb_content = f"[Mock Facebook Post Content]\n\nTargeted Campaign for: {business_description}\nTone Settings: {tone}\nCampaign Objective: {goal}{sample_hashtags}"
        st.session_state.ig_content = f"[Mock Instagram Caption]\n\nPremium quality tailored directly for you! ✨\nDesigned for: {business_description}\nTone: {tone}{sample_hashtags}"
        st.session_state.x_content = f"[Mock X Post]\n\nTransforming results through smart automation. Let's make it happen. 🔥{sample_hashtags}"
        st.session_state.tiktok_content = (
            f"🎬 **[HOOK]:** Stop scrolling if you want to scale your business today!\n\n"
            f"📝 **[BODY]:** Here is exactly how our solution changes the game for you.\n\n"
            f"📣 **[CTA]:** Check the link in our description to get started now!\n\n"
            f"🏷 *Tags:* {sample_hashtags.strip()}"
        )

# ================= ƁANGAREN DAMA: OUTPUTS GENERATED =================
with col_output:
    st.header("✨ Your Generated Content")
    st.write("AI-generated content tailored for your business.")
    
    # Tsarin nuna sakamako ta hanyar karantawa daga Session State (Baya gogewa)
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
            st.text_area(label="FB text", value=st.session_state.fb_content, height=180, key="fb_text_area", label_visibility="collapsed")
            
            # Action Buttons a jere masu kyan gani
            btn_copy_fb = st.button("📋 Copy Content", key="btn_copy_fb", use_container_width=True)
            if btn_copy_fb:
                st.toast("Copied to clipboard! (Or use the built-in copy icon on top right)")
            st.download_button("📥 Download File", data=st.session_state.fb_content, file_name="facebook_post.txt", mime="text/plain", key="btn_dl_fb", use_container_width=True)
            
        with tab_ig:
            st.subheader("Instagram Caption")
            st.text_area(label="IG text", value=st.session_state.ig_content, height=180, key="ig_text_area", label_visibility="collapsed")
            
            btn_copy_ig = st.button("📋 Copy Content", key="btn_copy_ig", use_container_width=True)
            if btn_copy_ig:
                st.toast("Copied to clipboard!")
            st.download_button("📥 Download File", data=st.session_state.ig_content, file_name="instagram_caption.txt", mime="text/plain", key="btn_dl_ig", use_container_width=True)
            
        with tab_x:
            st.subheader("X (Twitter) Post")
            st.text_area(label="X text", value=st.session_state.x_content, height=120, key="x_text_area", label_visibility="collapsed")
            
            btn_copy_x = st.button("📋 Copy Content", key="btn_copy_x", use_container_width=True)
            if btn_copy_x:
                st.toast("Copied to clipboard!")
            st.download_button("📥 Download File", data=st.session_state.x_content, file_name="x_post.txt", mime="text/plain", key="btn_dl_x", use_container_width=True)
            
        with tab_tiktok:
            st.subheader("TikTok Video Script")
            st.text_area(label="TikTok text", value=st.session_state.tiktok_content, height=180, key="tk_text_area", label_visibility="collapsed")
            
            btn_copy_tk = st.button("📋 Copy Script", key="btn_copy_tk", use_container_width=True)
            if btn_copy_tk:
                st.toast("Script copied to clipboard!")
            st.download_button("📥 Download Script", data=st.session_state.tiktok_content, file_name="tiktok_script.txt", mime="text/plain", key="btn_dl_tiktok", use_container_width=True)
    else:
        st.info("Provide your business profile details on the left and click 'Generate' to view your social media campaigns here.")