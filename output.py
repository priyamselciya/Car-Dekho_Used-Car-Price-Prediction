import streamlit as st
import json

# Streamlit App Title
st.title("JSON File Viewer")

# Select a file to view
file_options = ["brand.json", "model_mapping.json", "variant_name_mapping.json"]
selected_file = st.selectbox("Choose a file to view:", file_options)

# Define file paths (make sure these are correct paths)
file_paths = {
    "brand.json": "D:/Car-Dekho_Used-Car-Price-Prediction/JSON_Files/brand.json",
    "model_mapping.json": "D:/Car-Dekho_Used-Car-Price-Prediction/JSON_Files/model_mapping.json",
    "variant_name_mapping.json": "D:/Car-Dekho_Used-Car-Price-Prediction/JSON_Files/variant_name_mapping.json"
}

# Display the content of the selected file
if selected_file:
    file_path = file_paths[selected_file]
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        st.write(f"Contents of `{selected_file}`:")
        st.json(data)  # Display JSON data
    except Exception as e:
        st.error(f"Error loading file `{selected_file}`: {e}")
