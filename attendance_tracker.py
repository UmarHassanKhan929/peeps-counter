import streamlit as st
import pandas as pd
import json

# Function to calculate "On-site", "WFH", and "N/A" counts
def calculate_counts(data):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    counts = {day: {"On-site": 0, "WFH": 0, "N/A": 0} for day in days}

    for entry in data:
        for day in days:
            value = entry.get(day, "N/A")
            if value in counts[day]:
                counts[day][value] += 1

    # Flatten the counts dict into a list of rows for the DataFrame
    flattened_counts = [
        {
            "Day": day,
            "On-site Count": counts[day]["On-site"],
            "WFH Count": counts[day]["WFH"],
            "N/A Count": counts[day]["N/A"],
        }
        for day in days
    ]

    return flattened_counts

# Streamlit UI
st.title("Attendance Tracker - Day-wise Breakdown")
st.write("Upload a JSON file to get a breakdown of 'On-site', 'WFH', and 'N/A' attendance per day.")

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

        # Calculate counts for On-site, WFH, and N/A
        st.write("### Day-wise Breakdown of Attendance")
        counts = calculate_counts(data)

        # Display the results
        counts_df = pd.DataFrame(counts)
        st.table(counts_df)

    except Exception as e:
        st.error(f"Error processing file: {e}")