import nltk,re,collections
'''
def feature_extractor_unigram( all_reviews ):
    feature_uni_relative_freq = []
    feature_uni_pos = []
    for review in all_reviews:
        flist ={}
        total_word = nltk.word_tokenize( review )
        pos = nltk.pos_tag(total_word)
        all_pos = [(tag[1]) for tag in pos]  # find all the tags in each review
        total_pos = len(pos)
        # flist contains count of a specific POS / total number of POS in each review
        for value in pos:
            flist['UNIGRAM_POS_'+value[1]] = round( (all_pos.count(value[1]) / total_pos),4)
        #flist = [{'UNIGRAM_POS_' + v: round(all_pos.count(v) / total_pos, 4)} for k,v in pos]
        feature_uni_pos.append(flist)
        total = len(total_word)
        # flist contains count of a specific word / total number of word in each review
        flist = {}
        for word in total_word:
            flist['UNIGRAM_'+word] = round(total_word.count(word)/total ,4)
        #flist = [{'UNIGRAM_'+w : round(total_word.count(w)/total ,4)} for w in total_word]
        feature_uni_relative_freq.append(flist)
    return feature_uni_relative_freq , feature_uni_pos

def feature_extractor_bigram( all_reviews ):
    feature_bi_relative_freq = []
    feature_bi_pos = []

    for review in all_reviews:
        review_word = nltk.word_tokenize(review)
        pos = nltk.pos_tag( review_word )
        pos_bigram = nltk.bigrams(pos) #contains tuples
        # example of all_pos_bigram NN_JJ , VBD_.
        all_pos_bigram = [(tuple[0][1]+'_'+tuple[1][1]) for tuple in pos_bigram] # extract firstPOS_secondPOS in bigrams
        total_pos = len(all_pos_bigram)
        # flist contains count of a specific bigram POS / total number of bigram POS in each review
        flist = {}
        for p in all_pos_bigram:
            flist['BIGRAM_POS_' + p] = round(all_pos_bigram.count(p) / total_pos, 4)
        #flist = [{'BIGRAM_POS_' + p : round(all_pos_bigram.count(p) / total_pos, 4)} for p in all_pos_bigram]
        feature_bi_pos.append(flist)
        bigram_num = len(review_word) - 1
        bigrams = nltk.bigrams(review_word)
        # contains of a the count of the bigrams / total number of that bigram in each review
        flist = {}
        for word,count in nltk.FreqDist( bigrams ).most_common():
            flist['BIGRAM_'+ word[0]+'_'+word[1]] = round( (count/bigram_num),4 )
        #flist = [{'BIGRAM_'+ word[0]+'_'+word[1] : round( (count/bigram_num),4 ) } for word, count in nltk.FreqDist( bigrams ).most_common()]
        feature_bi_relative_freq.append(flist)
    return feature_bi_relative_freq,feature_bi_pos
'''

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
    file_name = "restaurant-training.data"
    pos_neg_reviews = process_reviews(file_name)

    pos_reviews = pos_neg_reviews[0]
    neg_reviews = pos_neg_reviews[1]

    '''
    pos_reviews = ['Yammy!!']
    neg_reviews = ['Horrible!!!']
    '''

    pos_features = feature_extractor(pos_reviews)
    neg_features = feature_extractor(neg_reviews)

    #print(pos_uni_feature_relative_freq[0])
    #pos_bi_feature_relative_freq, pos_bi_feature_POS = feature_extractor_bigram(pos_reviews)
    #neg_bi_feature_relative_freq, neg_bi_feature_POS = feature_extractor_bigram(neg_reviews)


    #for review in pos_uni_feature_relative_freq:
    #pos_uni_features = join_dict( pos_uni_feature_relative_freq , pos_uni_feature_POS)
    #pos_bi_features = join_dict(pos_bi_feature_relative_freq, pos_bi_feature_POS)

    #positive_features = join_dict(pos_uni_features , pos_bi_features)




    feature_set = []
    for feature in pos_features:
        feature_set.append( (feature , 'positive') )
    for feature in neg_features:
        feature_set.append((feature, 'negative'))




    classifier = nltk.NaiveBayesClassifier.train(feature_set)
    print( classifier.labels())
    #print(classifier.show_most_informative_features())
