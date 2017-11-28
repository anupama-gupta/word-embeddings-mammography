# relation-extraction-mammography
File word_embeddings.7z contains the relation embeddings trained on 300,000 mammography reports. <br />
## Parameters used to train the embeddings - <br />
Architecture - skip-gram <br />
Context window size - 5 <br />
Vector Size - 300

## Steps to generate the word vectors 
7za e word_embeddings.7z  (Unzip word_embeddings.7z)
python print_embeddings.py word_embeddings (Print the words and their embeddings)

