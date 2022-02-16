# Introduction
This repository includes a free-cash flow model that simulates the potential of large-scale offshore wind P2H. The model is made in Vensim PLE and enriched with the EMA-workbench in Python. It is the first publicaly available ESDMA model with the use of Vensim PLE - Jan 22'. Feel free to explore the model behaviour. 

# Vensim PLE models
Recognize the .vpmx files. These are the published Vensim PLE models that represent the techno-economic model. The 'model_inputs' files show the model inputs and formulas. 

# Python - EMA workbench application
The system dynamics (SD) models interact with the EMA workbench applied in PyCharm. The modeling method is therefore called ESDMA. The workbench is made to interact with Vensim DSS, however, the integration of a Pysd (another SD python package) connector allows to interact with Vensim PLE - the unpayed version. 

The MAIN Py models are listed with a 1 in front of the filename.
The applied result methodologies during the research are listed with a 2 and 3, where the 2 represents models without a comparison (i.e. policy) and 3 does.
The inapplicable result methodologies (in relation to the Internship) are listed with a 4 in front of the filename. They, however, may be interesting to use in another context.

Lastly, a txt file is added. This can be uploaded in the 'cmd prompt' to immediately install the required PyCharm packages. 

Good luck! Ids Dijkstra
