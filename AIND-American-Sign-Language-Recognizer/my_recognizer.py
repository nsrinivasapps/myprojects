import warnings
from asl_data import SinglesData
import numpy as np


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer    
    for n in range(test_set.num_items):
        testX,testlength = test_set.get_item_Xlengths(n)
        scores = {}
        best_guess_word = None
        best_test_score = np.float('-inf')
        for word in models:
            trained_model = models[word]
            try:
                test_score = trained_model.score(testX,testlength)
                scores[word] = test_score
                if test_score >= best_test_score:
                    best_test_score = test_score
                    best_guess_word = word                
            except: 
                scores[word] = np.float('-inf')
        probabilities.append(scores)
        guesses.append(best_guess_word)            
    return probabilities, guesses
    #raise NotImplementedError
