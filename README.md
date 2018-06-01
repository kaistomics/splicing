Welcome to this site for the One-Class Support Vector Machine (OCSVM)-Splicing tool. This site will serve as a source code repository for OCSVM-Splicing pipeline. 

# Prerequisites
This program requires the following Python modules. 

1. Python (=> 2.7 ): https://www.python.org/
2. NumPy : http://www.numpy.org/
3. scikit-learn : http://scikit-learn.org/stable/index.html
4. computed splicing strength scores using MaxEntScan
*5' splice sites 

# Options
**-m** *INT* : OCSVM-Splicing model number (1,2,or 3) 
**-i** *STR* : Input file name 
**-o** *STR* : Output file name 

# Inputs 
1. model 1 

1. Fill out **conf_file**
 * Example
 ```
samtools_home = /cluster/data/scratch/share/samtools-0.1.19
bwa_home = /cluster/data/scratch/share/bwa-0.6.2
blast_home = /cluster/bio/bin
cap3_home = /cluster/data/scratch/share/CAP3/
fasta_location = /cluster/data/scratch/db/hg19/hg19.fasta
meerkat_home= /cluster/data/scratch/share/Meerkat/scripts
tea_home = /home/hcjung/Tea
tea_run = scripts/tea.pl
tea_assembly = lib/assembly
tmp_dir = /cluster/data/scratch/TEA_COAD/tmp
retro = repeat.combined.div30.isize150.fa
```
2. Copy of **conf_file** and **tea_run** into a directory with bam files that you want to run. 
 * Example
 
  ![Image of secondstep](https://github.com/hastj7373/TEA/blob/master/second_step.gif)

3. Execute **tea_run** 
 ```
 tea.run bam_input tea ra -c hg19 -p 5 -f -K
 ```
 In the current version, users need to input a bam file and set # of threads for the parameter *-p* (Keep other parameters like above). Note that users need to input a bam file without ".bam" (see the example below)
  * Example (see details by clicking 'View Raw' in [here](https://github.com/hastj7373/TEA/blob/master/Example.docx))
  
  ![Image of thridstep](https://github.com/hastj7373/TEA/blob/master/third_step.gif)
 
# Output Results

1.TEA produces **sample_name.germline.contig**
 * Output format is described in [here](https://github.com/hastj7373/TEA/blob/master/output_format.txt)

2.If you want to call somatic variants, use **somatic.call** script after running TEA on each sample. This script produces  **sample_name.soamtic.contig**
