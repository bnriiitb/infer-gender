import pickle
import tensorflow as tf
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from tensorflow.keras.preprocessing.sequence import pad_sequences


def compute_scores(df, pred_col):
    precision, recall, f1_score, support = precision_recall_fscore_support(df.gender, df[pred_col], average='binary')
    accuracy = accuracy_score(df.gender, df[pred_col])
    print('precision --> ', precision)
    print('recall --> ', recall)
    print('f1_score --> ', f1_score)
    print('accuracy --> ', accuracy)
    return (precision, recall, f1_score, accuracy)


def save_as_pickle(file, name):
    # saving
    with open('{}.pickle'.format(name), 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('successfully persisted {}'.format(name))


def load_pickle(file_name):
    loaded_pickle = None
    with open('{}.pickle'.format(file_name), 'rb') as handle:
        loaded_pickle = pickle.load(handle)
    print('successfully loaded {}'.format(file_name))
    return loaded_pickle


class GenderPredictor:
    def __init__(self):
        self.vocab_size = 27
        self.embedding_dim = 12
        self.max_length = 36
        self.trunc_type = 'post'
        self.oov_tok = "<OOV>"
        # load the persisted files
        self.tokenizer = load_pickle('infer_gender/model/tokenizer')
        self.model = tf.keras.models.load_model("infer_gender/model/model.h5")

    def transform_texts(self, texts):
        sample_sequences = self.tokenizer.texts_to_sequences(texts)
        sample_padded = pad_sequences(sample_sequences, maxlen=self.max_length, truncating=self.trunc_type)
        return sample_padded

    def predict_gender(self,names):
        preds = self.model.predict(self.transform_texts(names))
        pred_gender = ['Male' if pred>=0.6 else 'Female' for pred in preds]
        return pred_gender