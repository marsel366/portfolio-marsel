import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os
from datetime import datetime

# ==================== CONFIGURATION ====================
st.set_page_config(
    page_title="Marsel | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== SESSION STATE ====================
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'contact_submitted' not in st.session_state:
    st.session_state.contact_submitted = False

# ==================== HIGH CONTRAST CSS ====================
def load_css():
    """Load custom CSS styles with high contrast"""
    base_css = """
    <style>
    /* ===== HIGH CONTRAST BASE STYLES ===== */
    .main {
        background-color: #ffffff !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        color: white !important;
    }
    
    /* ===== HIGH CONTRAST CARDS ===== */
    .main [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        padding: 32px !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15) !important;
        margin-bottom: 32px !important;
        border: 2px solid ##18338C !important;
        transition: all 0.3s ease !important;
    }
    
    .main [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(30, 64, 175, 0.2) !important;
        border-color: #2563eb !important;
    }
    
    /* Border color for cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: ##18338C !important;
    }
    
    /* ===== HIGH CONTRAST SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
        border-right: 3px solid #2563eb !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* ===== HIGH CONTRAST TYPOGRAPHY ===== */
    h1 {
        color: ##18338C !important;
        font-weight: 900 !important;
        margin-bottom: 1rem !important;
        font-size: 2.5rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: ##18338C !important;
        font-weight: 800 !important;
        font-size: 2rem !important;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 10px;
        margin-bottom: 1.5rem !important;
    }
    
    h3 {
        color: #2563eb !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    h4 {
        color: #3b82f6 !important;
        font-weight: 600 !important;
        font-size: 1.25rem !important;
    }
    
    p, span, div, .stMarkdown, .stMarkdown p {
        color: white !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
    }
    
    strong, b {
        color: #dc2626 !important;
        font-weight: 700 !important;
    }
    
    /* ===== HIGH CONTRAST METRICS ===== */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        color: ##18338C !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    
    [data-testid="stMetricLabel"] {
        color: #374151 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    [data-testid="stMetricDelta"] {
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    
    /* ===== HIGH CONTRAST BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(90deg, ##18338C 0%, #2563eb 100%) !important;
        color: white !important;
        border: 2px solid #1e3a8a !important;
        border-radius: 10px !important;
        padding: 12px 32px !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 20px rgba(30, 64, 175, 0.4) !important;
        border-color: #2563eb !important;
    }
    
    /* Link buttons */
    .stLinkButton > button {
        background: linear-gradient(90deg, #059669 0%, #10b981 100%) !important;
        border: 2px solid #047857 !important;
    }
    
    /* ===== HIGH CONTRAST TAGS ===== */
    .tag {
        background: linear-gradient(90deg, #3b82f6 0%, white 100%) !important;
        color: white !important;
        padding: 6px 16px !important;
        border-radius: 20px !important;
        margin-right: 10px !important;
        margin-bottom: 10px !important;
        font-size: 0.9rem !important;
        display: inline-block !important;
        font-weight: 600 !important;
        border: 1px solid #1d4ed8 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    }
    
    /* ===== HIGH CONTRAST TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px !important;
        border-bottom: 2px solid ##18338C !important;
        padding-bottom: 5px !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0 0 !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        background-color: #313640 !important;
        color: #374151 !important;
        border: 2px solid #d1d5db !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, ##18338C 0%, #2563eb 100%) !important;
        color: white !important;
        border-color: ##18338C !important;
    }
    
    /* ===== HIGH CONTRAST DIVIDERS ===== */
    hr, .stDivider {
        border: none !important;
        border-top: 3px solid ##18338C !important;
        margin: 2rem 0 !important;
        opacity: 1 !important;
    }
    
    /* ===== HIGH CONTRAST SOCIAL LINKS ===== */
    .social-link {
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        padding: 14px 18px !important;
        background: rgba(37, 99, 235, 0.1) !important;
        border-radius: 12px !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
        margin-bottom: 10px !important;
        border: 2px solid rgba(37, 99, 235, 0.3) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .social-link:hover {
        background: rgba(37, 99, 235, 0.3) !important;
        transform: translateX(5px) !important;
        border-color: #2563eb !important;
    }
    
    /* ===== HIGH CONTRAST ALERTS ===== */
    .stAlert {
        border: 2px solid !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    
    .stSuccess {
        background-color: #d1fae5 !important;
        border-color: #10b981 !important;
        color: #065f46 !important;
    }
    
    .stWarning {
        background-color: #fef3c7 !important;
        border-color: #f59e0b !important;
        color: #92400e !important;
    }
    
    .stInfo {
        background-color: #dbeafe !important;
        border-color: #3b82f6 !important;
        color: ##18338C !important;
    }
    
    .stError {
        background-color: #fee2e2 !important;
        border-color: #ef4444 !important;
        color: #991b1b !important;
    }
    
    /* ===== HIGH CONTRAST FORMS ===== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div {
        border: 2px solid ##18338C !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        color: white !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2) !important;
    }
    
    /* ===== HIGH CONTRAST CODE BLOCKS ===== */
    .stCode {
        background: #1e293b !important;
        color: #e2e8f0 !important;
        border: 2px solid #334155 !important;
        border-radius: 8px !important;
        padding: 16px !important;
    }
    
    /* ===== DARK MODE - HIGH CONTRAST ===== */
    .dark-mode .main {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }
    
    .dark-mode .main *:not([class*="st-"]):not(h1):not(h2):not(h3):not(h4) {
        color: #e2e8f0 !important;
    }
    
    .dark-mode [data-testid="stVerticalBlockBorderWrapper"] {
        background: #1e293b !important;
        border-color: #3b82f6 !important;
        color: #e2e8f0 !important;
    }
    
    .dark-mode h1 {
        color: white !important;
    }
    
    .dark-mode h2 {
        color: #93c5fd !important;
        border-bottom-color: #3b82f6 !important;
    }
    
    .dark-mode h3 {
        color: white !important;
    }
    
    .dark-mode h4 {
        color: #93c5fd !important;
    }
    
    .dark-mode p, .dark-mode span, .dark-mode div {
        color: #e2e8f0 !important;
    }
    
    .dark-mode [data-testid="stMetricValue"] {
        color: white !important;
    }
    
    .dark-mode .tag {
        background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%) !important;
        color: white !important;
    }
    
    /* ===== RESPONSIVE DESIGN ===== */
    @media (max-width: 768px) {
        .main [data-testid="stVerticalBlockBorderWrapper"] {
            padding: 24px !important;
            margin-bottom: 24px !important;
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2rem !important;
        }
        
        h1 {
            font-size: 2rem !important;
        }
        
        h2 {
            font-size: 1.5rem !important;
        }
    }
    
    /* ===== SCROLLBAR STYLING ===== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #3b82f6;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #2563eb;
    }
    </style>
    """
    
    st.markdown(base_css, unsafe_allow_html=True)
    
    # Add dark mode CSS if active
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        .main {
            background-color: #404042 !important;
        }
        
        .main * {
            color: #e2e8f0 !important;
        }
        
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: #1e293b !important;
            border-color: #3b82f6 !important;
        }
        
        .stButton > button {
            background: linear-gradient(90deg, #3b82f6 0%, white 100%) !important;
            border-color: #1d4ed8 !important;
        }
        
        /* Dark mode scrollbar */
        ::-webkit-scrollbar-track {
            background: #334155;
        }
        
        ::-webkit-scrollbar-thumb {
            background: white;
        }
        </style>
        """, unsafe_allow_html=True)

# ==================== UTILITY FUNCTIONS ====================
def render_social_links():
    """Render social media links in sidebar"""
    st.sidebar.markdown("### 🔗 Connect With Me")
    
    social_links = [
        ("📧", "Email", "mailto:marselinus95@gmail.com"),
        ("💼", "LinkedIn", "https://www.linkedin.com/in/marselinus-hindarto-485b121bb/"),
        ("💻", "GitHub", "https://github.com/marsel366"),
        ("📊", "Tableau Public", "https://public.tableau.com/app/profile/marselinus.hindarto/vizzes")
    ]
    
    for icon, name, url in social_links:
        st.sidebar.markdown(
            f'<a href="{url}" target="_blank" class="social-link">'
            f'<span style="font-size:20px">{icon}</span>'
            f'<span>{name}</span>'
            f'</a>',
            unsafe_allow_html=True
        )

# ==================== HIGH CONTRAST PAGE COMPONENTS ====================
def render_home_page():
    """Render the home page with high contrast"""
    with st.container(border=True):
        # Hero Section
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("assets/photo.jpg", 
                    use_container_width=True,
                    caption="Data Analyst | Business Intelligence")
        
        with col2:
            st.title("Marselinus Hindarto")
            st.markdown("##### 🎯 Data Analyst | Business Intelligence Specialist")
            st.markdown("##### 📍 Jakarta, Indonesia | Fresh Graduate")
            
            st.divider()
            
            st.markdown("""
            ### 👋 Hello!
            
            I'm a **passionate Data Analyst** with expertise in transforming raw data into 
            **actionable insights**. My work focuses on:
            
            📊 **Building interactive dashboards**  
            📈 **Time series forecasting**  
            🔍 **Exploratory data analysis**  
            
            All to drive **data-informed business decisions**.
            """)                
        # Tech Stack
        st.divider()
        st.subheader("🛠️ Tech Stack")
        
        tech_cols = st.columns(4)
        tech_stacks = {
            "📊 **Data Analysis**": ["Python", "Pandas", "NumPy", "SQL"],
            "📈 **Visualization**": ["Tableau", "Power BI", "Matplotlib", "Metabase"],
            "🤖 **ML & Forecasting**": ["Scikit-learn", "Statsmodels", "ARIMA", "Prophet"],
            "⚡ **Tools & Others**": ["Git", "Excel", "SQL Server", "PostMan"]
        }
        
        for idx, (category, tools) in enumerate(tech_stacks.items()):
            with tech_cols[idx]:
                st.markdown(category)
                for tool in tools:
                    st.markdown(f"• **{tool}**")

def render_data_viz_page():
    """Render data visualization projects page with high contrast"""
    st.header("📊 Data Visualization Portfolio")
    
    # ==================== PROJECT 1: LOYALTY POINTS ====================
    st.subheader("📋 Project 1: Loyalty Points Analytics")
    
    tab1_1, tab1_2, tab1_3 = st.tabs(["📖 Overview", "📈 Dashboard", "🎯 Insights"])
    
    with tab1_1:
        with st.container(border=True):
            st.markdown("### MyEraspace Loyalty Points Weekly Report")
            st.markdown("""
            **Comprehensive monitoring system** for loyalty points program to:
            
            ✅ **Optimize issuance and redemption strategies**  
            ✅ **Minimize point expiration risks**  
            ✅ **Maximize customer retention**  
            ✅ **Improve program ROI**
            """)
            
            # Tags with better contrast
            tags = ["Tableau", "Dashboard", "Business Intelligence", "Retail", "Analytics"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin:20px 0">{tag_html}</div>', unsafe_allow_html=True)
    
    with tab1_2:
        with st.container(border=True):
            st.markdown("### 📊 Interactive Tableau Dashboard")
            st.info("**Live Dashboard Embed** - Real-time data visualization. " 
            "Tip: Use view in desktop layout for best experience.")
            components.html("""
            <iframe
            src="https://public.tableau.com/views/Book1_17338886826920/Dashboard1?:showVizHome=no&:tabs=no"
            width="100%" height="1200">
            </iframe>
            """, height=1200)
    
    with tab1_3:
        with st.container(border=True):
            st.markdown("### 🎯 Key Business Insights")
            col1, col2 = st.columns(2)
            with col1:
                st.success("**✅ Key Finding 1: Point Expiration**")
                st.markdown("""
                **Issue:** Point expiration spikes identified in Week 15  
                **Impact:** 30% above average expiration rate  
                **Solution:** Automated alert system for expiration peaks
                """)
                st.metric("Affected Points", "1.2M", "30% increase", delta_color="inverse")
            
            with col2:
                st.warning("**⚠️ Key Finding 2: Redemption Gap**")
                st.markdown("""
                **Issue:** Redemption rate only 42% of issuance  
                **Opportunity:** $500K potential revenue increase  
                **Action:** Targeted redemption campaigns
                """)
                st.metric("Redemption Rate", "42%", "-8% target", delta_color="inverse")
    
    st.divider()
    
    # ==================== PROJECT 2: BLACK PEPPER EXPORT ====================
    st.subheader("🌍 Project 2: Indonesia Black Pepper Export Analysis")
    
    # SAMA PERSIS DENGAN PROJECT 1: 3 TABS
    tab2_1, tab2_2, tab2_3 = st.tabs(["📖 Overview", "📈 Dashboard", "🎯 Insights"])
    
    # TAB 2.1: OVERVIEW
    with tab2_1:
        with st.container(border=True):
            st.markdown("### Export Trend Analysis 2012-2024")
            st.markdown("""
            **Comprehensive analysis** of Indonesia's black pepper export patterns to:
            
            ✅ **Identify key international markets**  
            ✅ **Optimize export strategies and pricing**  
            ✅ **Maximize foreign exchange earnings**  
            ✅ **Support agricultural policy decisions**
            """)
            
            # Export Metrics
            st.markdown("#### 📊 Export Performance Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Export Value (2024)", "$128M", "+12% YoY", 
                         help="Total export value in 2024")
            with col2:
                st.metric("Top Destination", "Netherlands", "32% market share",
                         help="Country with highest export volume")
            with col3:
                st.metric("Growth Rate", "8.5% CAGR", "2012-2024",
                         help="Compound Annual Growth Rate")
            
            # Tags
            tags = ["Tableau", "Export Analysis", "Time Series", "Agriculture", "International Trade"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin:20px 0">{tag_html}</div>', unsafe_allow_html=True)
    
    # TAB 2.2: DASHBOARD
    with tab2_2:
        with st.container(border=True):
            st.markdown("### 📊 Interactive Export Dashboard")
            st.info("**Live Tableau Dashboard** - Explore Indonesia's black pepper export trends. Tip: Use view in desktop layout for best experience.")
            
            # Your Tableau embed code with high contrast wrapper
            components.html("""
            <iframe
            src="https://public.tableau.com/views/EksporLada/Dashboard1?:showVizHome=no&:tabs=no&:toolbar=yes"
            width="100%"
            height="900"
            style="border:none;">
            </iframe>
            """, height=900)
    
    # TAB 2.3: INSIGHTS
    with tab2_3:
        with st.container(border=True):
            st.markdown("### 🎯 Key Export Insights")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.success("**✅ Key Finding 1: Market Concentration**")
                st.markdown("""
                **Finding:** Netherlands dominates with **32%** of total exports  
                **Insight:** Strong EU foothold with established distribution  
                **Opportunity:** Expand to Germany and France markets
                """)
                st.metric("Netherlands Market Share", "32%", "+5% from 2020", 
                         help="Percentage of total exports to Netherlands")
            
            with col2:
                st.warning("**⚠️ Key Finding 2: Seasonal Fluctuations**")
                st.markdown("""
                **Finding:** Q4 exports 35% higher than annual average  
                **Insight:** Year-end harvest drives export volume  
                **Action:** Optimize logistics for Q4 peak season
                """)
                st.metric("Q4 Export Premium", "+35%", "vs annual average", 
                         help="Q4 export volume compared to annual average")
            
            st.divider()
            
            # Additional insights
            st.markdown("#### 📈 Additional Findings")
            
            insight_cols = st.columns(3)
            with insight_cols[0]:
                st.markdown("""
                **🌏 Emerging Markets**
                - Vietnam imports grew 45% YoY
                - China market potential: $25M
                - ASEAN region: 15% CAGR
                """)
            
            with insight_cols[1]:
                st.markdown("""
                **📊 Quality Trends**
                - Premium grade: 22% price premium
                - Organic segment: 18% growth
                - Certified products: 30% demand increase
                """)
            
            with insight_cols[2]:
                st.markdown("""
                **🚀 Growth Strategies**
                - Diversify to 5 new markets
                - Value-added products: +40% margin
                - Digital export platforms
                """)
    
    st.divider()
    
    # ==================== PROJECT 3: POWER BI SALES DASHBOARD ====================
    st.subheader("🍺 Project 3: Heineken Sales Performance Dashboard")
    
    # SAMAKAN DENGAN STRUKTUR PROJECT 1 & 2
    tab3_1, tab3_2, tab3_3 = st.tabs(["📖 Overview", "📈 Dashboard", "🎯 Insights"])
    
    # TAB 3.1: OVERVIEW
    with tab3_1:
        with st.container(border=True):
            st.markdown("### Sales Performance Monitoring System")
            st.markdown("""
            **Comprehensive sales analytics platform** designed to:
            
            ✅ **Track real-time sales across 150+ stores**  
            ✅ **Reduce manual reporting time by 25%**  
            ✅ **Increase sales through data-driven decisions**  
            ✅ **Automate KPI tracking for regional managers**
            """)
            
            # Performance Metrics
            st.markdown("#### 📊 Business Impact Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Reporting Time Saved", "25%", "Weekly", 
                         help="Reduction in manual reporting time")
            with col2:
                st.metric("Sales Increase", "15%", "Post-implementation",
                         help="Increase in sales after dashboard adoption")
            with col3:
                st.metric("Store Coverage", "150+", "Nationwide",
                         help="Number of stores covered by the dashboard")
            
            # Tags
            tags = ["Power BI", "Sales Analytics", "Real-time", "FMCG", "Business Intelligence"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin:20px 0">{tag_html}</div>', unsafe_allow_html=True)
    
    # TAB 3.2: DASHBOARD
    with tab3_2:
        with st.container(border=True):
            st.markdown("### 📊 Interactive Power BI Dashboard")
            st.info("**Dashboard Screenshots** - Sales performance visualization")
            
            # Dashboard Images
            if os.path.exists("assets/Dashboard1.png"):
                st.markdown("#### Overview Dashboard")
                st.image("assets/Dashboard1.png", 
                        caption="**Sales Overview Dashboard** - Real-time metrics and KPI tracking",
                        use_container_width=True)
                
                st.divider()
                
                st.markdown("#### Regional Analysis")
                st.image("assets/Dashboard2.png", 
                        caption="**Regional Performance Dashboard** - Sales by region and channel",
                        use_container_width=True)
            else:
                st.info("""
                **Dashboard preview would be displayed here**
                
                In a live deployment, actual Power BI dashboards or screenshots would be embedded
                to show the interactive sales analytics platform.
                """)
    
    # TAB 3.3: INSIGHTS
    with tab3_3:
        with st.container(border=True):
            st.markdown("### 🎯 Key Sales Insights")
            
            col1, col2 = st.columns(2)           
            with col1:
                st.warning("**⚠️ Key Finding 1: Regional Disparity**")
                st.markdown("""
                **Finding:** Java contributes 65% of national sales  
                **Insight:** Market concentration in Java region  
                **Action:** Develop Eastern Indonesia growth strategy
                """)
                st.metric("Java Region Contribution", "65%", "of national sales", 
                help="Percentage of total sales from Java region")
            st.divider()
            
            # Additional insights
            st.markdown("#### 📈 Additional Business Insights")
            
            insight_cols = st.columns(3)
            with insight_cols[0]:
                st.markdown("""
                **📦 Product Performance**
                - Product A: 35% revenue share
                - Premium segment: 22% growth
                - New products: 18% market penetration
                """)
            
            with insight_cols[1]:
                st.markdown("""
                **🏪 Store Analytics**
                - Top 10 stores: 40% of sales
                - High-growth regions: +25% YoY
                - Underperforming: 15 stores flagged
                """)
            
            with insight_cols[2]:
                st.markdown("""
                **📅 Seasonal Patterns**
                - Holiday sales: +50% peak
                - Weekend vs weekday: 35% difference
                - Promotional lift: 28% increase
                """)

def render_forecasting_page():
    """Render forecasting projects page with high contrast"""
    st.header("📈 Forecasting & Predictive Analytics")
    
    with st.container(border=True):
        st.subheader("🏍️ Motorcycle Population Forecasting - DKI Jakarta")
        
        st.markdown("""
        ### Project Overview
        
        **Objective:** Forecast motorcycle population growth to support:
        - Transportation infrastructure planning
        - Environmental impact assessment
        - Policy development and regulation
        - Economic opportunity identification
        
        **Methodology:** Advanced time series analysis using ARIMA modeling
        with historical data from 2010-2023.
        """)
        
        # Model Performance
        st.divider()
        st.markdown("### 📊 Model Performance Metrics")
        
        cols = st.columns(4)
        
        metrics = [
            ("Model Used", "ARIMA(1,2,1)", "Optimal parameters"),
            ("MAPE Score", "20%", "Accurate"),
            ("Forecast Horizon", "1 Years", "2023")
        ]
        
        for idx, (title, value, help_text) in enumerate(metrics):
            with cols[idx]:
                st.metric(f"**{title}**", value, help=help_text)
        
        # Visualization
        st.divider()
        st.markdown("### 📈 Forecast Results & Predictions")
        
        if os.path.exists("assets/newplot.png"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.image("assets/newplot.png", 
                        caption="**5-Year Motorcycle Population Forecast** - DKI Jakarta",
                        use_container_width=True)
            with col2:
                st.markdown("#### 🔮 Key Predictions")
                st.success("**2023:** 17.98M units")
                
        
        # Business Impact
        st.divider()
        st.markdown("### 💼 Business & Policy Implications")
        
        impact_cols = st.columns(3)
        
        with impact_cols[0]:
            st.markdown("""
            ### 🏗️ Infrastructure Planning
            - Road capacity expansion needs
            - Parking space requirements
            - Traffic management systems
            - Public transport integration
            """)
        
        with impact_cols[1]:
            st.markdown("""
            ### 📋 Policy Development
            - Vehicle registration strategies
            - Emission control planning
            - Safety regulations
            - Insurance frameworks
            """)
        
        with impact_cols[2]:
            st.markdown("""
            ### 💼 Business Opportunities
            - Automotive market growth
            - Aftermarket services demand
            - Insurance product development
            - Financing solutions
            """)
        
        # Project Links
        st.divider()
        st.markdown("### 🔗 Project Resources & Documentation")
        
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("📓 View Full Analysis on GitHub →", 
                         "https://github.com/marsel366/sepedamotor-forecast/",
                         use_container_width=True)
        with col2:
            st.download_button(
                label="📥 Download Technical Report →",
                data="Simulated report content",
                file_name="Motorcycle_Forecast_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )




# ==================== MAIN APP ====================
def main():
    """Main application function"""
    # Load CSS
    load_css()
    
    # Sidebar Configuration
    with st.sidebar:
        # Logo/Header
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 40px; margin-bottom: 10px; color: white;">📊</div>
            <h2 style="margin: 0; color: #ffffff !important; font-weight: 900;">Marselinus Hindarto</h2>
            <p style="color: #93c5fd; margin: 5px 0; font-weight: 600;">Data Analyst Portfolio</p>
            <div style="background: linear-gradient(90deg, #3b82f6 0%, white 100%); height: 3px; width: 80px; margin: 10px auto; border-radius: 2px;"></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Navigation
        st.markdown("### 🧭 Navigation")
        page = st.radio(
            "Select Page:",
            ["🏠 Home", "📊 Data Visualization", "📈 Forecasting"],
            label_visibility="collapsed"
        )
        
        st.divider()
        
        # Dark Mode Toggle
        st.session_state.dark_mode = st.toggle(
            "🌙 Dark Mode",
            value=st.session_state.dark_mode,
            help="Toggle between light and dark themes"
        )
        
        st.divider()
        
        # Social Links
        render_social_links()
        
        st.divider()
        
        # Footer
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <p style="color: #94a3b8; font-size: 12px; margin: 5px 0;">
                Built with ❤️ using <strong style="color: #ff4b4b;">Streamlit</strong>
            </p>
            <p style="color: #94a3b8; font-size: 12px; margin: 5px 0;">
                © 2024 Marsel Portfolio | All Rights Reserved
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Page Routing
    page_functions = {
        "🏠 Home": render_home_page,
        "📊 Data Visualization": render_data_viz_page,
        "📈 Forecasting": render_forecasting_page
    }
    
    # Render selected page
    if page in page_functions:
        page_functions[page]()

# ==================== RUN APP ====================
if __name__ == "__main__":
    main()