# word-embeddings-mammography
File word_embeddings.7z contains the word vectors trained on 300,000 mammography reports. <br />
## Parameters used to train the embeddings - <br />
Architecture - skip-gram <br />
Context window size - 5 <br />
Vector Size - 300

## Usage <br />
### Unzip word_embeddings.7z
$ 7za e word_embeddings.7z 
### Print the words and their embeddings
$ python get_embeddings.py word_embeddings

