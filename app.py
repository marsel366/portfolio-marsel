import streamlit as st
import streamlit.components.v1 as components
import os

# ==================== CONFIGURATION ====================
st.set_page_config(
    page_title="Marsel | Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== SESSION STATE ====================
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'page' not in st.session_state:
    st.session_state.page = "Home"


# ==================== HIDE SIDEBAR + CHROME ====================
st.markdown("""
<style>
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }

    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }
    [data-testid="stToolbar"] { display: none; }

    .main .block-container {
        padding-top: 0 !important;
        padding-bottom: 3rem !important;
        max-width: 1300px !important;
    }
    .main .block-container > div:first-child { margin-top: 0 !important; }

    /* iframe navbar full width */
    iframe[title="streamlit_components.v1.html"] {
        width: 100% !important;
        display: block !important;
    }

    /* Hidden trigger buttons: tetap ada untuk komunikasi JS → Streamlit,
       tetapi tidak mengambil ruang/layout di halaman */
    div[data-testid="stButton"]:has(button[kind="secondary"]),
    div[data-testid="stButton"]:has(button[kind="primary"]) {
        position: fixed !important;
        top: -10000px !important;
        left: -10000px !important;
        width: 1px !important;
        height: 1px !important;
        min-width: 1px !important;
        min-height: 1px !important;
        margin: 0 !important;
        padding: 0 !important;
        opacity: 0 !important;
        visibility: hidden !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }

    /* Hilangkan ruang dari kolom pembungkus trigger */
    div[data-testid="stHorizontalBlock"]:has(div[data-testid="stButton"]:has(button)) {
        min-height: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        gap: 0 !important;
        overflow: hidden !important;
    }
</style>
""", unsafe_allow_html=True)


# ==================== FONTS ====================
def load_fonts():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)


