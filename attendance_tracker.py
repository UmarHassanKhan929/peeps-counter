import streamlit as st
import pandas as pd
import json

# Function to calculate "On-site" counts
def calculate_onsite_counts(data):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    onsite_counts = {day: 0 for day in days}

    for entry in data:
        for day in days:
            if entry.get(day) == "On-site":
                onsite_counts[day] += 1

    sorted_counts = dict(sorted(onsite_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

# Streamlit UI
st.title("Attendance Tracker - On-Site Days")
st.write("Upload a JSON file to get a breakdown of On-site attendance per day.")

# File upload
uploaded_file = st.file_uploader("Upload your JSON file", type=["json"])

if uploaded_file:
    # Load JSON data
    try:
        data = json.load(uploaded_file)
        st.success("File uploaded successfully!")

        # Convert to DataFrame
        df = pd.DataFrame(data)
        st.write("### Preview of Uploaded Data")
        st.dataframe(df)

        # Calculate counts
        st.write("### On-site Counts Per Day")
        onsite_counts = calculate_onsite_counts(data)

        # Display the results
        onsite_df = pd.DataFrame(list(onsite_counts.items()), columns=["Day", "On-site Count"])
        st.table(onsite_df)

    except Exception as e:
        st.error(f"Error processing file: {e}")