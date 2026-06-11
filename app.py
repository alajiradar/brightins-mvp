import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Brightins - AI Marketing Employee",
    layout="wide"
)

# 2. INJECT SIMPLE & NEUTRAL CSS (Don kiyaye kyawun launuka da kashe jan layi)
st.markdown("""
    <style>
    /* Manyan maballai na Slate Black */
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
    
    /* Hana fitar jan layi lokacin da aka danna akwatin rubutu */
    textarea:focus, select:focus, input:focus, 
    div[data-baseweb="textarea"]:focus-within, 
    div[data-baseweb="select"]:focus-within {
        border-color: #1E293B !important;
        box-shadow: 0 0 0 1px #1E293B !important;
    }
    
    /* Daidaita kalar Tabs indicators */
    button[aria-selected="true"] {
        border-bottom-color: #1E293B !important;
    }
    div[data-baseweb="tab-highlight"] {
        background-color: #1E293B !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. JAVASCRIPT REAL COPY BUTTON FUNCTION
# Wannan aikin zai samar da maballin Copy na gaske wanda ba ya tayar da loda shafi
def render_js_copy_button(text_to_copy, button_label="📋 Copy Content"):
    # Gyara rubutu don kada ya karfafa muryar lambobin JS
    safe_text = text_to_copy.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
    
    html_code = f"""
    <button id="copyScriptBtn" style="
        width: 100%;
        background-color: #1E293B;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 14px;
        font-weight: 500;
        transition: background-color 0.2s;
    ">{button_label}</button>

    <script>
    document.getElementById('copyScriptBtn').addEventListener('click', function() {{
        const textArea = document.createElement('textarea');
        textArea.value = `{safe_text}`;
        document.body.appendChild(textArea);
        textArea.select();
        
        try {{
            document.execCommand('copy');
            const btn = document.getElementById('copyScriptBtn');
            const originalText = btn.innerText;
            btn.innerText = "✅ Copied to Clipboard!";
            btn.style.backgroundColor = "#10B981"; // Canza zuwa Green na nasara
            
            setTimeout(() => {{
                btn.innerText = originalText;
                btn.style.backgroundColor = "#1E293B";
            }}, 2000);
        }} catch (err) {{
            alert('Oops, unable to copy');
        }}
        
        document.body.removeChild(textArea);
    }});
    </script>
    """
    components.html(html_code, height=45)

# 4. INITIALIZE SESSION STATE (Kwakwalwar Ajiya)
if "generated" not in st.session_state:
    st.session_state.generated = False
    st.session_state.fb_content = ""
    st.session_state.ig_content = ""
    st.session_state.x_content = ""
    st.session_state.tiktok_content = ""

# 5. Sidebar Navigation
with st.sidebar:
    st.title("✨ Brightins")
    st.caption("Your Global AI Marketing Employee")
    st.write("") 
    
    st.button("🔮 Generate Content", use_container_width=True, type="primary")
    st.button("⏳ My History", use_container_width=True, disabled=True)
    st.button("💾 Saved Content", use_container_width=True, disabled=True)
    
    st.divider()
    st.caption("© 2026 Brightins. All rights reserved.")

# 6. Main Layout Grid Split
col_input, col_output = st.columns([1, 1.3], gap="large")

# ================= ƁANGAREN HAGU: INPUTS =================
with col_input:
    st.header("Welcome to Brightins 👋")
    st.write("Create powerful marketing content for your business in any language.")
    
    st.subheader("1. Describe Your Business")
    # Muna amfani da key domin Streamlit ya riƙe canjin rubutu ko da yaushe
    business_description = st.text_area(
        label="Tell us about your business or product:",
        placeholder="Type here (e.g., 'I sell luxury perfumes in London'...)",
        height=180,
        key="user_biz_input"
    )
    
    st.subheader("2. Choose Tone")
    tone = st.selectbox(
        label="Select the tone you want:",
        options=["Professional", "Friendly", "Luxury", "Aggressive Sales"],
        key="user_tone_input"
    )
    
    st.subheader("3. Business Goal")
    goal = st.selectbox(
        label="What do you want to achieve?",
        options=["Increase Sales", "Brand Awareness", "Lead Generation", "Product Launch", "Customer Retention"],
        key="user_goal_input"
    )
    
    st.write("") 
    generate_btn = st.button("✨ Generate Marketing Content", type="primary", use_container_width=True)
    st.info("💡 **Tip:** Write in any language. Brightins will automatically detect the language and generate content.")

# Sarrafa danna Generate: Lokacin da aka danna, kowane lokaci zai ɗauki sabon rubutun hagu baki ɗaya!
if generate_btn:
    if not business_description.strip():
        st.error("Please provide a business description on the left side before generating.")
    else:
        st.session_state.generated = True
        sample_hashtags = "\n\n#Business #Marketing #AI #SaaS #Growth #Brightins"
        
        # Sabunta ainihin bayanan state da sabon rubutun da aka shigar
        st.session_state.fb_content = f"[Mock Facebook Post Content]\n\nTargeted Campaign for: {business_description}\nTone Settings: {tone}\nCampaign Objective: {goal}{sample_hashtags}"
        st.session_state.ig_content = f"[Mock Instagram Caption]\n\nPremium quality tailored directly for you! ✨\nDesigned for: {business_description}\nTone: {tone}{sample_hashtags}"
        st.session_state.x_content = f"[Mock X Post]\n\nTransforming results through smart automation for {business_description}. Let's make it happen. 🔥{sample_hashtags}"
        st.session_state.tiktok_content = (
            f"🎬 **[HOOK]:** Stop scrolling if you want to scale your business today!\n\n"
            f"📝 **[BODY]:** Here is exactly how we deliver values for {business_description}.\n\n"
            f"📣 **[CTA]:** Check the link in our description to get started now!\n\n"
            f"🏷️ *Tags:* {sample_hashtags.strip()}"
        )

# ================= ƁANGAREN DAMA: OUTPUTS =================
with col_output:
    st.header("✨ Your Generated Content")
    st.write("AI-generated content tailored for your business.")
    
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
            
            # Kiran sabon maballin Copy na JavaScript
            render_js_copy_button(st.session_state.fb_content, "📋 Copy Facebook Content")
            st.download_button("📥 Download File", data=st.session_state.fb_content, file_name="facebook_post.txt", mime="text/plain", key="btn_dl_fb", use_container_width=True)
            
        with tab_ig:
            st.subheader("Instagram Caption")
            st.text_area(label="IG text", value=st.session_state.ig_content, height=180, key="ig_text_area", label_visibility="collapsed")
            
            render_js_copy_button(st.session_state.ig_content, "📋 Copy Instagram Content")
            st.download_button("📥 Download File", data=st.session_state.ig_content, file_name="instagram_caption.txt", mime="text/plain", key="btn_dl_ig", use_container_width=True)
            
        with tab_x:
            st.subheader("X (Twitter) Post")
            st.text_area(label="X text", value=st.session_state.x_content, height=120, key="x_text_area", label_visibility="collapsed")
            
            render_js_copy_button(st.session_state.x_content, "📋 Copy X Content")
            st.download_button("📥 Download File", data=st.session_state.x_content, file_name="x_post.txt", mime="text/plain", key="btn_dl_x", use_container_width=True)
            
        with tab_tiktok:
            st.subheader("TikTok Video Script")
            st.text_area(label="TikTok text", value=st.session_state.tiktok_content, height=180, key="tk_text_area", label_visibility="collapsed")
            
            render_js_copy_button(st.session_state.tiktok_content, "📋 Copy TikTok Script")
            st.download_button("📥 Download Script", data=st.session_state.tiktok_content, file_name="tiktok_script.txt", mime="text/plain", key="btn_dl_tiktok", use_container_width=True)
    else:
        st.info("Provide your business profile details on the left and click 'Generate' to view your social media campaigns here.")