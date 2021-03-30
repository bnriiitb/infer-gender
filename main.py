from infer_gender import GenderPredictor

if __name__ == '__main__':
    gp = GenderPredictor()
    print(gp.predict_gender(['nagaraju budigam']))