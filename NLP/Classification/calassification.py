import nltk
import re
import pickle
import sys
import pprint


def feature_extractor( all_reviews ):
    result = []
    for review in all_reviews:
        flist ={}
        total_word = nltk.word_tokenize( review )
        pos = nltk.pos_tag(total_word)
        all_pos = [(tag[1]) for tag in pos]  # find all the tags in each review
        total_pos = len(pos)
        for value in pos:
            flist['UNIGRAM_POS_'+value[1]] = round( (all_pos.count(value[1]) / total_pos),4)
        total = len(total_word)
        for word in total_word:
            flist['UNIGRAM_'+word] = round(total_word.count(word)/total ,4)
        pos = nltk.pos_tag( total_word )
        pos_bigram = nltk.bigrams(pos) #contains tuples
        # example of all_pos_bigram NN_JJ , VBD_.
        all_pos_bigram = [(tuple[0][1]+'_'+tuple[1][1]) for tuple in pos_bigram] # extract firstPOS_secondPOS in bigrams
        total_pos = len(all_pos_bigram)
        for p in all_pos_bigram:
            flist['BIGRAM_POS_' + p] = round(all_pos_bigram.count(p) / total_pos, 4)
        bigram_num = len(total_word) - 1
        bigrams = nltk.bigrams(total_word)
        # contains of a the count of the bigrams / total number of that bigram in each review
        for word,count in nltk.FreqDist( bigrams ).most_common():
            flist['BIGRAM_'+ word[0]+'_'+word[1]] = round( (count/bigram_num),4 )
        result.append(flist)
    return result



def join_dict(dict1 , dict2):
    new_dict = []
    for i in range(len(dict1)):
        new_dict.append( list(dict1[i].items()) + list(dict2[i].items()) )
    return new_dict


def get_score(review):
    return int(re.search(r'Overall = ([1-5])', review).group(1))

def get_text(review):
    return re.search(r'Text = "(.*)"', review).group(1)

def process_reviews(file_name):
    file = open(file_name, "rb")
    raw_data = file.read().decode("latin1")
    file.close()

    positive_texts = []
    negative_texts = []
    document = []
    first_sent = None
    for review in re.split(r'\.\n', raw_data):
        overall_score = get_score(review)
        review_text = get_text(review)
        if overall_score > 3:
            positive_texts.append(review_text)
        elif overall_score < 3:
            negative_texts.append(review_text)
        if first_sent == None:
            sent = nltk.sent_tokenize(review_text)
            if (len(sent) > 0):
                first_sent = sent[0]
    document.append(positive_texts)
    document.append(negative_texts)
    return document

if __name__ == '__main__':
    #filename = sys.argv[1]
    file_name_train = "restaurant-training.data"
    file_name_development = "restaurant-development.data"
    pos_neg_reviews_train = process_reviews(file_name_train)
    pos_neg_reviews_development = process_reviews(file_name_development)

    pos_reviews = pos_neg_reviews_train[0]
    neg_reviews = pos_neg_reviews_train[1]

    pos_reviews_d = pos_neg_reviews_development[0]
    neg_reviews_d = pos_neg_reviews_development[1]


    feature_set = ([( feature ,'positive') for feature in feature_extractor(pos_reviews)] +
                   [( feature, 'negative') for feature in feature_extractor(pos_reviews)])

    feature_set_dev = ([(feature, 'positive') for feature in feature_extractor(pos_reviews_d)] +
                   [(feature, 'negative') for feature in feature_extractor(neg_reviews_d)])


    classifier = nltk.NaiveBayesClassifier.train(feature_set)
    print('Accuracy =', round(nltk.classify.accuracy(classifier,feature_set_dev)*100,4),'%')

    file = open('classifier.pickle','wb')
    pickle.dump(classifier,file)
    file.close()

    sys.stdout = open('informative-features.txt', 'w')
    print(classifier.show_most_informative_features())
    sys.stdout = sys.__stdout__

