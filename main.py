import streamlit as st

# Page config
st.set_page_config(
    page_title="HBR - Uber Case Study Dashboard",
    layout="wide"
)

# ===== HEADER =====
# Create three columns: left logo, title, right logo
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    # Replace with your actual path or URL
    st.image("left_logo.png", use_container_width=True)

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
    # Replace with your actual path or URL
    st.image("right_logo.png", use_container_width=True)

st.markdown("---")  # horizontal divider

# ===== TABS =====
tab_metadata, tab_data_dict, tab_visualizations = st.tabs(
    ["Metadata", "Data Dictionary", "Visualizations"]
)

# -------- TAB 1: METADATA --------
with tab_metadata:
    st.subheader("Dataset Metadata")

    # Example structure – replace with your real content
    st.markdown("### Overview")
    st.write(
        """
        - **Case Study:** HBR – Uber
        - **Purpose:** Analyze key metrics, customer behavior, and operational patterns.
        - **Data Source:** *[Describe source here]*  
        - **Data Period:** *[e.g., Jan 2019 – Dec 2020]*  
        - **Number of Records:** *[e.g., 100,000]*  
        """
    )

    st.markdown("### Collection & Cleaning Notes")
    st.write(
        """
        - Data collected from *[system / export / API]*  
        - Missing values handled via *[method]*  
        - Outliers treated based on *[rules]*  
        - Timezone normalization: *[details]*  
        """
    )

# -------- TAB 2: DATA DICTIONARY --------
with tab_data_dict:
    st.subheader("Data Dictionary")

    # You can organize this however you like – here’s a simple layout
    st.markdown("### Variables")

    # Example data dictionary – replace with your own
    st.markdown()
    """
        | Variable Name      | Type        | Description                                   |
        |--------------------|------------|-----------------------------------------------|
        | `trip_id`          | String     | Unique identifier for each trip              |
        | `driver_id`        | String     | Unique identifier for each driver            |
        | `rider_id`         | String     | Unique identifier for each rider             |
        | `start_time`       | Datetime   | Trip start timestamp                         |
        | `end_time`         | Datetime   | Trip end timestamp                           |
        | `pickup_location`  | String     | Pickup neighborhood / zone                   |
        | `dropoff_location` | String     | Dropoff neighborhood / zone                  |
        | `fare_amount`      | Numeric    | Fare paid by the rider                       |
        | `surge_multiplier` | Numeric    | Surge factor applied to base fare            |
        | `trip_distance`    | Numeric_ n  
        """
