import streamlit as st

# 1. Page Configuration (Set to wide layout to match the mockup)
st.set_page_config(
    page_title="Brightins - AI Marketing Employee",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar Navigation (Matching the left menu of your mockup)
with st.sidebar:
    st.title("✨ Brightins")
    st.caption("Your Global AI Marketing Employee")
    st.space = st.write("") # Spacer
    
    # Navigation Buttons (Visual representation for MVP)
    st.button("🔮 Generate Content", use_container_width=True, type="primary")
    st.button("⏳ My History", use_container_width=True, disabled=True)
    st.button("💾 Saved Content", use_container_width=True, disabled=True)
    
    st.divider()
    st.caption("© 2026 Brightins. All rights reserved.")

# 3. Main Workspace Split (Left: Input, Right: Output)
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
    
    st.write("") # Spacer
    generate_btn = st.button("✨ Generate Marketing Content", type="primary", use_container_width=True)
    
    st.info("💡 **Tip:** Write in any language. Brightins will automatically detect the language and generate content in the same language.")

# ================= RIGHT COLUMN: OUTPUT =================
with col_output:
    st.header("✨ Your Generated Content")
    st.write("AI-generated content tailored for your business.")
    
    if generate_btn:
        if not business_description.strip():
            st.error("Please provide a business description on the left side before generating.")
        else:
            st.success("Content generated successfully! Scroll through the tabs below.")
            
            # Output Tabs
            tab_fb, tab_ig, tab_x, tab_tiktok = st.tabs([
                "📘 Facebook Post", 
                "📸 Instagram Caption", 
                "🐦 X (Twitter) Post", 
                "🎵 TikTok Script"
            ])
            
            # Universal tags appended inside the posts automatically
            sample_hashtags = "\n\n#Business #Marketing #AI #SaaS #Growth #Brightins"
            
            with tab_fb:
                st.subheader("Facebook Post")
                mock_fb = f"[Mock Facebook Post Content]\n\nTargeted Campaign for: {business_description}\nTone Settings: {tone}\nCampaign Objective: {goal}{sample_hashtags}"
                st.text_area(label="Content Display", value=mock_fb, height=180, key="fb_text", label_visibility="collapsed")
                
                # Action buttons stacked correctly below
                st.button("📋 Copy to Clipboard", key="btn_copy_fb", use_container_width=True)
                st.download_button("📥 Download File", data=mock_fb, file_name="facebook_post.txt", mime="text/plain", key="btn_dl_fb", use_container_width=True)
                
            with tab_ig:
                st.subheader("Instagram Caption")
                mock_ig = f"[Mock Instagram Caption]\n\nPremium quality tailored directly for you! ✨\nDesigned for: {business_description}\nTone: {tone}{sample_hashtags}"
                st.text_area(label="Content Display", value=mock_ig, height=180, key="ig_text", label_visibility="collapsed")
                
                st.button("📋 Copy to Clipboard", key="btn_copy_ig", use_container_width=True)
                st.download_button("📥 Download File", data=mock_ig, file_name="instagram_caption.txt", mime="text/plain", key="btn_dl_ig", use_container_width=True)
                
            with tab_x:
                st.subheader("X (Twitter) Post")
                mock_x = f"[Mock X Post]\n\nTransforming results through smart automation. Let's make it happen. 🔥{sample_hashtags}"
                st.text_area(label="Content Display", value=mock_x, height=120, key="x_text", label_visibility="collapsed")
                
                st.button("📋 Copy to Clipboard", key="btn_copy_x", use_container_width=True)
                st.download_button("📥 Download File", data=mock_x, file_name="x_post.txt", mime="text/plain", key="btn_dl_x", use_container_width=True)
                
            with tab_tiktok:
                st.subheader("TikTok Video Script")
                mock_tiktok = (
                    f"🎬 **[HOOK]:** Stop scrolling if you want to scale your business today!\n\n"
                    f"📝 **[BODY]:** Here is exactly how our solution changes the game for you.\n\n"
                    f"📣 **[CTA]:** Check the link in our description to get started now!\n\n"
                    f"🏷️ **Tags:** {sample_hashtags.strip()}"
                )
                st.markdown(mock_tiktok)
                
                st.button("📋 Copy Script", key="btn_copy_tiktok", use_container_width=True)
                st.download_button("📥 Download Script", data=mock_tiktok, file_name="tiktok_script.txt", mime="text/plain", key="btn_dl_tiktok", use_container_width=True)
    else:
        # State before user clicks Generate
        st.info("Provide your business profile details on the left and click 'Generate' to view your social media campaigns here.")