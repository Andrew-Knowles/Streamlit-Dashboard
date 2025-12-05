import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="HBR - Uber Case Study Dashboard",
    layout="wide"
)

# ========= LOAD DATA FROM GOOGLE SHEETS =========
data_url = "https://docs.google.com/spreadsheets/d/1fTpJACr1Ay6DEIgFxjFZF8LgEPiwwAFY/edit?usp=sharing&ouid=103457517634340619188&rtpof=true&sd=true"

@st.cache_data
def load_file(url: str) -> dict:
    # More robust: cut everything after /edit?
    base = url.split("/edit?")[0]
    modified_url = base + "/export?format=xlsx"

    # Load ALL sheets from the Excel file
    all_sheets = pd.read_excel(modified_url, sheet_name=None)

    data = {}
    for sheet_name, df in all_sheets.items():
        data[sheet_name] = df
    return data

data = load_file(data_url)

# Optional: pick which sheet to look at
sheet_names = list(data.keys())
default_sheet = "Switchbacks" if "Switchbacks" in sheet_names else sheet_names[0]
current_sheet = default_sheet  # or use a selectbox somewhere if you want

# ===== HEADER =====
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.image("data file/Uber-logo.png", use_container_width=True)

with col2:
    st.markdown(
        """
        <h1 style="text-align: center; margin-bottom: 0;">
            HBR - Uber Case Study Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("data file/rice-logo.jpg", use_container_width=True)

st.markdown("---")

# ===== TABS =====
tab_metadata, tab_data_dict, tab_visualizations = st.tabs(
    ["Metadata", "Data Dictionary", "Visualizations"]
)

# -------- TAB 1: METADATA --------
# -------- TAB 1: METADATA --------
with tab_metadata:
    st.subheader("Dataset Metadata")

    # Pull metadata text from the Copyright sheet
    try:
        metadata_text = show_metadata(data)

        st.markdown("### Source Metadata (from Google Sheets)")
        st.markdown(
            f"""
            <div style="padding:12px; background-color:#f0f2f6; border-radius:8px;">
                <pre style="white-space: pre-wrap;">{metadata_text}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Could not load metadata: {e}")

# -------- TAB 2: DATA DICTIONARY --------
with tab_data_dict:
    st.subheader("Data Dictionary")
    st.markdown("### Variables")

    # Fix: st.markdown must wrap the triple-quoted string
    st.markdown(
        """
        | Variable Name      | Type         | Description                                   |
        |--------------------|-------------|-----------------------------------------------|
        | `trip_id`          | String      | Unique identifier for each trip               |
        | `driver_id`        | String      | Unique identifier for each driver             |
        | `rider_id`         | String      | Unique identifier for each rider              |
        | `start_time`       | Datetime    | Trip start timestamp                          |
        | `end_time`         | Datetime    | Trip end timestamp                            |
        | `pickup_location`  | String      | Pickup neighborhood / zone                    |
        | `dropoff_location` | String      | Dropoff neighborhood / zone                   |
        | `fare_amount`      | Numeric     | Fare paid by the rider                        |
        | `surge_multiplier` | Numeric     | Surge factor applied to base fare             |
        | `trip_distance`    | Numeric     | Distance of the trip (e.g., in km or miles)   |
        | `trip_status`      | Categorical | Completed / Cancelled / No-show               |
        """
    )

    st.info("Update this table to match the actual columns in your Google Sheets data.")

# -------- TAB 3: VISUALIZATIONS --------
with tab_visualizations:
    st.subheader("Visualizations")

    st.markdown(
        """
        This tab uses the data loaded from the Google Sheets document.  
        Below is a simple preview of the `Switchbacks` (or default) sheet and a placeholder for charts.
        """
    )

    st.markdown(f"### Data preview: `{current_sheet}`")
    st.dataframe(data[current_sheet].head())

    # Example: if there is a numeric column to plot, you can quickly visualize it.
    # Replace 'SomeNumericColumn' with a real column name from the sheet.
    if not data[current_sheet].empty:
        numeric_cols = data[current_sheet].select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            col_to_plot = st.selectbox("Select numeric column to plot", numeric_cols)
            st.line_chart(data[current_sheet][col_to_plot])
        else:
            st.warning("No numeric columns found in this sheet to plot.")

