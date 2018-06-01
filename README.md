Welcome to this site for the One-Class Support Vector Machine (OCSVM)-Splicing tool. This site will serve as a source code repository for OCSVM-Splicing pipeline. 

# Prerequisites
This program requires the following modules. 

1. Python (=> 2.7 ): https://www.python.org/
2. NumPy : http://www.numpy.org/
3. scikit-learn : http://scikit-learn.org/stable/index.html
4. computed splicing strength scores using MaxEntScan
   - 5' splice sites : http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html
   - 3' splice sites : http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq_acc.html

# Options

1. **-m** *INT* : OCSVM-Splicing model number (1,2,or 3) 
2. **-i** *STR* : Input file name 
3. **-o** *STR* : Output file name 

   ```
   example:  python one_calss_SVM.py -m 1 -i model_1_input.txt -o model_1_output.txt
   
   ```

# OCSVM-Splicing models
* **Model 1 : Intornic SNVs at 5' splice sites (within 4bp next to GT)**
 
 ![Image of model 1](https://github.com/kaistomics/splicing/blob/master/model1.png)

score of 5’splice<sup>MUT</sup> – 5’spliceWT 

* **Model 2 : Intornic SNVs at 3' splice sites (within 1bp next to AG)**
 
 ![Image of model 2](https://github.com/kaistomics/splicing/blob/master/model2.png)
 
* **Model 3 : Exonic SNVs at 5' splice sites (within 2bp next to GT)**
 
 ![Image of model 3](https://github.com/kaistomics/splicing/blob/master/model3.png)
 
 
 
# Output Results

Each model annotes SNVs as **"benign"** or **"deleterious"**.
   - example
  ![Image of output](https://github.com/kaistomics/splicing/blob/master/output_example.png) 


