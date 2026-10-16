import streamlit as st
import pandas as pd
# Importing the backend logic that your partner will build
from backend import analyze_motif_enrichment

def main():
    st.set_page_config(page_title="Motif Enrichment Analyzer", layout="wide")
    
    st.title("Sequence Motif Enrichment Analyzer")
    st.write("Upload a set of biological sequences to determine if a specific motif is statistically enriched.")

    # Sidebar for inputs (UI/UX Polish)
    with st.sidebar:
        st.header("Analysis Parameters")
        
        # File upload handling
        uploaded_file = st.file_uploader("Upload Target Sequences (FASTA format)", type=["fasta", "fa", "txt"])
        
        # Motif input
        motif_input = st.text_input("Enter Motif (e.g., TATA, ATGC)", value="").upper()
        
        # Run button
        run_analysis = st.button("Run Enrichment Analysis", type="primary")

    # Main area for results
    if run_analysis:
        if not uploaded_file:
            st.warning("Please upload a FASTA file to proceed.")
        elif not motif_input:
            st.warning("Please enter a motif sequence.")
        else:
            with st.spinner("Analyzing sequences..."):
                # Call the backend function written by your partner
                # Passing the file object and the motif string
                try:
                    results_df = analyze_motif_enrichment(uploaded_file, motif_input)
                    
                    st.success("Analysis Complete!")
                    
                    st.subheader("Enrichment Results")
                    # Displaying the pandas DataFrame from the backend as requested
                    st.dataframe(results_df, use_container_width=True)
                    
                    # Placeholder for plot display
                    st.subheader("Visualization")
                    st.bar_chart(data=results_df, x="Sequence_ID", y="Motif_Count")
                    
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
    else:
        st.info("Please configure your parameters in the sidebar and click Run.")

if __name__ == "__main__":
    main()