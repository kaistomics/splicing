Welcome to this site for the One-Class SVM predictive models for splicing-altering variants. This site will serve as a source code repository for the predictive models. 

# Prerequisites
This program requires the following Python modules. 

1. Python (=> 2.7 ): https://www.python.org/
 * BWA 0.6.2 is required. 
2. Samtools
 * Samtools 0.1.5 or above. 
3. Meerkat
 * Download Meetkat and see its intall instruction at [Meerkat website](http://compbio.med.harvard.edu/Meerkat/). 
  * Make sure that Meerkat is correctly installed.  
4. TEA
 * Source code for the Tea pipeline at [GitHub](https://github.com/hastj7373/TEA).
 * CAP3 assembler.
 * R packages : Bioconductor, Rsamtools, IRanges and [spp](http://compbio.med.harvard.edu/Supplements/ChIP-seq/).
 * Download repeat library at [TEA website](http://compbio.med.harvard.edu/Tea/)(Donwload repeat.combined.div30.isize150.fa and move it to /TEA_installed/lib/assembly). 

# Running TEA

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
