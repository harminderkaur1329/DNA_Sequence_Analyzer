# ============================================================
# DNA Sequence Analyzer using Streamlit
# Author: Harminder Kaur
# ============================================================


# ============================================================
# STEP 1: Import Libraries
# ============================================================
# streamlit -> Creates the web application
# Seq -> Performs DNA operations
# SeqIO -> Reads FASTA files
# StringIO -> Converts uploaded FASTA files into readable text

import streamlit as st
from Bio.Seq import Seq
from Bio import SeqIO
from io import StringIO

# ============================================================
# STEP 2: Create DNA Analysis Function
# ============================================================
# This function contains all the DNA analysis logic.
# We can call it from Manual Input OR FASTA Upload.

def analyze_dna(dna):

    # Convert sequence to uppercase
    dna = Seq(str(dna).upper())

    # --------------------------------------------------------
    # Validate DNA
    # --------------------------------------------------------
    valid_bases = {"A", "T", "G", "C"}

    if not all(base in valid_bases for base in dna):
        st.error("❌ Invalid DNA Sequence!")
        return

    # --------------------------------------------------------
    # DNA Length
    # --------------------------------------------------------
    dna_length = len(dna)

    # --------------------------------------------------------
    # GC Content
    # --------------------------------------------------------
    gc_count = dna.count("G") + dna.count("C")
    gc_content = (gc_count / dna_length) * 100

    # --------------------------------------------------------
    # Nucleotide Count
    # --------------------------------------------------------
    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")

    # --------------------------------------------------------
    # Reverse Complement
    # --------------------------------------------------------
    reverse = dna.reverse_complement()

    # --------------------------------------------------------
    # RNA
    # --------------------------------------------------------
    rna = dna.transcribe()

    # --------------------------------------------------------
    # Protein
    # --------------------------------------------------------
    protein = rna.translate()

    # --------------------------------------------------------
    # Display Results
    # --------------------------------------------------------
    # Display the original DNA sequence
    st.subheader("Original DNA Sequence")

    st.code(dna)

    st.success("✅ Valid DNA Sequence")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("DNA Length", dna_length)

    with col2:
        st.metric("GC Content", f"{gc_content:.2f}%")

    st.subheader("Nucleotide Count")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("A", a_count)
    c2.metric("T", t_count)
    c3.metric("G", g_count)
    c4.metric("C", c_count)

    st.subheader("Reverse Complement")
    st.code(reverse)

    st.subheader("RNA Sequence")
    st.code(rna)

    st.subheader("Protein Sequence")
    st.code(protein)

# ============================================================
# STEP 3: Create Download Report
# ============================================================
# Store all results in one formatted string.

    report = f"""
==============================
DNA ANALYSIS REPORT
==============================

Original DNA Sequence:
{dna}

DNA Length:
{dna_length}

GC Content:
{gc_content:.2f}%

Nucleotide Count
----------------
A : {a_count}
T : {t_count}
G : {g_count}
C : {c_count}

Reverse Complement:
{reverse}

RNA Sequence:
{rna}

Protein Sequence:
{protein}
"""

# ============================================================
 # STEP 3.1: Download Button
# ============================================================

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="DNA_Analysis_Report.txt",
        mime="text/plain",
         key=f"download_{str(dna)}"
    )


# ============================================================
# STEP 4: Configure Web Page
# ============================================================
# Sets the browser tab title, icon and layout.

st.set_page_config(
    page_title="DNA Sequence Analyzer",
    page_icon="🧬",
    layout="wide"
)


# ============================================================
# STEP 5: Create the App Title
# ============================================================
# Displays the heading at the top of the webpage.

st.title("🧬 DNA Sequence Analyzer")

st.write("Analyze DNA sequences using Biopython.")


# ============================================================
# STEP 6: Sidebar Menu
# ============================================================

st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Choose Analysis Type",
    [
        "Manual DNA Input",
        "Upload FASTA File"
    ]
)

# ============================================================
# STEP 7: Manual DNA Input
# ============================================================

if option == "Manual DNA Input":

    dna_input = st.text_area(
        "Enter DNA Sequence",
        height=150
    )

    analyze = st.button("Analyze DNA")

    if analyze:
        
        dna = Seq(dna_input.upper())

        analyze_dna(dna)

# ============================================================
# STEP 8: Upload FASTA File
# ============================================================

elif option == "Upload FASTA File":

    uploaded_file = st.file_uploader(
        "Choose a FASTA File",
        type=["fasta", "fa", "txt"]
    )
# ============================================================
# STEP 9: Check if File is Uploaded
# ============================================================

    if uploaded_file is not None:

        st.success("✅ FASTA File Uploaded Successfully!")

        fasta_data = StringIO(
            uploaded_file.getvalue().decode("utf-8")
        )

        for record in SeqIO.parse(fasta_data, "fasta"):

            st.header(record.id)

            analyze_dna(record.seq)

            st.divider()

# ============================================================
# STEP 10: Footer
# ============================================================

st.divider()

st.markdown(
    """
---
Developed by Harminder Kaur

Powered by Python • Biopython • Streamlit
"""
)