# ==================== MAIN CSS ====================
def load_css():
    light_css = """
    <style>
    :root {
        --sage: #8DA9C4; --sage-soft: #B4C7DA;
        --cream: #FAF7F2; --sand: #F0EAE0;
        --moss: #A8B5A0; --terra: #C89F82;
        --ink: #3A4A5C; --ink-soft: #6B7B8C; --ink-muted: #95A3B3;
        --bg-main: #FAF7F2; --bg-card: #FFFFFF; --bg-elevated: #FFFDFB;
        --text-main: #3A4A5C; --text-muted: #6B7B8C;
        --border-color: #E8E2D8; --border-soft: #F0EAE0;
        --primary: #8DA9C4; --primary-dark: #6B8BA8;
        --secondary: #A8B5A0; --accent: #C89F82;
        --shadow-sm: 0 1px 3px rgba(58,74,92,0.04);
        --shadow-md: 0 4px 20px -4px rgba(58,74,92,0.08);
        --shadow-lg: 0 20px 40px -12px rgba(58,74,92,0.12);
    }

    html, body, .stApp, .main {
        background-color: var(--bg-main) !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
        color: var(--text-main) !important;
    }
    .main p, .main span, .main div, .main li, .main label {
        color: var(--text-main);
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Sora', sans-serif !important;
        color: var(--ink) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    h1 { font-size: 2.75rem !important; font-weight: 800 !important; }
    h2 { font-size: 1.75rem !important; }
    h3 { font-size: 1.35rem !important; }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 20px !important;
        padding: 32px !important;
        box-shadow: var(--shadow-md) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative; overflow: hidden;
    }
    [data-testid="stVerticalBlockBorderWrapper"]::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, var(--sage), var(--moss), var(--terra));
        opacity: 0; transition: opacity 0.4s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg) !important;
        border-color: var(--sage-soft) !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover::before { opacity: 1; }

    [data-testid="stMetricValue"] {
        font-family: 'Sora', sans-serif !important;
        font-size: 2rem !important; font-weight: 700 !important;
        background: linear-gradient(135deg, var(--primary-dark), var(--secondary));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; letter-spacing: -0.03em;
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important; font-weight: 500 !important;
        font-size: 0.8rem !important; text-transform: uppercase; letter-spacing: 0.08em;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 8px; border-bottom: 1px solid var(--border-color) !important; }
    .stTabs [data-baseweb="tab"] {
        height: 44px; background-color: transparent !important;
        border-radius: 10px 10px 0 0 !important; padding: 8px 20px !important;
        color: var(--text-muted) !important; font-weight: 600 !important; border: none !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--primary-dark) !important; background: rgba(141, 169, 196, 0.06) !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--primary-dark) !important; background: rgba(141, 169, 196, 0.08) !important;
    }
    .stTabs [data-baseweb="tab-highlight"] { background-color: var(--primary-dark) !important; height: 2px !important; }
    .stTabs [data-baseweb="tab-border"] { display: none; }

    .tech-tag {
        background: linear-gradient(135deg, rgba(141,169,196,0.12), rgba(168,181,160,0.10));
        color: var(--primary-dark); padding: 6px 14px; border-radius: 999px;
        font-size: 0.78rem; font-weight: 600; display: inline-block;
        margin: 3px 3px 3px 0; border: 1px solid rgba(141,169,196,0.25);
        transition: all 0.25s ease;
    }
    .tech-tag:hover {
        background: linear-gradient(135deg, var(--sage), var(--sage-soft));
        color: #FFFFFF; transform: translateY(-2px);
    }

    .stButton > button, .stLinkButton > a {
        background: linear-gradient(135deg, var(--sage), var(--sage-soft)) !important;
        color: #FFFFFF !important; border: none !important; border-radius: 12px !important;
        padding: 10px 24px !important; font-weight: 600 !important;
        box-shadow: 0 4px 14px -4px rgba(141, 169, 196, 0.5) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton > button:hover, .stLinkButton > a:hover {
        box-shadow: 0 10px 24px -6px rgba(141, 169, 196, 0.6) !important;
        filter: brightness(1.05);
    }

    hr {
        border: none !important; border-top: 1px solid var(--border-color) !important;
        margin: 2rem 0 !important;
    }
    [data-testid="stAlert"] {
        border-radius: 14px !important; border: 1px solid var(--border-color) !important;
        background: var(--bg-elevated) !important;
    }
    [data-testid="stImage"] img { border-radius: 16px !important; }

    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--sage-soft); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--sage); }
    </style>
    """

    dark_css = """
    <style>
    :root {
        --bg-main: #1C1F26; --bg-card: #252A33; --bg-elevated: #2D323C;
        --text-main: #E8E2D8; --text-muted: #A8A296;
        --border-color: #3A4048; --border-soft: #2F343D;
        --primary: #A8C0D6; --primary-dark: #C4D4E3;
        --secondary: #B8C4B0; --accent: #D4B59A;
        --shadow-md: 0 4px 20px -4px rgba(0,0,0,0.35);
        --shadow-lg: 0 20px 40px -12px rgba(0,0,0,0.45);
    }
    h1, h2, h3, h4, h5, h6 { color: #E8E2D8 !important; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(145deg, #252A33, #1F232B) !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover { border-color: var(--primary) !important; }
    .tech-tag {
        background: rgba(168, 192, 214, 0.12); color: var(--primary);
        border-color: rgba(168, 192, 214, 0.25);
    }
    </style>
    """

    st.markdown(light_css, unsafe_allow_html=True)
    if st.session_state.dark_mode:
        st.markdown(dark_css, unsafe_allow_html=True)


