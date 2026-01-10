import streamlit as st
import pandas as pd
import plotly.express as px
from ui import apply_custom_ui  # Ensure you have ui.py in the same folder

# 1. Page Config
st.set_page_config(page_title="Netflix 15-Graph Analysis", layout="wide")

# 2. Apply Styling
apply_custom_ui()

# 3. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('netflix_cleaned.csv')
    return df

df = load_data()

# 4. Sidebar Filters
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=150)
st.sidebar.header("Global Filters")
c_type = st.sidebar.multiselect("Content Type", options=df['type'].unique(), default=df['type'].unique())
year_range = st.sidebar.slider("Select Year", int(df['year'].min()), int(df['year'].max()), (2015, 2021))

f_df = df[(df['type'].isin(c_type)) & (df['year'].between(year_range[0], year_range[1]))]

# 5. Main Dashboard
st.title("🎬 Netflix 15-Graph Insight Dashboard")

# Top Metrics (No Boxes as requested)
c1, c2, c3 = st.columns(3)
c1.metric("Total Titles", len(f_df))
c2.metric("Avg Complexity", round(f_df['complexity_score'].mean(), 2))
c3.metric("Avg Duration", f"{round(f_df['duration_num'].mean(), 1)} min/eps")

st.divider()

# Tabs for 15 Graphs
t1, t2, t3 = st.tabs(["📊 Growth & Time", "🎭 Genre & Content", "🗺️ Strategy & Clusters"])

# --- TAB 1: 5 GRAPHS ---
with t1:
    st.subheader("1. Growth: Content Added Over Years")
    fig1 = px.area(f_df.groupby('year').size().reset_index(name='Count'), x='year', y='Count', color_discrete_sequence=['#E50914'], template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("2. Releases by Weekday")
        fig2 = px.bar(f_df['weekday'].value_counts(), color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)
        
        st.subheader("4. Best Month for Content")
        fig4 = px.line(f_df.groupby('month').size().reset_index(name='Count'), x='month', y='Count', color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig4, use_container_width=True)

    with col_b:
        st.subheader("3. Type Distribution (Pie)")
        fig3 = px.pie(f_df, names='type', hole=0.5, color_discrete_sequence=['#E50914', '#00815A'])
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("5. Gap: Release vs Added Year")
        fig5 = px.histogram(f_df, x='year_diff', nbins=20, color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig5, use_container_width=True)

# --- TAB 2: 5 GRAPHS ---
with t2:
    st.subheader("6. Top 10 Genres (Specific)")
    top_g = f_df['listed'].str.split(', ').explode().value_counts().head(10)
    fig6 = px.bar(x=top_g.values, y=top_g.index, orientation='h', color_discrete_sequence=['#E50914'], template="plotly_dark")
    st.plotly_chart(fig6, use_container_width=True)

    col_c, col_d = st.columns(2)
    with col_c:
        st.subheader("7. Genre Count per Title")
        fig7 = px.box(f_df, x='num_genres', color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig7, use_container_width=True)
        
        st.subheader("9. Complexity Score Violin")
        fig9 = px.violin(f_df, y="complexity_score", x="type", color="type", box=True, color_discrete_sequence=['#E50914', '#00815A'])
        st.plotly_chart(fig9, use_container_width=True)

    with col_d:
        st.subheader("8. Movie Duration (Minutes)")
        fig8 = px.histogram(f_df[f_df['type']=='Movie'], x='duration_num', color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig8, use_container_width=True)

        st.subheader("10. Cast Size vs Complexity")
        fig10 = px.scatter(f_df, x='num_cast', y='complexity_score', opacity=0.4, color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig10, use_container_width=True)

# --- TAB 3: 5 GRAPHS ---
with t3:
    st.subheader("11. Machine Learning Clusters (K-Means)")
    fig11 = px.scatter(f_df, x='complexity_score', y='duration_num', color='cluster', size='num_genres', hover_name='title', template="plotly_dark")
    st.plotly_chart(fig11, use_container_width=True)

    col_e, col_f = st.columns(2)
    with col_e:
        st.subheader("12. Ratings Distribution")
        fig12 = px.bar(f_df['rating'].value_counts(), color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig12, use_container_width=True)
        
        st.subheader("14. Top 10 Countries")
        fig14 = px.pie(f_df, names='country', color_discrete_sequence=px.colors.sequential.Reds_r)
        st.plotly_chart(fig14, use_container_width=True)

    with col_f:
        st.subheader("13. Top 10 Directors")
        top_d = f_df['director'].value_counts().head(11)[1:]
        fig13 = px.bar(x=top_d.index, y=top_d.values, color_discrete_sequence=['#E50914'], template="plotly_dark")
        st.plotly_chart(fig13, use_container_width=True)

        st.subheader("15. Rating Density by Type")
        fig15 = px.strip(f_df, x="rating", y="complexity_score", color="type", color_discrete_sequence=['#E50914', '#00815A'])
        st.plotly_chart(fig15, use_container_width=True)

       