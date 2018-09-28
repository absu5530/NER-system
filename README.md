# NER-system
Named Entity Recognition system for the CoNLL 2003 shared task

A Named Entity Recognition system for the English dataset in the CoNLL 2003 shared task. Trains on eng.train, tests on eng.testa and outputs eng.guessa with predicted NE tags.

The conllevel.perl can be used to determine accuracy, precision, recall and F1 scores for all the tags. The command for this is:

perl conlleval.perl < eng.guessa




Results split by type of named entity:


processed 51578 tokens with 5942 phrases; found: 6225 phrases; correct: 5119.

accuracy:  97.73%; precision:  82.23%; recall:  86.15%; FB1:  84.15

LOC: precision:  87.45%; recall:  91.40%; FB1:  89.38  1920

MISC: precision:  84.38%; recall:  83.19%; FB1:  83.78  909

ORG: precision:  71.72%; recall:  77.33%; FB1:  74.42  1446

PER: precision:  83.90%; recall:  88.82%; FB1:  86.29  1950
