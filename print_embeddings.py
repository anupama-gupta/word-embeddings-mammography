import sys
import gensim

def print_vectors(model):
	for word in model.vocab:
		print word, " ", model[word]

if __name__ == "__main__":

    vec_file = sys.argv[1]
    model = gensim.models.Word2Vec.load(vec_file)
    print_vectors(model)


