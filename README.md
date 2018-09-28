# NER-system
Named Entity Recognition system for the CoNLL 2003 shared task

A Named Entity Recognition system for the English dataset in the CoNLL 2003 shared task. Trains on eng.train, tests on eng.testa and outputs eng.guessa with predicted NE tags.

The conllevel.perl can be used to determine accuracy, precision, recall and F1 scores for all the tags. The command for this is:

perl conlleval.perl < eng.guessa

Results split by type of named entity in Results.txt
