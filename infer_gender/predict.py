import os
import sys
from pathlib import Path
import pickle as pickle
import tensorflow as tf
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from tensorflow.keras.preprocessing.sequence import pad_sequences

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


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
        pickle.dump(file, handle)
    print('Successfully persisted {}'.format(name))


def load_pickle(file_name):
    # print('pwd --> {}'.format(os.getcwd()))
    loaded_pickle = None
    with open('{}'.format(file_name), 'rb') as handle:
        loaded_pickle = pickle.load(handle)
    print('Successfully loaded {}'.format(file_name))
    return loaded_pickle


class GenderPredictor:
    def __init__(self):
        self.vocab_size = 27
        self.embedding_dim = 12
        self.max_length = 36
        self.trunc_type = 'post'
        self.oov_tok = "<OOV>"
        # load the persisted files
        data_path = Path(__file__).parent / Path("data")
        tokenizer_pickle_path = data_path / Path('tokenizer.pickle')
        if sys.version_info[0] ==3 and sys.version_info[1]<8:
            tokenizer_pickle_path = data_path / Path('py37') / Path('tokenizer.pickle')
        elif sys.version_info[0]<3:
            raise Exception("infer_gender doesn\'t support python2")
        model_path = data_path / Path('model.h5')

        print('Loading tokenizer pickle file from {}'.format(tokenizer_pickle_path))
        print('Loading model file from {}'.format(model_path))

        self.tokenizer = load_pickle(tokenizer_pickle_path)
        self.model = tf.keras.models.load_model(model_path, compile = False)

        # save_as_pickle(self.tokenizer, 'infer_gender/data/py37/tokenizer')

    def _transform_texts(self, texts):
        sample_sequences = self.tokenizer.texts_to_sequences(texts)
        sample_padded = pad_sequences(sample_sequences, maxlen=self.max_length, truncating=self.trunc_type)
        return sample_padded

    def predict_gender(self, names):
        preds = self.model.predict(self._transform_texts(names))
        pred_gender = ['Male' if pred >= 0.6 else 'Female' for pred in preds]
        return pred_gender

    def predict_gender_proba(self, names):
        preds = self.model.predict(self._transform_texts(names))
        # pred_gender = ['Male' if pred >= 0.6 else 'Female' for pred in preds]
        return preds

    # if __name__=='__main__':
    #     from infer_gender import GenderPredictor
    #     gp = GenderPredictor()
