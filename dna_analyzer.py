# ============================================================
# DNA Sequence Analyzer using Biopython
# Author: Harminder Kaur
# ============================================================

# ------------------------------------------------------------
# STEP 1: Import Required Libraries
# ------------------------------------------------------------
# Seq is used to perform biological operations like
# transcription, translation, and reverse complement.
# SeqIO is used to read DNA sequences from FASTA files.
from Bio.Seq import Seq
from Bio import SeqIO


# ------------------------------------------------------------
# STEP 2: Create a Function to Analyze One DNA Sequence
# ------------------------------------------------------------
# A function lets us reuse the same code whenever we need
# to analyze another sequence.
def analyze_dna(dna):

    # --------------------------------------------------------
    # STEP 2.1: Convert input to uppercase
    # --------------------------------------------------------
    # This ensures that 'atgc' and 'ATGC' are treated the same.
    dna = Seq(str(dna).upper())


    # --------------------------------------------------------
    # STEP 2.2: Validate DNA Sequence
    # --------------------------------------------------------
    # DNA should only contain A, T, G, and C.
    valid_bases = {"A", "T", "G", "C"}

    if not all(base in valid_bases for base in dna):
        print("\n❌ Invalid DNA Sequence!")
        return


    # --------------------------------------------------------
    # STEP 2.3: Calculate DNA Length
    # --------------------------------------------------------
    dna_length = len(dna)


    # --------------------------------------------------------
    # STEP 2.4: Calculate GC Content
    # --------------------------------------------------------
    gc_count = dna.count("G") + dna.count("C")
    gc_content = (gc_count / dna_length) * 100


    # --------------------------------------------------------
    # STEP 2.5: Count Each Nucleotide
    # --------------------------------------------------------
    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")


    # --------------------------------------------------------
    # STEP 2.6: Reverse Complement
    # --------------------------------------------------------
    reverse_complement = dna.reverse_complement()


    # --------------------------------------------------------
    # STEP 2.7: Transcription
    # --------------------------------------------------------
    # Convert DNA into RNA.
    rna = dna.transcribe()


    # --------------------------------------------------------
    # STEP 2.8: Translation
    # --------------------------------------------------------
    # Convert RNA into Protein.
    protein = rna.translate()


    # --------------------------------------------------------
    # STEP 2.9: Display Results
    # --------------------------------------------------------
    print("\n========== DNA ANALYSIS ==========")

    print("DNA Sequence :", dna)
    print("DNA Length :", dna_length)
    print("GC Content :", round(gc_content, 2), "%")

    print("\nNucleotide Count")
    print("----------------")
    print("A :", a_count)
    print("T :", t_count)
    print("G :", g_count)
    print("C :", c_count)

    print("\nReverse Complement :", reverse_complement)
    print("RNA Sequence :", rna)
    print("Protein Sequence :", protein)


    # --------------------------------------------------------
    # STEP 2.10: Save Results to a Text File
    # --------------------------------------------------------
    # "a" means append (don't overwrite previous results).
    with open("dna_results.txt", "a") as file:

        file.write("\n=============================\n")
        file.write(f"DNA Sequence: {dna}\n")
        file.write(f"DNA Length: {dna_length}\n")
        file.write(f"GC Content: {round(gc_content,2)}%\n")
        file.write(f"A Count: {a_count}\n")
        file.write(f"T Count: {t_count}\n")
        file.write(f"G Count: {g_count}\n")
        file.write(f"C Count: {c_count}\n")
        file.write(f"Reverse Complement: {reverse_complement}\n")
        file.write(f"RNA Sequence: {rna}\n")
        file.write(f"Protein Sequence: {protein}\n")

    print("\n✅ Results saved successfully.")


# ------------------------------------------------------------
# STEP 3: Main Menu
# ------------------------------------------------------------
# The program keeps running until the user chooses Exit.
while True:

    print("\n========== DNA ANALYZER ==========")
    print("1. Analyze Manual DNA Sequence")
    print("2. Analyze FASTA File")
    print("3. Exit")

    choice = input("Enter your choice: ")


    # --------------------------------------------------------
    # OPTION 1: Manual DNA Analysis
    # --------------------------------------------------------
    if choice == "1":

        while True:

            dna_input = input("\nEnter DNA Sequence: ")

            analyze_dna(dna_input)

            again = input("\nAnalyze another sequence? (yes/no): ").lower()

            if again != "yes":
                break


    # --------------------------------------------------------
    # OPTION 2: FASTA File Analysis
    # --------------------------------------------------------
    elif choice == "2":

        filename = input("\nEnter FASTA file name: ")

        try:

            # Read every sequence inside the FASTA file.
            for record in SeqIO.parse(filename, "fasta"):

                print("\nSequence ID:", record.id)

                analyze_dna(record.seq)

        except FileNotFoundError:

            print("\n❌ File not found.")


    # --------------------------------------------------------
    # OPTION 3: Exit Program
    # --------------------------------------------------------
    elif choice == "3":

        print("\nThank you for using DNA Analyzer!")
        break


    # --------------------------------------------------------
    # Invalid Menu Choice
    # --------------------------------------------------------
    else:

        print("\n❌ Invalid choice.")