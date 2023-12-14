import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Streamlit app
def main():
    st.title("CSV Upload and Age Histogram Plotter")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Validate if the necessary columns exist
        if 'name' in df.columns and 'age' in df.columns:
            # Plotting a histogram of ages
            st.write("Histogram of Ages")
            fig, ax = plt.subplots()
            df['age'].hist(bins=20, ax=ax)
            st.pyplot(fig)
        else:
            st.error("CSV file must contain 'name' and 'age' columns.")

if __name__ == "__main__":
    main()
