import pandas as pd
from Bio import SeqIO
import io

def analyze_motif_enrichment(fasta_file, motif):
    """
    Core enrichment algorithm.
    Reads the FASTA file, counts motif occurrences, and performs statistical tests.
    Returns a pandas DataFrame.
    """
    # Read the uploaded file content using Biopython
    stringio = io.StringIO(fasta_file.getvalue().decode("utf-8"))
    records = list(SeqIO.parse(stringio, "fasta"))
    
    # Mock data generation (Your partner will replace this with real math/logic)
    results = []
    for record in records:
        sequence_str = str(record.seq).upper()
        # Basic counting for the placeholder
        count = sequence_str.count(motif)
        
        results.append({
            "Sequence_ID": record.id,
            "Sequence_Length": len(sequence_str),
            "Motif_Count": count,
            "P_Value": 0.05 / (count + 1) # Mock p-value calculation
        })
    
    # Convert to pandas DataFrame for the front-end to render
    df = pd.DataFrame(results)
    
    # If no records were found, return empty df with correct columns
    if df.empty:
         df = pd.DataFrame(columns=["Sequence_ID", "Sequence_Length", "Motif_Count", "P_Value"])
         
    return df