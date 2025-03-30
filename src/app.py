import os

import cloudpickle
import folium
import pandas as pd
import streamlit as st

from parse_pdf import extract_police_report_data

st.set_page_config(
    page_title="CityX Crime Watch",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto",
)


# load crime classifier model
with open("crime-classifier.pkl", "rb") as f:
    model = cloudpickle.load(f)


# display cityX map
def create_folium_map(df):
    districts = (
        df.groupby("PdDistrict")
        .agg({"latitude": "mean", "longitude": "mean"})
        .reset_index()
    )

    mean_lat = df["latitude"].mean()
    mean_lon = df["longitude"].mean()

    m = folium.Map(location=[mean_lat, mean_lon], zoom_start=12, control_scale=True)

    # add districts
    for _, row in districts.iterrows():
        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=f"District: {row['PdDistrict']}",
            icon=folium.Icon(color="blue"),
        ).add_to(m)

    folium.LayerControl().add_to(m)
    return m


# app title
st.title("CityX Crime Watch 🖥️")

df = pd.read_csv("../data/dataset-cleaned.csv")
folium_map = create_folium_map(df)
st.components.v1.html(folium_map._repr_html_(), height=650)

# file uploader
st.subheader("Upload a Police Report")
uploaded_pdf = st.file_uploader("Upload a PDF with the police report", type=["pdf"])


# handle uploaded file and parse content
def handle_pdf_upload(uploaded_pdf):
    temp_file_path = os.path.join(".", "uploaded_report.pdf")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    # extract pdf content
    data = extract_police_report_data(temp_file_path)

    # remove file from system
    os.remove(temp_file_path)
    return data


# display report info
if uploaded_pdf is not None:
    data = handle_pdf_upload(uploaded_pdf)

    st.subheader("Extracted Police Report Data")

    # Convert extracted data to DataFrame for display
    df_report = pd.DataFrame(data.items(), columns=["key", "value"])
    st.table(df_report)

    # Get detailed description for classification
    detailed_description = data.get("Detailed Description", "")

    if detailed_description:
        # Predict crime category & severity
        preds = model.classify(detailed_description)

        # Display classification results
        st.info(f"**Predicted Crime Category:** {preds['category']}")
        st.warning(f"**Crime Severity Level:** {preds['severity']}")
