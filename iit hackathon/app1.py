import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import zipfile
import io

# Streamlit App Title
st.title("📊 Social Media User Behavior Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload socialmedia.zip", type="zip")

if uploaded_file is not None:
    # Extract and read CSV from zip
    with zipfile.ZipFile(uploaded_file, "r") as z:
        csv_filename = z.namelist()[0]
        with z.open(csv_filename) as f:
            df = pd.read_csv(f)

    # Display DataFrame Head
    st.subheader("📌 Sample Data")
    st.dataframe(df.head(10))

    # Create IncomeGroup column
    df['IncomeGroup'] = pd.cut(df['Income'], bins=[0, 20000, 50000, 80000, 150000], labels=['Low', 'Mid', 'High', 'Very High'])

    # Create AgeGroup column
    df['AgeGroup'] = pd.cut(df['Age'], bins=[10, 20, 30, 40, 50, 60, 70], labels=['10s', '20s', '30s', '40s', '50s', '60s'])

    st.markdown("---")
    st.subheader("📈 Visualizations")

    # Tabs for each chart
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Platform vs Device Type", 
        "Connection Type by Location", 
        "Platform vs Income Group", 
        "Watch Reason by Platform", 
        "Addiction by Age Group", 
        "Self Control vs Productivity Loss"
    ])

    with tab1:
        st.write("### Platform Usage by Device Type")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data=df, x='Platform', hue='DeviceType', ax=ax)
        ax.set_title('Platform Usage by Device Type (Operations Insight)')
        ax.set_xlabel('Platform')
        ax.set_ylabel('Number of Users')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with tab2:
        st.write("### Connection Type Usage by Location")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.countplot(data=df, x='Location', hue='ConnectionType', order=df['Location'].value_counts().index, ax=ax)
        ax.set_title('Connection Type Usage by Location')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with tab3:
        st.write("### Platform Preference by Income Group")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data=df, x='Platform', hue='IncomeGroup', ax=ax)
        ax.set_title('Platform Preference by Income Group')
        st.pyplot(fig)

    with tab4:
        st.write("### Watch Reasons per Platform")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.countplot(data=df, x='Platform', hue='Watch Reason', ax=ax)
        ax.set_title('Watch Reasons per Platform')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with tab5:
        st.write("### Addiction Level by Age Group")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x='AgeGroup', y='Addiction Level', ax=ax)
        ax.set_title('Addiction Level by Age Group')
        st.pyplot(fig)

    with tab6:
        st.write("### Self Control vs Productivity Loss")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=df, x='Self Control', y='ProductivityLoss', hue='Platform', ax=ax)
        ax.set_title('Self Control vs Productivity Loss')
        st.pyplot(fig)

else:
    st.warning("Please upload the socialmedia.zip file to proceed.")