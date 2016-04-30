import nltk
import re
import pickle
import sys
import pprint

def feature_extractor( all_reviews ):
    result = []
    for review in all_reviews:
        flist ={}
        total_word = nltk.word_tokenize(review)
        pos = nltk.pos_tag(total_word)
        all_pos = [(tag[1]) for tag in pos]  # find all the tags in each review
        total_pos = len(pos)
        pos_count = nltk.FreqDist(all_pos).most_common()
        for value in pos_count:
            flist['UNIGRAM_POS_' + value[0]] = value[1] / total_pos
        total = len(total_word)
        word_count = nltk.FreqDist(total_word).most_common()
        for w in word_count:
            flist['UNIGRAM_' + w[0]] = w[1] / total
        pos_bigram = nltk.bigrams(pos) #contains tuples
        all_pos_bigram = [(tuple[0][1]+'_'+tuple[1][1]) for tuple in pos_bigram] # extract firstPOS_secondPOS in bigrams
        total_pos = len(all_pos_bigram)
        all_bi_pos = nltk.FreqDist(all_pos_bigram).most_common()
        for value in all_bi_pos:
            flist['BIGRAM_POS_' + value[0]] = value[1] / total_pos
        bigram_num = len(total_word) - 1
        bigrams = nltk.bigrams(total_word)
        for word,count in nltk.FreqDist( bigrams ).most_common():
            flist['BIGRAM_'+ word[0]+'_'+word[1]] = count/bigram_num
        result.append(flist)
    return result


def generate_file(feature_set, file_name):
    pos_line = ''
    neg_line = ''
    for data in feature_set:
        if data[1] == 'positive':
            pos_line += 'positive '
            for key in data[0]:
                pos_line += key + ':' + str(data[0][key]) + ' '
            pos_line += '\n'
        elif data[1] == 'negative':
            neg_line += 'negative '
            for key in data[0]:
                neg_line += key + ':' + str(data[0][key]) + ' '
            neg_line += '\n'


    re.sub(r'positive \w','**',pos_line)
    #pos_line.replace(r'positive \n','')
    with open(file_name, 'w+', encoding='UTF-8') as file:
        file.write(pos_line)
        file.write(neg_line)


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
    file_name_test = "restaurant-testing.data"

    pos_neg_reviews_train = process_reviews(file_name_train)
    pos_neg_reviews_development = process_reviews(file_name_development)
    pos_neg_reviews_test = process_reviews(file_name_test)


    pos_reviews = pos_neg_reviews_train[0]
    neg_reviews = pos_neg_reviews_train[1]

    pos_reviews_dev = pos_neg_reviews_development[0]
    neg_reviews_dev = pos_neg_reviews_development[1]

    pos_reviews_test = pos_neg_reviews_test[0]
    neg_reviews_test = pos_neg_reviews_test[1]

    feature_set = ([( feature ,'positive') for feature in feature_extractor(pos_reviews)] +
                   [( feature, 'negative') for feature in feature_extractor(neg_reviews)])


    generate_file(feature_set,'training-features.txt')


    feature_set_dev = ([(feature, 'positive') for feature in feature_extractor(pos_reviews_dev)] +
                      [(feature, 'negative') for feature in feature_extractor(neg_reviews_dev)])

    generate_file(feature_set_dev, 'development-features.txt')


    feature_set_test = ([(feature, 'positive') for feature in feature_extractor(pos_reviews_test)] +
                       [(feature, 'negative') for feature in feature_extractor(neg_reviews_test)])

    generate_file(feature_set_test, 'testing-features.txt')

    classifier = nltk.NaiveBayesClassifier.train(feature_set)
    with open('restaurant-baseline-model-P1.pickle','wb') as file:
        pickle.dump(classifier, file)

    print('Accuracy =', nltk.classify.accuracy(classifier,feature_set_dev)*100,'%')
    print(classifier.labels())
    sys.stdout = open('informative-features.txt', 'w')
    print(classifier.show_most_informative_features(20))
    sys.stdout = sys.__stdout__



