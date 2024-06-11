from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse
import random

def replace_sequence_random(donor_seq, recipient_seq, percentage, output_path):
    """
    This function replaces a random part of the recipient sequence with a random part of the donor sequence
    of the same length, determined by a percentage of the length of the sequences.

    Input:
        donor_seq: The donor DNA sequence.
        recipient_seq: The recipient DNA sequence.
        percentage: The percentage of the sequence to be replaced.
        output_path: Path for the output file.
    """

    # Ensure the percentage is suitable
    if not (0 < percentage <= 100):
        raise ValueError("Percentage must be between 0 and 100")

    # Determine the replacement length based on the percentage
    replacement_length = int(min(len(donor_seq), len(recipient_seq)) * (percentage / 100))

    # Step 3. Initialize a random starting position for the replacement in the first sequence
    # Using random package, select the staring position in gen1 to be replaced
    start_gen1 = random.randint(0, len(donor_seq) - replacement_length)
    
    # Step 4. Get a random starting position for the replacement part in the second sequence
    # The same procedure as step 3
    start_gen2 = random.randint(0, len(recipient_seq) - replacement_length)
    
    # Step 5. Extraction of the part to be replaced from the first sequence
    # Sclicing procedure
    replacement_part = donor_seq[start_gen1:start_gen1 + replacement_length]
    
    # Step 6. Extract the replacement part from the second sequence
    original_part = recipient_seq[start_gen2:start_gen2 + replacement_length]

    # Step 7. Replace the part in the first sequence
    chimera_genome = recipient_seq[:start_gen2] + replacement_part + recipient_seq[start_gen2 + replacement_length:]
    
    # Create a SeqRecord for the output
    description = f"Replaced {percentage}% of donor sequence"
    output = SeqRecord(Seq(chimera_genome), id = "Chimeric Genome", description=description)

    # Write to the specified output file
    SeqIO.write(output, output_path, "fasta")
    print(f"Chimeric genome saved to {output_path}")

def main():
    desc = "Perform gene transfer events between two genomes in FASTA files."
    parser = argparse.ArgumentParser(description=desc)

    help_donor = "Path to the donor FASTA file."
    help_recipient = "Path to the recipient FASTA file."
    parser.add_argument("--donor", "-d", type=str, help=help_donor, required=True)
    parser.add_argument("--recipient", "-r", type=str, help=help_recipient, required=True)
    
    help_percentage = "Percentage of donor genome to be transferred."
    parser.add_argument("--percentage", "-p", type=float, help=help_percentage, required=True)
    
    help_output = "Name for the output modified FASTA file."
    parser.add_argument("--out", "-o", type=str, help=help_output, required=False, default="output.fasta")

    args = parser.parse_args()
    donor_record = SeqIO.read(args.donor, "fasta")
    recipient_record = SeqIO.read(args.recipient, "fasta")
    percentage = args.percentage
    output = args.out

    # Call the function with the parsed arguments
    replace_sequence_random(donor_record.seq, recipient_record.seq, percentage, output)

if __name__ == "__main__":
    main()