# ==================== NAVBAR ====================
def render_navbar():
    """Navbar via iframe. Komunikasi via postMessage ke parent."""
    pages = [
        ("", "Home"),
        ("", "Data Visualization"),
        ("", "Forecasting"),
    ]

    nav_links_html = ""
    for icon, name in pages:
        active = "active" if st.session_state.page == name else ""
        nav_links_html += (
            f'<a class="nav-link {active}" data-page="{name}" href="javascript:void(0);">'
            f'<span>{icon}</span><span>{name}</span>'
            f'<span class="dot"></span></a>'
        )

    theme_icon = "" if st.session_state.dark_mode else ""
    is_dark = st.session_state.dark_mode

    if is_dark:
        navbar_bg = "rgba(28, 31, 38, 0.85)"
        border_soft = "#2F343D"; border_color = "#3A4048"
        ink = "#E8E2D8"; ink_soft = "#A8A296"; ink_muted = "#7A7568"
        card_bg = "#252A33"; nav_links_bg = "rgba(58, 64, 72, 0.6)"; dot_color = "#A8C0D6"
    else:
        navbar_bg = "rgba(250, 247, 242, 0.85)"
        border_soft = "#F0EAE0"; border_color = "#E8E2D8"
        ink = "#3A4A5C"; ink_soft = "#6B7B8C"; ink_muted = "#95A3B3"
        card_bg = "#FFFFFF"; nav_links_bg = "rgba(232, 226, 216, 0.4)"; dot_color = "#8DA9C4"

    navbar_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background: transparent; overflow: hidden; }}
        .custom-navbar {{
            display: flex; align-items: center; justify-content: space-between;
            gap: 24px; padding: 14px 32px;
            background: {navbar_bg};
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border-bottom: 1px solid {border_soft};
        }}
        .brand {{ display: flex; align-items: center; gap: 12px; cursor: pointer; }}
        .brand-mark {{
            width: 38px; height: 38px; border-radius: 11px;
            background: linear-gradient(135deg, #8DA9C4, #A8B5A0);
            display: flex; align-items: center; justify-content: center;
            color: #FFFFFF; font-family: 'Sora', sans-serif;
            font-weight: 800; font-size: 1.05rem;
            box-shadow: 0 6px 14px -6px rgba(141,169,196,0.6);
            transition: transform 0.3s ease;
        }}
        .brand:hover .brand-mark {{ transform: rotate(-6deg) scale(1.05); }}
        .brand-text {{ display: flex; flex-direction: column; line-height: 1.1; }}
        .brand-name {{
            font-family: 'Sora', sans-serif; font-weight: 700;
            font-size: 1.05rem; color: {ink}; letter-spacing: -0.02em;
        }}
        .brand-tag {{
            font-size: 0.68rem; color: {ink_muted};
            letter-spacing: 0.1em; text-transform: uppercase; font-weight: 600;
        }}

        .nav-links {{
            display: flex; align-items: center; gap: 4px;
            padding: 5px; background: {nav_links_bg};
            border-radius: 999px; border: 1px solid {border_soft};
        }}
        .nav-link {{
            position: relative; padding: 8px 18px; border-radius: 999px;
            font-size: 0.88rem; font-weight: 600; color: {ink_soft};
            text-decoration: none; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex; align-items: center; gap: 6px;
            white-space: nowrap; cursor: pointer;
            user-select: none;
        }}
        .nav-link:hover {{ color: #6B8BA8; }}
        .nav-link.active {{
            background: {card_bg}; color: #6B8BA8;
            box-shadow: 0 2px 8px -2px rgba(58,74,92,0.12);
        }}
        .nav-link .dot {{
            width: 5px; height: 5px; border-radius: 50%;
            background: {dot_color}; opacity: 0; transition: opacity 0.25s ease;
        }}
        .nav-link.active .dot {{ opacity: 1; }}

        .nav-right {{ display: flex; align-items: center; gap: 8px; }}
        .icon-btn {{
            width: 38px; height: 38px; border-radius: 50%;
            background: {card_bg}; border: 1px solid {border_color};
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none; color: {ink_soft}; font-size: 15px;
            padding: 0; font-family: inherit;
        }}
        .icon-btn:hover {{
            background: linear-gradient(135deg, #8DA9C4, #B4C7DA);
            color: #FFFFFF; transform: translateY(-2px);
            border-color: #8DA9C4;
            box-shadow: 0 8px 18px -8px rgba(141,169,196,0.7);
        }}
        .divider-v {{ width: 1px; height: 22px; background: {border_color}; margin: 0 4px; }}
    </style>
    </head>
    <body>
        <div class="custom-navbar">
            <div class="brand" onclick="sendNav('Home')">
                <div class="brand-mark">M</div>
                <div class="brand-text">
                    <span class="brand-name">Marsel's Space</span>
                    <span class="brand-tag">Data & Analytics</span>
                </div>
            </div>
            <div class="nav-links">
                {nav_links_html}
            </div>
            <div class="nav-right">
                <a class="icon-btn" href="mailto:marselinus95@gmail.com" title="Email">✉️</a>
                <a class="icon-btn" href="https://www.linkedin.com/in/marselinus-hindarto-485b121bb/" target="_blank" title="LinkedIn">👔</a>
                <a class="icon-btn" href="https://github.com/marsel366" target="_blank" title="GitHub">🐙</a>
                <a class="icon-btn" href="https://public.tableau.com/app/profile/marselinus.hindarto/vizzes" target="_blank" title="Tableau">📊</a>
                <div class="divider-v"></div>
                <button class="icon-btn" onclick="sendTheme()" title="Toggle theme">{theme_icon}</button>
            </div>
        </div>

        <script>
            function sendNav(pageName) {{
                try {{
                    window.parent.postMessage({{ type: 'nav', page: pageName }}, '*');
                }} catch(e) {{ console.error('nav error', e); }}
            }}
            function sendTheme() {{
                try {{
                    window.parent.postMessage({{ type: 'theme' }}, '*');
                }} catch(e) {{ console.error('theme error', e); }}
            }}
            document.querySelectorAll('.nav-link').forEach(el => {{
                el.addEventListener('click', function(e) {{
                    e.preventDefault();
                    e.stopPropagation();
                    sendNav(this.dataset.page);
                }});
            }});
        </script>
    </body>
    </html>
    """
    components.html(navbar_html, height=78, scrolling=False)


# ==================== HIDDEN TRIGGER BUTTONS ====================
def render_hidden_triggers():
    """
    Invisible Streamlit triggers used by the navbar iframe.
    They remain in the DOM so the parent JS can click them,
    but CSS removes them from the visible page layout.
    """
    if st.button("home", key="_btn_nav_home"):
        st.session_state.page = "Home"
        st.rerun()

    if st.button("dataviz", key="_btn_nav_dataviz"):
        st.session_state.page = "Data Visualization"
        st.rerun()

    if st.button("forecast", key="_btn_nav_forecast"):
        st.session_state.page = "Forecasting"
        st.rerun()

    if st.button("theme", key="_btn_nav_theme"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()


# ==================== PARENT LISTENER (JS) ====================
def install_message_listener():
    """
    JS di parent: terima postMessage dari iframe navbar,
    lalu klik hidden button Streamlit untuk trigger rerun.
    """
    components.html("""
    <script>
    (function() {
        const parentWindow = window.parent;
        const parentDoc = parentWindow.document;

        if (parentWindow.__navbarListenerV3) return;
        parentWindow.__navbarListenerV3 = true;

        // ====== KLIK HIDDEN BUTTON BY KEY ======
        function clickButtonByKey(key) {
            const buttons = parentDoc.querySelectorAll(
                'button[kind="secondary"], button[kind="primary"], div[data-testid="stButton"] button'
            );
            for (const btn of buttons) {
                const parentBlock = btn.closest('[data-testid="stButton"]');
                if (parentBlock && parentBlock.querySelector('.st-key-' + key)) {
                    btn.click();
                    return true;
                }
            }
            const wrapper = parentDoc.querySelector('.st-key-' + key);
            if (wrapper) {
                const b = wrapper.querySelector('button');
                if (b) { b.click(); return true; }
            }
            return false;
        }

        // ====== HANDLE MESSAGE DARI IFRAME ======
        parentWindow.addEventListener('message', function(event) {
            const data = event.data;
            if (!data || typeof data !== 'object') return;

            if (data.type === 'nav') {
                const map = {
                    'Home': '_btn_nav_home',
                    'Data Visualization': '_btn_nav_dataviz',
                    'Forecasting': '_btn_nav_forecast',
                };
                const key = map[data.page];
                if (key) clickButtonByKey(key);
            }
            else if (data.type === 'theme') {
                clickButtonByKey('_btn_nav_theme');
            }
        });

        // ====== CURSOR GLOW ======
        if (!parentDoc.getElementById('cursor-glow')) {
            const glow = parentDoc.createElement('div');
            glow.id = 'cursor-glow';
            Object.assign(glow.style, {
                position: 'fixed', width: '320px', height: '320px',
                borderRadius: '50%', pointerEvents: 'none',
                background: 'radial-gradient(circle, rgba(141,169,196,0.16) 0%, transparent 70%)',
                transform: 'translate(-50%, -50%)',
                zIndex: '9998', mixBlendMode: 'screen',
                transition: 'opacity 0.3s ease',
            });
            parentDoc.body.appendChild(glow);
            parentDoc.addEventListener('mousemove', function(e) {
                glow.style.left = e.clientX + 'px';
                glow.style.top = e.clientY + 'px';
            });
        }

        // ====== SCROLL REVEAL ======
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.1 });

        function revealElements() {
            parentDoc.querySelectorAll('[data-testid="stVerticalBlockBorderWrapper"]').forEach(function(el, i) {
                if (!el.dataset.revealed) {
                    el.dataset.revealed = 'true';
                    el.style.opacity = '0';
                    el.style.transform = 'translateY(30px)';
                    el.style.transition = 'opacity 0.7s ease ' + (i * 0.08) + 's, transform 0.7s ease ' + (i * 0.08) + 's';
                    observer.observe(el);
                }
            });
        }
        setTimeout(revealElements, 300);
        setInterval(revealElements, 1500);
    })();
    </script>
    """, height=0)


# ==================== PAGES ====================
def render_home_page():
    with st.container(border=True):
        col1, col2 = st.columns([1, 2.5], gap="large")
        with col1:
            if os.path.exists("assets/photo.jpg"):
                st.image("assets/photo.jpg", use_container_width=True)
            else:
                st.image(
                    "https://api.dicebear.com/7.x/avataaars/svg?seed=Marsel&backgroundColor=8DA9C4",
                    use_container_width=True
                )
        with col2:
            st.markdown(
                "<p style='color:#8DA9C4; font-weight:600; letter-spacing:0.1em; "
                "text-transform:uppercase; font-size:0.8rem; margin-bottom:8px;'>"
                "Data Analyst · Business Intelligence</p>",
                unsafe_allow_html=True
            )
            st.title("Marselinus Hindarto")
            st.markdown(
                "<p style='color:#6B7B8C; font-size:1rem; margin-top:-8px;'>"
                " Jakarta, Indonesia</p>",
                unsafe_allow_html=True
            )
            st.markdown("""
            I transform raw data into **actionable strategic insights**. Passionate about
            uncovering hidden patterns and building intuitive dashboards that drive
            data-informed business decisions.
            """)
            st.write("")
            mc = st.columns(3)
            with mc[0]: st.metric("Projects", "3+", "Data Viz & ML")
            with mc[1]: st.metric("Tools", "8+", "SQL · Python · BI")
            with mc[2]: st.metric("Experience", "Entry", "Eager to Impact")

    st.write("")
    st.markdown("### Core Competencies")
    with st.container(border=True):
        cols = st.columns(4)
        categories = {
            "Visualization": ["Tableau", "Power BI", "Metabase", "Matplotlib"],
            "Programming": ["Python", "Pandas", "NumPy", "SQL"],
            "Predictive ML": ["Scikit-learn", "ARIMA", "Prophet", "Statsmodels"],
            "Tools & DB": ["Git", "Excel", "SQL Server", "PostgreSQL"]
        }
        for idx, (cat, skills) in enumerate(categories.items()):
            with cols[idx]:
                st.markdown(
                    f"<p style='font-weight:700; color:#3A4A5C; margin-bottom:10px; "
                    f"font-family:Sora,sans-serif; font-size:0.95rem;'>{cat}</p>",
                    unsafe_allow_html=True
                )
                tags_html = "".join([f'<span class="tech-tag">{s}</span>' for s in skills])
                st.markdown(tags_html, unsafe_allow_html=True)


def render_data_viz_page():
    st.title("Data Visualization Portfolio")
    st.markdown(
        "<p style='color:#6B7B8C; font-size:1.05rem;'>"
        "Interactive dashboards showcasing business intelligence and data storytelling.</p>",
        unsafe_allow_html=True
    )
    st.write("")

    with st.container(border=True):
        st.subheader("MyEraspace Loyalty Points Analytics")
        tags = ["Tableau", "Retail", "Customer Retention", "KPI Tracking"]
        st.markdown("".join([f'<span class="tech-tag">{t}</span>' for t in tags]),
                    unsafe_allow_html=True)
        st.write("")
        tab1, tab2, tab3 = st.tabs(["Overview", "Interactive Dashboard", "Business Insights"])
        with tab1:
            st.markdown("""
            **Objective:** Build a comprehensive monitoring system to track loyalty point
            issuance, redemptions, and expiration risks.
            - **Optimize** issuance and redemption campaigns
            - **Minimize** point expiration friction for customers
            - **Maximize** program ROI
            """)
        with tab2:
            st.info("**Pro Tip:** Switch to desktop layout inside Tableau for the best experience.")
            components.html("""
            <iframe src="https://public.tableau.com/views/Book1_17338886826920/Dashboard1?:showVizHome=no&:tabs=no"
            width="100%" height="850" style="border:none; border-radius: 12px;"></iframe>
            """, height=850)
        with tab3:
            c1, c2 = st.columns(2)
            with c1:
                st.error("**Key Finding 1: Expiration Risk**")
                st.write("**Issue:** Massive expiration spikes in Week 15 (30% above average).")
                st.metric("Affected Points", "1.2M", "-30% Risk Potential")
            with c2:
                st.success("**Key Finding 2: Redemption Gap**")
                st.write("**Opportunity:** Current redemption is only 42%. Targeted campaigns can unlock revenue.")
                st.metric("Target Revenue Lift", "Rp 500M", "+8% Conversion")

    st.write("")

    with st.container(border=True):
        st.subheader("Indonesia Black Pepper Export Analysis")
        tags = ["Tableau", "Time Series", "Agriculture Trade", "Geo-Analytics"]
        st.markdown("".join([f'<span class="tech-tag">{t}</span>' for t in tags]),
                    unsafe_allow_html=True)
        st.write("")
        tab1, tab2, tab3 = st.tabs(["Overview", "Interactive Dashboard", "Business Insights"])
        with tab1:
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Value (2024)", "$128M", "+12% YoY")
            c2.metric("Top Market", "Netherlands", "32% Share")
            c3.metric("Growth Rate", "8.5%", "CAGR")
        with tab2:
            components.html("""
            <iframe src="https://public.tableau.com/views/EksporLada/Dashboard1?:showVizHome=no&:tabs=no&:toolbar=yes"
            width="100%" height="850" style="border:none; border-radius: 12px;"></iframe>
            """, height=850)
        with tab3:
            c1, c2 = st.columns(2)
            with c1:
                st.info("**Market Concentration**")
                st.write("Netherlands holds 32% of total exports. **Action:** Leverage this hub to expand to neighboring EU countries.")
            with c2:
                st.warning("**Seasonal Fluctuations**")
                st.write("Q4 exports surge 35% above annual average. **Action:** Scale logistics proactively in Q3.")

    st.write("")

    with st.container(border=True):
        st.subheader("Heineken Sales Performance Dashboard")
        tags = ["Power BI", "Sales Analytics", "Real-time", "FMCG"]
        st.markdown("".join([f'<span class="tech-tag">{t}</span>' for t in tags]),
                    unsafe_allow_html=True)
        st.write("")
        tab1, tab2, tab3 = st.tabs(["Overview", "Dashboard Screens", "Business Insights"])
        with tab1:
            st.markdown("""
            **Objective:** Develop a comprehensive sales analytics platform for regional
            managers to track performance across nationwide stores.
            - **Track** real-time sales across 150+ stores
            - **Automate** reporting, reducing manual effort by 25%
            - **Identify** high and low-performing regions instantly
            """)
            st.write("")
            c1, c2, c3 = st.columns(3)
            c1.metric("Reporting Time Saved", "25%", "Weekly")
            c2.metric("Sales Increase", "15%", "Post-implementation")
            c3.metric("Store Coverage", "150+", "Nationwide")
        with tab2:
            st.info("**Dashboard Previews:** Interactive elements are securely hosted on Power BI Service.")
            if os.path.exists("assets/Dashboard1.png"):
                st.image("assets/Dashboard1.png",
                         caption="Sales Overview Dashboard - Real-time metrics and KPI tracking",
                         use_container_width=True)
                st.divider()
                if os.path.exists("assets/Dashboard2.png"):
                    st.image("assets/Dashboard2.png",
                             caption="Regional Performance Dashboard - Sales by region and channel",
                             use_container_width=True)
            else:
                st.warning("**Images not found!** Place `Dashboard1.png` and `Dashboard2.png` inside `assets/`.")
        with tab3:
            st.warning("**Key Finding 1: Regional Disparity**")
            st.write("**Insight:** The Java region dominates with **65% of national sales**.")
            st.metric("Java Contribution", "65%", "Action: Develop Eastern Indonesia strategy")
            st.divider()
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("""
                **Product Performance**
                - **Product A:** Generates 35% of total revenue.
                - **Premium Segment:** Showing strong 22% YoY growth.
                """)
            with c2:
                st.markdown("""
                **Store Analytics**
                - **Top 10 Stores:** Contribute to 40% of all sales.
                - **Underperforming:** 15 stores flagged for immediate review.
                """)


def render_forecasting_page():
    st.title("Forecasting & Predictive Analytics")
    st.markdown(
        "<p style='color:#6B7B8C; font-size:1.05rem;'>"
        "Applying statistical models and machine learning to predict future trends.</p>",
        unsafe_allow_html=True
    )
    st.write("")

    with st.container(border=True):
        st.subheader("Motorcycle Population Forecast — DKI Jakarta")
        st.write("Predicting urban mobility trends using Advanced Time Series Analysis (ARIMA) to aid infrastructure and policy planning.")
        st.divider()
        cols = st.columns(3)
        cols[0].metric("Model Architecture", "ARIMA (1,2,1)")
        cols[1].metric("MAPE Score", "20%", "Normal")
        cols[2].metric("Forecast Target (2023)", "17.98M Units", "+Trend")
        st.divider()
        c1, c2 = st.columns([2, 1])
        with c1:
            if os.path.exists("assets/newplot.png"):
                st.image("assets/newplot.png", use_container_width=True, caption="5-Year Projection")
            else:
                st.info("Forecast visualization plot will be rendered here.")
        with c2:
            st.markdown("### Policy Impact")
            st.markdown("""
            - **Infrastructure:** Urgent need for road capacity expansion.
            - **Environment:** Emission control & EV incentives required.
            - **Business:** Boom in aftermarket services & financing.
            """)
            st.write("")
            st.link_button("View GitHub Repo →",
                           "https://github.com/marsel366/sepedamotor-forecast/",
                           use_container_width=True)


# ==================== MAIN ====================
def main():
    load_fonts()
    load_css()

    # 1. Navbar (iframe)
    render_navbar()

    # 2. Hidden trigger buttons (dipakai JS untuk rerun)
    render_hidden_triggers()

    # 3. Parent listener JS
    install_message_listener()

    # 4. Render halaman aktif
    if st.session_state.page == "Home":
        render_home_page()
    elif st.session_state.page == "Data Visualization":
        render_data_viz_page()
    elif st.session_state.page == "Forecasting":
        render_forecasting_page()

    st.markdown("""
    <div style="text-align: center; margin-top: 60px; padding-top: 24px;
                border-top: 1px solid var(--border-color);">
        <p style="color: #95A3B3; font-size: 0.75rem; letter-spacing: 0.05em;">
            Crafted with using Streamlit · © 2026 Marselinus Hindarto
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()