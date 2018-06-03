import sys
import os
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import sys, getopt


myopts, args = getopt.getopt(sys.argv[1:],"m:i:o:") 

model=''
input_file=''
output_file=''
for o,a in myopts : 
  if o == '-m' :
    model = a
  elif o == '-i' :
    input_file = a
  elif o == '-o' :
    output_file = a
    

print 'model number' + ':' +  model
print 'input_file' + ':' + input_file
print 'output_file' + ':' + output_file


if model == '1' :
  clf = joblib.load('model1.pkl') 
elif model == '2' :
  clf = joblib.load('model2.pkl')
elif model == '3' :
  clf = joblib.load('model3.pkl')


f=open(input_file,'r')
fline = f.readline()
head = fline
fline = f.readline()
test=[]
while fline :
        fline = fline.strip()
        fso = fline.split('\t')
        instance=[]
        instance.append(float(fso[0]))
        instance.append(float(fso[1]))
        test.append(instance)
        fline = f.readline()
f.close()

X_test = np.r_[test]
predicted = clf.predict(X_test)


#output
g=open(output_file,'w')
g.write(head)
i=0
while i < len(predicted) :
  g.write(str(test[i][0]) + '\t' + str(test[i][1]))
  if predicted[i] == 1 :
    g.write('\t' + 'deleterious' + '\n')
  elif predicted[i] == -1 :
    g.write('\t' + 'benign' + '\n')
  i=i+1
g.close()

print "\n\ndone!"



  







