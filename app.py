import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Brightins - AI Marketing Employee",
    layout="centered"
)

# 2. Header Section (Clean and Simple - No Icon)
st.title("Brightins")
st.subheader("Your Global AI Marketing Employee")
st.write("Describe your business in any language, and Brightins will generate your tailored social media marketing campaign instantly.")

st.divider()

# 3. User Inputs Section (Fully in English)
st.header("Business Profile")

# Input 1: Business Description
business_description = st.text_area(
    label="What is your business about? (e.g., 'Ina sayar da takalma a Kano' or 'I sell luxury perfumes in Abuja')",
    placeholder="Type your business description here...",
    height=150
)

# Layout for inputs
col1, col2 = st.columns(2)

with col1:
    # Input 2: Tone Selection
    tone = st.selectbox(
        label="Select Tone",
        options=["Professional", "Friendly", "Luxury", "Aggressive Sales"]
    )

with col2:
    # Input 3: Business Goal
    goal = st.selectbox(
        label="Select Marketing Goal",
        options=["Increase Sales", "Brand Awareness", "Lead Generation", "Product Launch", "Customer Retention"]
    )

st.divider()

# 4. Action Button (Color is now managed globally by config.toml)
if st.button("Generate Marketing Content", type="primary", use_container_width=True):
    
    if not business_description.strip():
        st.warning("Please provide a business description before generating content.")
    else:
        st.success("🤖 Brightins has successfully generated your marketing content!")
        
        # 5. Output Tabs (Hashtags tab removed as requested)
        tab_fb, tab_ig, tab_x, tab_tiktok = st.tabs([
            "📘 Facebook Post", 
            "📸 Instagram Caption", 
            "🐦 X (Twitter) Post", 
            "🎵 TikTok Script"
        ])
        
        # Global Hashtags that will automatically append to each post
        sample_hashtags = "\n\n#Business #Marketing #AI #SaaS #Growth #Brightins"
        
        with tab_fb:
            st.subheader("Facebook Post")
            mock_fb = f"[Mock Facebook Post Content]\n\nBusiness: {business_description}\nTone: {tone}\nGoal: {goal}{sample_hashtags}"
            st.text_area(label="Copy Facebook Content", value=mock_fb, height=200, key="fb_text")
            st.button("Copy to Clipboard", key="btn_fb")
            
        with tab_ig:
            st.subheader("Instagram Caption")
            mock_ig = f"[Mock Instagram Caption]\n\nElevate your lifestyle with the best offers today! ✨\nTone: {tone}\nGoal: {goal}{sample_hashtags}"
            st.text_area(label="Copy Instagram Content", value=mock_ig, height=200, key="ig_text")
            st.button("Copy to Clipboard", key="btn_ig")
            
        with tab_x:
            st.subheader("X (Twitter) Post")
            mock_x = f"[Mock X Post]\n\nReady to transform your business results? Let's get started. 🔥{sample_hashtags}"
            st.text_area(label="Copy X Content", value=mock_x, height=150, key="x_text")
            st.button("Copy to Clipboard", key="btn_x")
            
        with tab_tiktok:
            st.subheader("TikTok Video Script")
            # For TikTok script, we append hashtags to the end of the markdown content naturally
            mock_tiktok = (
                f"🎬 **[HOOK]:** Stop scrolling if you want to scale your business today!\n\n"
                f"📝 **[BODY]:** Here is exactly how {business_description} changes the game for you.\n\n"
                f"📣 **[CTA]:** Click the link in our bio to order yours right now!\n\n"
                f"🏷️ **Hashtags:** {sample_hashtags.strip()}"
            )
            st.markdown(mock_tiktok)
            st.button("Copy Script", key="btn_tiktok")