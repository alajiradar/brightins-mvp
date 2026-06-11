import streamlit as st
import streamlit.components.v1 as components
import time

# ── 1. PAGE CONFIGURATION ─────────────────────────────────────────────────────
# Streamlit zai yi amfani da native theme dinsa na asali yanzu
st.set_page_config(page_title="Brightins", page_icon="🚀", layout="wide")

# ── 2. WEB APP META TAGS ──────────────────────────────────────────────────────
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

# ── 3. HIDE FOOTER ONLY ──────────────────────────────────────────────────────
# Mun bar MainMenu da Header a bude kadan domin users su iya canza Theme idan suna so
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# ── 4. TOP BAR ───────────────────────────────────────────────────────────────
top_left, top_right = st.columns([3, 1])

with top_left:
    st.title("Brightins 🚀")
    st.subheader("Your Global AI Marketing Employee")

with top_right:
    # Wuri ne don sanya abubuwa na gaba (kamar zabar Yare)
    st.write("")

st.write("---")


# ══════════════════════════════════════════════════════════════════════════════
# APPLICATION LOGIC
# ══════════════════════════════════════════════════════════════════════════════

# ── 5. LOCAL AI SIMULATOR ENGINE ─────────────────────────────────────────────
def generate_social_posts_local(business_description, tone, business_goal):
    time.sleep(1.2)

    desc       = business_description.strip() if business_description.strip() else "our premium products"
    desc_lower = desc.lower()

    hausa_keywords = [
        "takalma", "saida", "kano", "turare", "yadi", "shadda", "atamfa",
        "kaya", "kudi", "maka", "kuna", "mun", "ina", "tsada", "bunkasa", "kasuwanci",
    ]
    is_hausa = any(word in desc_lower for word in hausa_keywords)

    if is_hausa:
        cta_text  = "Turo mana saƙon gaggawa (DM) yanzu a nan don ka mallaki naka! 📥"
        body_text = (
            f"Kuna neman mafi kyau? Ga cikakken bayani akan {desc}. "
            "Muna tabbatar muku da inganci da gaskiya a kowane lokaci domin gamsuwarku."
        )
        hashtags = "#Kasuwanci #Kano #Inganci #Arewa"
        fb = f"🚀 [Brightins AI Engine - Tone: {tone}]\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        ig = f"✨ Kasuwancinmu na gari (Goal: {business_goal}) ✨\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        tw = f"{body_text}\n\n{cta_text} {hashtags}"
        tt = (
            f"🎥 [TikTok/Shorts Script - Daƙiƙa 60]\nTone: {tone}\n\n"
            f"[0-15s - HOOK]: 'Tsaya ka saurara! Idan kana son bunkasa kasuwancinka a Intanet, wannan bidiyon naka ne!'\n\n"
            f"[15-45s - BODY]: 'Ga babban dalilin da ya sa kowa ke magana akan {desc}. Yana da sauƙi da inganci.'\n\n"
            f"[45-60s - CTA]: '{cta_text}'"
        )
    else:
        cta_text  = "Send us a Direct Message (DM) right now to place your order! 📥"
        body_text = (
            f"Looking for the ultimate solution to elevate your lifestyle? Introducing '{desc}'. "
            "Crafted with precision and engineered to deliver top-notch results just for you."
        )
        hashtags = "#BusinessGrowth #PremiumQuality #Innovation"
        fb = f"🚀 [Brightins AI Generated Post]\nTone: {tone} | Goal: {business_goal}\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        ig = f"✨ Quality meets excellence. ✨\n\n{body_text}\n\n{cta_text}\n\n{hashtags}"
        tw = f"{body_text}\n\n{cta_text} {hashtags}"
        tt = (
            f"🎥 [TikTok/Shorts Script - 60 Seconds]\nTone: {tone}\n\n"
            f"[0-15s - HOOK]: 'Stop scrolling if you want to elevate your business today!'\n\n"
            f"[15-45s - BODY]: 'Here is why everyone is talking about {desc}. It is simple, effective, and designed just for you.'\n\n"
            f"[45-60s - CTA]: '{cta_text}'"
        )

    return {"facebook": fb, "instagram": ig, "twitter": tw, "tiktok": tt}


# ── 6. MAIN UI LAYOUT ────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 1. Describe Your Business")
    st.caption("Tell us about your business, products or services")
    business_description = st.text_area(
        "Business Description",
        value="",
        placeholder="e.g., We sell premium organic coffee blends online to customers worldwide...",
        label_visibility="collapsed",
    )

    st.markdown("### 2. Choose Tone")
    st.caption("Select the emotional tone for your marketing copy")
    tone = st.selectbox(
        "Tone",
        ["Professional", "Aggressive Sales", "Friendly", "Humorous", "Luxury"],
        label_visibility="collapsed",
    )

    st.markdown("### 3. Business Goal")
    st.caption("What is the main objective of this content?")
    business_goal = st.selectbox(
        "Goal",
        ["Increase Sales", "Brand Awareness", "Get Leads"],
        label_visibility="collapsed",
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
                st.session_state["brightins_posts"] = posts
                st.session_state["data_ready"]       = True

    if st.session_state.get("data_ready", False):
        posts = st.session_state["brightins_posts"]

        tab1, tab2, tab3, tab4 = st.tabs(
            ["📘 Facebook Post", "📸 Instagram Caption", "🐦 X (Twitter) Post", "🎥 TikTok Script"]
        )

        # HAKAN SHINE MAFI TSAFTA: Kowane akwati yana da kofin kansa na asali na Streamlit (Copy Icon) a sama
        with tab1:
            st.text_area("Facebook Content", posts["facebook"], height=230, label_visibility="collapsed")
            
        with tab2:
            st.text_area("Instagram Content", posts["instagram"], height=230, label_visibility="collapsed")
            
        with tab3:
            st.text_area("X Content", posts["twitter"], height=230, label_visibility="collapsed")
            
        with tab4:
            st.text_area("TikTok Content", posts["tiktok"], height=230, label_visibility="collapsed")