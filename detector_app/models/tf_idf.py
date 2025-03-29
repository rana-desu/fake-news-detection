import pandas as pd
from detector_app import preprocessor
from sklearn.feature_extraction.text import TfidfTransformer

def main():
    df = pd.read_csv(r"dataset/2/fake_and_real_news.csv")
    print(df.shape)

    # vectorizer = TfidfTransformer()
    # x = vectorizer.fit_transform(df)

if __name__ == "__main__":
    main()