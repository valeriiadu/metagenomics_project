# Lateral Gene Transfer Generator
This code was developed as part of a project carried out during the Microbial Metagenomics course (Molecular Biology master degree) at the University of Padova. The project was supervised by Prof. Stefano Campanaro, Dr. Sofia Fraulini.

## Overview

This script simulates horizontal gene transfer (HGT) by generating chimeric genomes. It takes two input genomes in FNA format and replaces a portion of the recipient genome with a portion of the donor genome. The modified genome is then saved to a new FASTA file. This script can be used to test the efficiency of software tool like FastANI in dealing with such generated variants.

## Features

- **Input**: Two complete genomes in FNA format.
- **Output**: A chimeric genome in FASTA format.
- **Customizable**: Specify the percentage of the genome to be replaced.
- **Randomized**: Randomly selects regions for replacement, ensuring variability in each run.

## Requirements

- Python 3.x
- Biopython
- argparse

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install Biopython using pip:
    ```bash
    pip install biopython
    ```
3. Install FastANI using conda:
    ```bash
    conda create -n fastani -c bioconda fastani
    ```
## Usage

To run the script, use the following command:

```bash
python chimera_gen.py --donor donor.fna --recipient recipient.fna --percentage 10 --out chimeric_genome.fasta
```

### Arguments

- `--donor` (`-d`): Path to the donor FASTA file (required).
- `--recipient` (`-r`): Path to the recipient FASTA file (required).
- `--percentage` (`-p`): Percentage of the donor genome to be transferred (required).
- `--out` (`-o`): Name for the output modified FASTA file (default: `output.fasta`).

## Example

```bash
python chimera_gen.py --donor Methanoculleus_marisnigri_JR1.fna --recipient Lactobacillus_acidophilus_La-14.fna --percentage 10 --out chimeric_genome.fasta
```

## Script Details

The script performs the following steps:

1. **Load the Genomes**: Reads the donor and recipient genomes from the provided FNA files.
2. **Validate Percentage**: Ensures the percentage provided is between 0 and 100.
3. **Determine Replacement Length**: Calculates the length of the sequence to be replaced based on the percentage.
4. **Select Random Start Positions**: Chooses random starting positions in both genomes for the replacement region.
5. **Extract Sequences**: Extracts the sequence segments to be replaced from both genomes.
6. **Create Chimeric Genome**: Replaces the segment in the donor genome with the segment from the recipient genome.
7. **Save the Output**: Writes the modified genome to the specified output file.

## Further Work

### Part 1: Generate Chimeric Genomes

1. Develop a Python script to parse both genomes and perform gene transfer events.
2. Track modifications to the recipient genome and validate the accuracy.
3. Output the modified genome in FASTA format and log the locations of applied modifications.

### Part 2: Analyze Software Performance

1. Execute the script multiple times with varying lengths of HGTs.
2. Use FastANI to compute ANI between the original and modified genomes using:
    ```bash
    fastANI -r original_genome.fasta --ql query_list.txt -o output_file
    ```
3. Analyze the impact of mutations on software performance using statistical tools (RStudio tools).
4. Plot the relationship between the ength of HGTs and ANI.
5. Optionally, repeat with different donor genomes from various taxonomic groups to assess the impact of phylogenetic distance.

## Authors
Ghiotto Chiara, Gorbunova Valeriia, Masone Felicita Pia

## Contribution

Contributions to this project are welcome. Please create a fork and submit a pull request with your changes.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer.

---

This README provides a comprehensive guide to using the Lateral Gene Transfer Generator script. Follow the instructions to generate chimeric genomes and analyze their impact on genome comparison tools.
