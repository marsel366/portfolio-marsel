import streamlit as st
import streamlit.components.v1 as components
import os

# ==================== CONFIGURATION ====================
st.set_page_config(
    page_title="Marsel | Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== SESSION STATE ====================
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True  # Default to Dark Mode for modern feel

# ==================== MODERN CSS STYLING ====================
def load_css():
    """Load custom CSS styles with Modern Indigo & Teal Theme"""
    
    # Base CSS variables (Light Theme)
    base_css = """
    <style>
    :root {
        --primary: #4F46E5;       /* Indigo 600 */
        --primary-light: #818CF8;
        --secondary: #0D9488;     /* Teal 600 */
        --accent: #F43F5E;        /* Rose 500 */
        --bg-main: #F8FAFC;       /* Slate 50 */
        --bg-card: #FFFFFF;
        --text-main: #0F172A;     /* Slate 900 */
        --text-muted: #475569;    /* Slate 600 */
        --border-color: #E2E8F0;  /* Slate 200 */
        --sidebar-bg: #0F172A;    /* Dark Sidebar for contrast */
        --sidebar-text: #F8FAFC;
    }

    /* ===== GLOBAL STYLES ===== */
    .main {
        background-color: var(--bg-main) !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    .stApp {
        background-color: var(--bg-main);
    }

    /* Override Text Colors */
    .main p, .main span, .main div, .main li {
        color: var(--text-main);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--primary) !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }

    /* ===== CARD WIDGETS (Containers) ===== */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 24px !important;
        padding: 30px !important;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px -15px rgba(79, 70, 229, 0.15) !important;
        border-color: var(--primary-light) !important;
    }

    /* ===== METRICS ===== */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 900 !important;
        color: var(--secondary) !important;
        background: -webkit-linear-gradient(45deg, var(--secondary), var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        border-bottom: 2px solid var(--border-color) !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent !important;
        border-radius: 8px 8px 0 0 !important;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        border: none !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: transparent !important;
        color: var(--primary) !important;
        border-bottom: 3px solid var(--primary) !important;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
        border-right: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span {
        color: var(--sidebar-text) !important;
    }

    /* ===== SOCIAL LINKS ===== */
    .social-link {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 12px 20px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        text-decoration: none !important;
        color: #F8FAFC !important;
        font-weight: 600;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .social-link:hover {
        background: var(--primary);
        transform: translateX(5px);
        border-color: var(--primary);
    }

    /* ===== TAGS ===== */
    .tech-tag {
        background: rgba(79, 70, 229, 0.1);
        color: var(--primary);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        display: inline-block;
        margin: 4px;
        border: 1px solid rgba(79, 70, 229, 0.2);
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4) !important;
    }
    
    /* ===== DIVIDERS ===== */
    hr {
        border-top: 1px dashed var(--border-color) !important;
        margin: 2.5rem 0 !important;
    }
    </style>
    """
    
    dark_css = """
    <style>
    :root {
        --bg-main: #0B1120;       /* Midnight Blue */
        --bg-card: #1E293B;       /* Slate 800 */
        --text-main: #F8FAFC;     /* Slate 50 */
        --text-muted: #94A3B8;    /* Slate 400 */
        --border-color: #334155;  /* Slate 700 */
        --primary: #818CF8;
        --secondary: #2DD4BF;
    }
    
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(145deg, #1E293B, #0F172A) !important;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5) !important;
    }
    
    .tech-tag {
        background: rgba(129, 140, 248, 0.15);
        color: #818CF8;
        border-color: rgba(129, 140, 248, 0.3);
    }
    </style>
    """

    st.markdown(base_css, unsafe_allow_html=True)
    if st.session_state.dark_mode:
        st.markdown(dark_css, unsafe_allow_html=True)

# ==================== UI COMPONENTS ====================
def render_social_links():
    st.sidebar.markdown("### 🔗 Connect With Me")
    social_links = [
        ("", "Email", "mailto:marselinus95@gmail.com"),
        ("", "LinkedIn", "https://www.linkedin.com/in/marselinus-hindarto-485b121bb/"),
        ("", "GitHub", "https://github.com/marsel366"),
        ("", "Tableau Public", "https://public.tableau.com/app/profile/marselinus.hindarto/vizzes")
    ]
    for icon, name, url in social_links:
        st.sidebar.markdown(
            f'<a href="{url}" target="_blank" class="social-link">'
            f'<span style="font-size:18px">{icon}</span><span>{name}</span></a>',
            unsafe_allow_html=True
        )

# ==================== PAGES ====================
def render_home_page():
    # Hero Section
    with st.container(border=True):
        col1, col2 = st.columns([1, 2.5], gap="large")
        
        with col1:
            # Menggunakan placeholder jika gambar tidak ada
            if os.path.exists("assets/photo.jpg"):
                st.image("assets/photo.jpg", use_container_width=True)
            else:
                st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Marsel&backgroundColor=4F46E5", use_container_width=True)
                
        with col2:
            st.title("Marselinus Hindarto")
            st.markdown("#### Data Analyst | Business Intelligence")
            st.markdown("Jakarta, Indonesia")
            
            st.markdown("""
            I transform raw data into **actionable strategic insights**. Passionate about uncovering hidden patterns and building intuitive dashboards that drive data-informed business decisions.
            """)
            
            # Quick Stats Row
            st.write("")
            metric_cols = st.columns(3)
            with metric_cols[0]: st.metric("Projects Completed", "3+", "Data Viz & ML")
            with metric_cols[1]: st.metric("Tools Mastered", "8+", "SQL, Python, BI")
            with metric_cols[2]: st.metric("Experience", "Entry-Level", "Eager to Impact")

    # Tech Stack Section
    st.markdown("###  Core Competencies")
    with st.container(border=True):
        cols = st.columns(4)
        categories = {
            "Data Visualization": ["Tableau", "Power BI", "Metabase", "Matplotlib"],
            "Programming & Data": ["Python", "Pandas", "NumPy", "SQL"],
            "Predictive ML": ["Scikit-learn", "ARIMA", "Prophet", "Statsmodels"],
            "Tools & DB": ["Git", "Excel", "SQL Server", "PostgreSQL"]
        }
        
        for idx, (cat, skills) in enumerate(categories.items()):
            with cols[idx]:
                st.markdown(f"**{cat}**")
                tags_html = "".join([f'<span class="tech-tag">{skill}</span>' for skill in skills])
                st.markdown(tags_html, unsafe_allow_html=True)

def render_data_viz_page():
    st.title("Data Visualization Portfolio")
    st.markdown("Interactive dashboards showcasing business intelligence and data storytelling.")
    st.write("")

    # === PROJECT 1: LOYALTY POINTS ===
    with st.container(border=True):
        st.subheader("MyEraspace Loyalty Points Analytics")
        tags = ["Tableau", "Retail", "Customer Retention", "KPI Tracking"]
        st.markdown("".join([f'<span class="tech-tag">{tag}</span>' for tag in tags]), unsafe_allow_html=True)
        st.write("")

        tab1, tab2, tab3 = st.tabs(["Overview", "Interactive Dashboard", "Business Insights"])
        
        with tab1:
            st.markdown("""
            **Objective:** Build a comprehensive monitoring system to track loyalty point issuance, redemptions, and expiration risks.
            - **Optimize** issuance and redemption campaigns
            - **Minimize** point expiration friction for customers
            - **Maximize** program ROI
            """)
            
        with tab2:
            st.info("**Pro Tip:** Switch to desktop layout inside Tableau for the best experience.")
            components.html("""
            <iframe src="https://public.tableau.com/views/Book1_17338886826920/Dashboard1?:showVizHome=no&:tabs=no" width="100%" height="850" style="border:none; border-radius: 12px;"></iframe>
            """, height=850)
            
        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                st.error("**Key Finding 1: Expiration Risk**")
                st.write("**Issue:** Massive expiration spikes in Week 15 (30% above average).")
                st.metric("Affected Points", "1.2M", "-30% Risk Potential")
            with col2:
                st.success("**Key Finding 2: Redemption Gap**")
                st.write("**Opportunity:** Current redemption is only 42%. Targeted campaigns can unlock revenue.")
                st.metric("Target Revenue Lift", "Rp 500M", "+8% Conversion")

    st.write("")

    # === PROJECT 2: BLACK PEPPER EXPORT ===
    with st.container(border=True):
        st.subheader("Indonesia Black Pepper Export Analysis")
        tags = ["Tableau", "Time Series", "Agriculture Trade", "Geo-Analytics"]
        st.markdown("".join([f'<span class="tech-tag">{tag}</span>' for tag in tags]), unsafe_allow_html=True)
        st.write("")

        tab1, tab2, tab3 = st.tabs(["Overview", "Interactive Dashboard", "Business Insights"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Value (2024)", "$128M", "+12% YoY")
            col2.metric("Top Market", "Netherlands", "32% Share")
            col3.metric("Growth Rate", "8.5%", "CAGR")
            
        with tab2:
            components.html("""
            <iframe src="https://public.tableau.com/views/EksporLada/Dashboard1?:showVizHome=no&:tabs=no&:toolbar=yes" width="100%" height="850" style="border:none; border-radius: 12px;"></iframe>
            """, height=850)
            
        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                st.info("**Market Concentration**")
                st.write("Netherlands holds 32% of total exports. **Action:** Leverage this hub to expand to neighboring EU countries like Germany and France.")
            with col2:
                st.warning("**Seasonal Fluctuations**")
                st.write("Q4 exports surge 35% above the annual average due to harvest cycles. **Action:** Scale logistics proactively in Q3.")

    st.write("")

    # === PROJECT 3: HEINEKEN SALES DASHBOARD ===
    with st.container(border=True):
        st.subheader("Heineken Sales Performance Dashboard")
        tags = ["Power BI", "Sales Analytics", "Real-time", "FMCG"]
        st.markdown("".join([f'<span class="tech-tag">{tag}</span>' for tag in tags]), unsafe_allow_html=True)
        st.write("")

        tab1, tab2, tab3 = st.tabs(["Overview", "Dashboard Screens", "Business Insights"])
        
        with tab1:
            st.markdown("""
            **Objective:** Develop a comprehensive sales analytics platform for regional managers to track performance across nationwide stores.
            - **Track** real-time sales across 150+ stores
            - **Automate** reporting, reducing manual effort by 25%
            - **Identify** high and low-performing regions instantly
            """)
            st.write("")
            col1, col2, col3 = st.columns(3)
            col1.metric("Reporting Time Saved", "25%", "Weekly")
            col2.metric("Sales Increase", "15%", "Post-implementation")
            col3.metric("Store Coverage", "150+", "Nationwide")
            
        with tab2:
            st.info("**Dashboard Previews:** Interactive elements are securely hosted on Power BI Service.")
            
            # Pengecekan apakah gambar ada di folder assets
            if os.path.exists("assets/Dashboard1.png"):
                st.image("assets/Dashboard1.png", caption="Sales Overview Dashboard - Real-time metrics and KPI tracking", use_container_width=True)
                st.divider()
                if os.path.exists("assets/Dashboard2.png"):
                    st.image("assets/Dashboard2.png", caption="Regional Performance Dashboard - Sales by region and channel", use_container_width=True)
            else:
                # Placeholder keren jika gambar belum diupload
                st.warning("**Images not found!** Please ensure `Dashboard1.png` and `Dashboard2.png` are placed inside the `assets/` folder.")
                
        with tab3:
            st.warning("**Key Finding 1: Regional Disparity**")
            st.write("**Insight:** The Java region dominates with **65% of national sales**, indicating heavy market concentration.")
            st.metric("Java Contribution", "65%", "Action: Develop Eastern Indonesia strategy")
            
            st.divider()
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **Product Performance**
                - **Product A:** Generates 35% of total revenue.
                - **Premium Segment:** Showing strong 22% YoY growth.
                """)
            with col2:
                st.markdown("""
                **Store Analytics**
                - **Top 10 Stores:** Contribute to 40% of all sales.
                - **Underperforming:** 15 stores flagged for immediate review.
                """)
def render_forecasting_page():
    st.title("Forecasting & Predictive Analytics")
    st.markdown("Applying statistical models and machine learning to predict future trends.")
    
    with st.container(border=True):
        st.subheader("Motorcycle Population Forecast - DKI Jakarta")
        st.write("Predicting urban mobility trends using Advanced Time Series Analysis (ARIMA) to aid infrastructure and policy planning.")
        
        st.divider()
        
        cols = st.columns(3)
        cols[0].metric("Model Architecture", "ARIMA (1,2,1)")
        cols[1].metric("MAPE Score", "20%", "Normal")
        cols[2].metric("Forecast Target (2023)", "17.98M Units", "+Trend")
        
        st.divider()
        
        # Simulasi gambar grafik
        col1, col2 = st.columns([2, 1])
        with col1:
            if os.path.exists("assets/newplot.png"):
                st.image("assets/newplot.png", use_container_width=True, caption="5-Year Projection")
            else:
                st.info("Forecast visualization plot will be rendered here.")
        
        with col2:
            st.markdown("### Policy Impact")
            st.markdown("""
            -  **Infrastructure:** Urgent need for road capacity expansion.
            -  **Environment:** Emission control & EV incentives required.
            -  **Business:** Boom in aftermarket services & financing.
            """)
            
            st.write("")
            st.link_button(" View GitHub Repo", "https://github.com/marsel366/sepedamotor-forecast/", use_container_width=True)

# ==================== MAIN APP ENGINE ====================
def main():
    load_css()
    
    with st.sidebar:
        # Custom Header Sidebar
        st.markdown("""
        <div style="text-align: center; padding-bottom: 20px;">
            <div style="background: linear-gradient(135deg, #4F46E5, #0D9488); height: 4px; width: 50px; margin: 0 auto 15px auto; border-radius: 2px;"></div>
            <h2 style="margin: 0; font-size: 24px;">Marsel's Space</h2>
            <p style="color: var(--text-muted); font-size: 14px; margin-top: 5px;">Data & Analytics</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Options
        page = st.radio(
            "Navigation",
            ["Home", "Data Visualization", "Forecasting"],
            label_visibility="collapsed"
        )
        
        st.divider()
        
        # Toggle Dark Mode
        st.session_state.dark_mode = st.toggle(
            "🌙 Dark Mode",
            value=st.session_state.dark_mode
        )
        
        st.divider()
        render_social_links()
        
        # Footer
        st.markdown("""
        <div style="text-align: center; margin-top: 40px;">
            <p style="color: #64748B; font-size: 12px;">Crafted using Streamlit<br/>© 2026 Marselinus Hindarto</p>
        </div>
        """, unsafe_allow_html=True)

    # Router
    if page == "Home":
        render_home_page()
    elif page == "Data Visualization":
        render_data_viz_page()
    elif page == "Forecasting":
        render_forecasting_page()

if __name__ == "__main__":
    main()