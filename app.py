import streamlit as st

# 1. Page Configuration (Tsarin yadda shafin zai bayyana)
st.set_page_config(
    page_title="Brightins - AI Marketing Employee",
    page_icon="🚀",
    layout="centered"
)

# 2. Header Section (Bayanai na saman shafi)
st.title("🚀 Brightins")
st.subheader("Your Global AI Marketing Employee")
st.write("Bayyana kasuwancinka da harshenka, Brightins zai samar maka da tallan da ya dace.")

st.divider()

# 3. User Inputs Section (Wajen da mai amfani zai shigar da bayanai)
st.header("📋 Bayanan Kasuwanci")

# Input 1: Business Description
business_description = st.text_area(
    label="Mene ne kasuwancinka? (Misali: Ina sayar da takalma a Kano / I sell perfumes in Abuja)",
    placeholder="Rubuta bayani anan...",
    height=150
)

# Layout for columns (Raba shafin gida biyu don dropdowns)
col1, col2 = st.columns(2)

with col1:
    # Input 2: Tone Selection
    tone = st.selectbox(
        label="Zaɓi Yanayin Magana (Tone)",
        options=["Professional", "Friendly", "Luxury", "Aggressive Sales"]
    )

with col2:
    # Input 3: Business Goal
    goal = st.selectbox(
        label="Zaɓi Manufar Tallan (Goal)",
        options=["Increase Sales", "Brand Awareness", "Lead Generation", "Product Launch", "Customer Retention"]
    )

st.divider()

# 4. Action Button (Maballin rura wuta)
if st.button("Generate Marketing Content", type="primary", use_container_width=True):
    
    if not business_description.strip():
        st.warning("Don Allah rubuta bayanin kasuwancinka kafin ka danna maballin.")
    else:
        st.success("🤖 Brightins ya kammala tsara tallanka! Ga sakamakon nan a ƙasa:")
        
        # 5. Output Tabs (Wajen nuna sakamako daban-daban)
        tab_fb, tab_ig, tab_x, tab_tiktok, tab_tags = st.tabs([
            "📘 Facebook Post", 
            "📸 Instagram Caption", 
            "🐦 X (Twitter) Post", 
            "🎵 TikTok Script", 
            "🏷️ Hashtags"
        ])
        
        # Lokacin da aka haɗa da OpenAI a Mako na 2, waɗannan bayanan za su canza na gaske
        with tab_fb:
            st.subheader("Facebook Post")
            mock_fb = f"🤖 [Wannan misali ne na Facebook Post]\n\nKasuwanci: {business_description}\nYanayi: {tone}\nManufa: {goal}\n\nKwanan nan ainihin tallan zai fito anan!"
            st.text_area(label="Copy Facebook Content", value=mock_fb, height=150, key="fb_text")
            st.button("Copy to Clipboard", key="btn_fb")
            
        with tab_ig:
            st.subheader("Instagram Caption")
            mock_ig = f"🤖 [Wannan misali ne na Instagram Caption]\n\nDubi kyawun kayanmu! ✨\nYanayi: {tone}\nManufa: {goal}"
            st.text_area(label="Copy Instagram Content", value=mock_ig, height=150, key="ig_text")
            st.button("Copy to Clipboard", key="btn_ig")
            
        with tab_x:
            st.subheader("X (Twitter) Post")
            mock_x = f"🤖 [Wannan misali ne na X Post]\n\nKasuwancinmu yana bunkasa. Ko kun shirya? 🔥 #Brightins"
            st.text_area(label="Copy X Content", value=mock_x, height=100, key="x_text")
            st.button("Copy to Clipboard", key="btn_x")
            
        with tab_tiktok:
            st.subheader("TikTok Video Script")
            mock_tiktok = (
                f"🎬 **[HOOK]:** Minti 3 na farko da zai tsayar da mai kallo!\n\n"
                f"📝 **[BODY]:** Bayanin yadda {business_description} zai canza rayuwarsu.\n\n"
                f"📣 **[CTA]:** Danna link na bio namu yanzu domin yin oda!"
            )
            st.markdown(mock_tiktok)
            st.button("Copy Script", key="btn_tiktok")
            
        with tab_tags:
            st.subheader("Relevant Hashtags")
            mock_tags = "#Kasuwanci #Marketing #AI #Startup #GlobalBusiness"
            st.text_area(label="Copy Hashtags", value=mock_tags, height=80, key="tags_text")
            st.button("Copy Hashtags", key="btn_tags")