import streamlit as st
import streamlit.components.v1 as components
import time

# ── 1. PAGE CONFIGURATION ─────────────────────────────────────────────────────
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

# ── 3. HIDE STREAMLIT DEFAULT CHROME ─────────────────────────────────────────
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer     {visibility: hidden;}
    header     {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# THEME SYSTEM
# ══════════════════════════════════════════════════════════════════════════════

# ── 4. THEME DEFINITIONS ──────────────────────────────────────────────────────
THEMES = {
    "🌞 Light": {
        "app_bg":             "#f4f2fb",
        "sidebar_bg":         "#ece9f8",
        "block_bg":           "#ffffff",
        "text_primary":       "#1a1535",
        "text_secondary":     "#4a4270",
        "text_muted":         "#7e7a9a",
        "input_bg":           "#ffffff",
        "input_border":       "#c7bfee",
        "input_text":         "#1a1535",
        "tab_active_bg":      "#7f56da",
        "tab_active_text":    "#ffffff",
        "tab_inactive_bg":    "#e8e4f7",
        "tab_inactive_text":  "#4a4270",
        "btn_primary_bg":     "#7f56da",
        "btn_primary_text":   "#ffffff",
        "btn_secondary_bg":   "#ece9f8",
        "btn_secondary_text": "#4a4270",
        "divider":            "#d4cef5",
        "card_shadow":        "0 2px 12px rgba(127,86,218,0.10)",
    },
    "🌙 Dark": {
        "app_bg":             "#0d0b18",
        "sidebar_bg":         "#13101f",
        "block_bg":           "#1a1630",
        "text_primary":       "#ffffff",       # <-- FIX 1: pure white for max readability
        "text_secondary":     "#d4cfee",
        "text_muted":         "#9993b8",
        "input_bg":           "#211d36",
        "input_border":       "#4a4370",
        "input_text":         "#ffffff",       # <-- FIX 1: white text inside inputs
        "tab_active_bg":      "#7f56da",
        "tab_active_text":    "#ffffff",
        "tab_inactive_bg":    "#1e1a33",
        "tab_inactive_text":  "#d4cfee",
        "btn_primary_bg":     "#7f56da",
        "btn_primary_text":   "#ffffff",
        "btn_secondary_bg":   "#2a2545",
        "btn_secondary_text": "#d4cfee",
        "divider":            "#2e294d",
        "card_shadow":        "0 2px 20px rgba(0,0,0,0.50)",
    },
    "💻 System": None,   # handled by CSS media query
}

# URL-safe keys for query_params (avoids emoji encoding issues in URLs)
THEME_TO_KEY = {
    "🌞 Light":  "light",
    "🌙 Dark":   "dark",
    "💻 System": "system",
}
KEY_TO_THEME = {v: k for k, v in THEME_TO_KEY.items()}

QUERY_PARAM = "brightins_theme"


# ── 5. PERSISTENCE: read theme from URL query params (set by JS bridge below) ─
#
#   Flow for a brand-new visit (nothing in URL, something in localStorage):
#     1) Python runs → no query param → defaults to Light (brief flash)
#     2) JS bridge runs in browser → reads localStorage → rewrites URL
#     3) Browser reloads → Python reads query param → correct theme applied
#
#   Flow for a page refresh (query param already in URL):
#     1) Python reads query param directly → correct theme, no flash
#
if "brightins_theme" not in st.session_state:
    raw = st.query_params.get(QUERY_PARAM, "light")
    st.session_state["brightins_theme"] = KEY_TO_THEME.get(raw, "🌞 Light")


# ── 6. CSS BUILDERS ────────────────────────────────────────────────────────────

def build_theme_css(p: dict) -> str:
    """
    Generates a complete <style> block from a palette dict `p`.
    FIX 1: Every Streamlit label selector is explicitly listed so dark-mode
    text is always white and fully legible.
    """
    return f"""
    <style>

    /* ── App shell ─────────────────────────────────────────── */
    .stApp, .block-container {{
        background-color: {p["app_bg"]} !important;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {p["sidebar_bg"]} !important;
    }}

    /* ── Base typography (catches most things) ─────────────── */
    html, body {{
        color: {p["text_primary"]} !important;
    }}

    /* ── Streamlit-specific text targets ───────────────────── */
    /* Generic markdown / paragraph text */
    .stMarkdown, .stMarkdown p, .stMarkdown span,
    .stText, .element-container p {{
        color: {p["text_primary"]} !important;
    }}

    /* ALL widget labels (FIX 1 — the main culprit for dark-mode) */
    label,
    .stSelectbox    label,
    .stTextArea     label,
    .stTextInput    label,
    .stMultiSelect  label,
    .stSlider       label,
    .stRadio        label,
    .stCheckbox     label,
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] span,
    div[class*="Label"],
    div[class*="label"] {{
        color: {p["text_primary"]} !important;
    }}

    /* Caption / helper text */
    .stCaption, .stCaption p, small {{
        color: {p["text_muted"]} !important;
    }}

    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        color: {p["text_primary"]} !important;
    }}

    /* Generic span / div fallback */
    span, li {{
        color: {p["text_primary"]} !important;
    }}

    /* ── Inputs ─────────────────────────────────────────────── */
    textarea, input {{
        background-color: {p["input_bg"]}     !important;
        color:            {p["input_text"]}   !important;
        border-color:     {p["input_border"]} !important;
        border-radius:    8px                 !important;
    }}
    .stTextArea  > div > div,
    .stTextInput > div > div,
    div[data-baseweb="select"] > div {{
        background-color: {p["input_bg"]}     !important;
        border-color:     {p["input_border"]} !important;
        border-radius:    8px                 !important;
    }}

    /* Dropdown menu list */
    div[data-baseweb="popover"] li,
    div[data-baseweb="menu"]    li {{
        background-color: {p["input_bg"]}   !important;
        color:            {p["input_text"]} !important;
    }}
    div[data-baseweb="popover"] li:hover,
    div[data-baseweb="menu"]    li:hover {{
        background-color: {p["tab_inactive_bg"]} !important;
    }}

    /* Selected value text inside selectbox */
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] p {{
        color: {p["input_text"]} !important;
    }}

    /* ── Primary buttons ────────────────────────────────────── */
    .stButton > button {{
        background-color: {p["btn_primary_bg"]}  !important;
        color:            {p["btn_primary_text"]} !important;
        border:           none !important;
        border-radius:    8px  !important;
        font-weight:      600  !important;
        transition:       opacity 0.2s;
    }}
    .stButton > button:hover {{ opacity: 0.86 !important; }}

    /* ── Download buttons ───────────────────────────────────── */
    .stDownloadButton > button {{
        background-color: {p["btn_secondary_bg"]}  !important;
        color:            {p["btn_secondary_text"]} !important;
        border:           1px solid {p["input_border"]} !important;
        border-radius:    8px !important;
        font-weight:      500 !important;
    }}

    /* ── Tabs ───────────────────────────────────────────────── */
    div[data-baseweb="tab-list"] {{
        background-color: {p["tab_inactive_bg"]} !important;
        border-radius:    10px !important;
        padding:          4px  !important;
        gap:              4px  !important;
    }}
    button[data-baseweb="tab"] {{
        background-color: transparent              !important;
        color:            {p["tab_inactive_text"]} !important;
        border-radius:    8px  !important;
        font-weight:      500  !important;
        transition:       background 0.2s, color 0.2s;
    }}
    button[data-baseweb="tab"][aria-selected="true"] {{
        background-color: {p["tab_active_bg"]}  !important;
        color:            {p["tab_active_text"]} !important;
        font-weight:      700 !important;
        box-shadow:       {p["card_shadow"]}     !important;
    }}

    /* ── Alerts ─────────────────────────────────────────────── */
    div[data-testid="stAlert"] {{
        background-color: {p["block_bg"]}    !important;
        color:            {p["text_primary"]} !important;
        border-radius:    10px !important;
    }}
    div[data-testid="stAlert"] p {{
        color: {p["text_primary"]} !important;
    }}

    /* ── Spinner ────────────────────────────────────────────── */
    .stSpinner > div {{
        border-top-color: {p["btn_primary_bg"]} !important;
    }}

    /* ── Divider ────────────────────────────────────────────── */
    hr {{ border-color: {p["divider"]} !important; }}

    /* ── Scrollbar ──────────────────────────────────────────── */
    ::-webkit-scrollbar             {{ width: 6px; }}
    ::-webkit-scrollbar-track       {{ background: {p["app_bg"]}; }}
    ::-webkit-scrollbar-thumb       {{ background: {p["input_border"]}; border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: {p["btn_primary_bg"]}; }}

    </style>
    """


SYSTEM_CSS = """
<style>
@media (prefers-color-scheme: light) {
    .stApp, .block-container { background-color: #f4f2fb !important; }
    html, body, [class*="css"], .stMarkdown, .stMarkdown p,
    p, span, li, label,
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] p { color: #1a1535 !important; }
    h1,h2,h3,h4,h5,h6 { color: #1a1535 !important; }
    textarea, input { background-color: #ffffff !important; color: #1a1535 !important; border-color: #c7bfee !important; border-radius: 8px !important; }
    div[data-baseweb="select"] > div { background-color: #ffffff !important; border-color: #c7bfee !important; }
    div[data-baseweb="select"] span { color: #1a1535 !important; }
    .stButton > button { background-color: #7f56da !important; color: #ffffff !important; border-radius: 8px !important; }
    div[data-baseweb="tab-list"] { background-color: #e8e4f7 !important; border-radius: 10px !important; }
    button[data-baseweb="tab"] { color: #4a4270 !important; }
    button[data-baseweb="tab"][aria-selected="true"] { background-color: #7f56da !important; color: #ffffff !important; }
    hr { border-color: #d4cef5 !important; }
}
@media (prefers-color-scheme: dark) {
    .stApp, .block-container { background-color: #0d0b18 !important; }
    html, body, [class*="css"], .stMarkdown, .stMarkdown p,
    p, span, li, label,
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] p { color: #ffffff !important; }
    h1,h2,h3,h4,h5,h6 { color: #ffffff !important; }
    textarea, input { background-color: #211d36 !important; color: #ffffff !important; border-color: #4a4370 !important; border-radius: 8px !important; }
    div[data-baseweb="select"] > div { background-color: #211d36 !important; border-color: #4a4370 !important; }
    div[data-baseweb="select"] span { color: #ffffff !important; }
    .stButton > button { background-color: #7f56da !important; color: #ffffff !important; border-radius: 8px !important; }
    div[data-baseweb="tab-list"] { background-color: #1e1a33 !important; border-radius: 10px !important; }
    button[data-baseweb="tab"] { color: #d4cfee !important; }
    button[data-baseweb="tab"][aria-selected="true"] { background-color: #7f56da !important; color: #ffffff !important; }
    hr { border-color: #2e294d !important; }
}
</style>
"""


# ── 7. INJECT ACTIVE THEME CSS ────────────────────────────────────────────────
current_theme = st.session_state["brightins_theme"]

if current_theme == "💻 System":
    st.markdown(SYSTEM_CSS, unsafe_allow_html=True)
else:
    st.markdown(build_theme_css(THEMES[current_theme]), unsafe_allow_html=True)


# ── 8. JAVASCRIPT BRIDGE: localStorage ↔ URL query param ─────────────────────
#
#   This small script runs in the browser on every page load.
#
#   On FIRST visit (nothing in URL, but something saved in localStorage):
#     → reads the saved theme, appends it as a query param, reloads once
#     → on the reload, Python reads the query param (step 5) and applies it
#
#   On REFRESH (query param already in URL because Python wrote it):
#     → saves the current URL theme to localStorage (keeps them in sync)
#     → no redirect needed — Python already read it correctly
#
#   On THEME CHANGE (user picks a new theme via the selectbox):
#     → Python updates query_params and reruns; JS then saves to localStorage
#
current_theme_key = THEME_TO_KEY[current_theme]

components.html(f"""
<script>
(function() {{
    var STORAGE_KEY = 'brightins_theme';
    var PARAM_KEY   = '{QUERY_PARAM}';
    var current     = '{current_theme_key}';

    // Always keep localStorage in sync with what Python resolved
    try {{ localStorage.setItem(STORAGE_KEY, current); }} catch(e) {{}}

    // On a genuinely fresh load (no query param in URL), check localStorage
    // and redirect so Python picks it up on the next run.
    var params = new URLSearchParams(window.parent.location.search);
    if (!params.has(PARAM_KEY)) {{
        var saved = null;
        try {{ saved = localStorage.getItem(STORAGE_KEY); }} catch(e) {{}}
        if (saved && saved !== 'light') {{          // 'light' is the default — no redirect needed
            params.set(PARAM_KEY, saved);
            window.parent.location.search = params.toString();
        }}
    }}
}})();
</script>
""", height=0)


# ── 9. TOP BAR: branding left | theme selector right ─────────────────────────
top_left, top_right = st.columns([3, 1])

with top_left:
    st.title("Brightins 🚀")
    st.subheader("Your Global AI Marketing Employee")

with top_right:
    st.markdown("<div style='padding-top:22px;'></div>", unsafe_allow_html=True)
    chosen = st.selectbox(
        label="Theme",
        options=list(THEMES.keys()),
        index=list(THEMES.keys()).index(current_theme),
        key="theme_selector",
        label_visibility="collapsed",
        help="Switch between Light, Dark, or your OS system theme.",
    )
    if chosen != current_theme:
        # Update session state AND URL query param (fixes persistence on refresh)
        st.session_state["brightins_theme"] = chosen
        st.query_params[QUERY_PARAM] = THEME_TO_KEY[chosen]
        # JS bridge (section 8) will then sync the new value into localStorage
        st.rerun()

st.write("---")


# ══════════════════════════════════════════════════════════════════════════════
# APPLICATION LOGIC (100 % unchanged)
# ══════════════════════════════════════════════════════════════════════════════

# ── 10. LOCAL AI SIMULATOR ENGINE ─────────────────────────────────────────────
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


# ── 11. MAIN UI LAYOUT ────────────────────────────────────────────────────────
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

        with tab1:
            st.text_area("Facebook Content", posts["facebook"], height=200, label_visibility="collapsed")
            components.html(f"""
                <textarea id="fb_text" style="display:none;">{posts["facebook"]}</textarea>
                <button onclick="navigator.clipboard.writeText(document.getElementById('fb_text').value); alert('🚀 Facebook Post Copied!')"
                    style="background-color:#7f56da;color:white;border:none;padding:12px 20px;border-radius:6px;
                    cursor:pointer;font-weight:bold;font-size:14px;width:100%;display:flex;
                    align-items:center;justify-content:center;gap:8px;margin-bottom:10px;">
                    📋 Copy Facebook Post
                </button>
            """, height=50)
            st.download_button("📥 Download Facebook Post", data=posts["facebook"],
                               file_name="brightins_facebook.txt", mime="text/plain", use_container_width=True)

        with tab2:
            st.text_area("Instagram Content", posts["instagram"], height=200, label_visibility="collapsed")
            components.html(f"""
                <textarea id="ig_text" style="display:none;">{posts["instagram"]}</textarea>
                <button onclick="navigator.clipboard.writeText(document.getElementById('ig_text').value); alert('📸 Instagram Caption Copied!')"
                    style="background-color:#7f56da;color:white;border:none;padding:12px 20px;border-radius:6px;
                    cursor:pointer;font-weight:bold;font-size:14px;width:100%;display:flex;
                    align-items:center;justify-content:center;gap:8px;margin-bottom:10px;">
                    📋 Copy Instagram Caption
                </button>
            """, height=50)
            st.download_button("📥 Download Instagram Caption", data=posts["instagram"],
                               file_name="brightins_instagram.txt", mime="text/plain", use_container_width=True)

        with tab3:
            st.text_area("X Content", posts["twitter"], height=150, label_visibility="collapsed")
            components.html(f"""
                <textarea id="x_text" style="display:none;">{posts["twitter"]}</textarea>
                <button onclick="navigator.clipboard.writeText(document.getElementById('x_text').value); alert('𝕏 X Post Copied!')"
                    style="background-color:#7f56da;color:white;border:none;padding:12px 20px;border-radius:6px;
                    cursor:pointer;font-weight:bold;font-size:14px;width:100%;display:flex;
                    align-items:center;justify-content:center;gap:8px;margin-bottom:10px;">
                    📋 Copy X Post
                </button>
            """, height=50)
            st.download_button("📥 Download X Post", data=posts["twitter"],
                               file_name="brightins_x_post.txt", mime="text/plain", use_container_width=True)

        with tab4:
            st.text_area("TikTok Content", posts["tiktok"], height=220, label_visibility="collapsed")
            components.html(f"""
                <textarea id="tt_text" style="display:none;">{posts["tiktok"]}</textarea>
                <button onclick="navigator.clipboard.writeText(document.getElementById('tt_text').value); alert('🎥 Video Script Copied!')"
                    style="background-color:#7f56da;color:white;border:none;padding:12px 20px;border-radius:6px;
                    cursor:pointer;font-weight:bold;font-size:14px;width:100%;display:flex;
                    align-items:center;justify-content:center;gap:8px;margin-bottom:10px;">
                    📋 Copy Video Script
                </button>
            """, height=50)
            st.download_button("📥 Download TikTok Script", data=posts["tiktok"],
                               file_name="brightins_tiktok_script.txt", mime="text/plain", use_container_width=True)

    else:
        st.write("Your multi-platform marketing content will appear here after you hit the generate button.")


# ── 12. FOOTER ────────────────────────────────────────────────────────────────
st.markdown(
    "<br><br><hr>"
    "<p style='text-align:center;color:gray;font-size:14px;'>"
    "© 2026 Brightins AI Enterprise. All Rights Reserved.</p>",
    unsafe_allow_html=True,
)