import os
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from textblob import TextBlob
from tqdm import tqdm

tqdm.pandas()

USE_SAVE = True
LONG_WORK = True

# Get the number of cores
num_cores = os.cpu_count()
assert num_cores is not None
num_threads = max(1, num_cores - 1)


def read_file_status_bar(file_path: str) -> pd.DataFrame:
    total_lines = sum(1 for _ in open(file_path, "r"))

    with tqdm(total=total_lines, desc=f"Reading TSV: {file_path}", unit="line") as pbar:
        chunksize = total_lines // 200
        chunks = []

        for chunk in pd.read_csv(
            file_path, sep="\t", na_values=["\\N"], chunksize=chunksize
        ):
            chunks.append(chunk)

            # Update the progress bar
            pbar.update(chunksize)

    return pd.concat(chunks, axis=0, ignore_index=True)


def sentiment_create(principals: pd.DataFrame) -> pd.DataFrame:
    SENTIMENT_FILE = "title.basics.tsv/sentiment.tsv"
    if os.path.exists(SENTIMENT_FILE):
        sentiments = read_file_status_bar(SENTIMENT_FILE)
        return pd.merge(principals, sentiments, on="tconst")

    polarity_list = []
    subjectivity_list = []

    for title in tqdm(principals["primaryTitle"]):
        blob = TextBlob(str(title))
        polarity, subjectivity = blob.sentiment  # type: ignore
        polarity_list.append(polarity)
        subjectivity_list.append(subjectivity)

    principals["polarity"] = polarity_list
    principals["subjectivity"] = subjectivity_list

    # save sentiment analysis to file
    sentiments = pd.DataFrame(
        {
            "tconst": principals["tconst"],
            "polarity": polarity_list,
            "subjectivity": subjectivity_list,
        }
    )
    print("Saving sentiment analysis to file")
    sentiments.to_csv(SENTIMENT_FILE, sep="\t", index=False)

    return principals


def process_title_basics() -> pd.DataFrame:
    PREPROCESSED = "title.basics.tsv/preprocessed.tsv"
    DATA = "title.basics.tsv/data.tsv"
    if os.path.exists(PREPROCESSED) and USE_SAVE:
        return read_file_status_bar("title.basics.tsv/preprocessed.tsv")

    principals = read_file_status_bar(DATA)

    # drop unnecessary columns
    print(f"Preprocessing TSV: {DATA}")
    principals.drop("endYear", axis=1, inplace=True)
    principals.dropna(inplace=True)

    # change to proper types
    principals = principals.astype(
        dtype={
            "startYear": int,
            "isAdult": int,
            "runtimeMinutes": int,
        }
    )

    print("Creating new columns for each title type")
    principals = pd.get_dummies(principals, columns=["titleType"], dtype=int)

    print("Creating binary columns for each genre")
    genre_dummies = pd.get_dummies(
        principals["genres"].str.split(",", expand=True).stack().str.strip(), dtype=int
    )
    principals = pd.concat([principals, genre_dummies.groupby(level=0).max()], axis=1)
    del genre_dummies
    principals = principals.fillna(0)
    principals.drop("genres", axis=1, inplace=True)

    print("Creating new column to check if primaryTitle is same as originalTitle")
    principals["isSameTitle"] = (
        principals["primaryTitle"] == principals["originalTitle"]
    ).astype(int)

    if LONG_WORK:
        print("Creating new column with sentiment analysis of primaryTitle")
        principals = sentiment_create(principals)

        principals.drop("originalTitle", axis=1, inplace=True)

    # save preprocessed principals to file
    print(f"Saving preprocessed principals to file {PREPROCESSED}")
    principals.to_csv(PREPROCESSED, sep="\t", index=False)
    print("SAVED!")
    return principals


def generate_learning_table() -> pd.DataFrame:
    SCORES_FILE = "title.ratings.tsv/data.tsv"
    LEARNING_TABLE_FILE = "learning_table.tsv"
    if os.path.exists(LEARNING_TABLE_FILE) and USE_SAVE:
        return read_file_status_bar(LEARNING_TABLE_FILE)
        
    
    title_basics = process_title_basics()

    print(f"Adding scores")
    scores = read_file_status_bar(SCORES_FILE)
    scores.drop("numVotes", axis=1, inplace=True)
    all_data = pd.merge(title_basics, scores, on="tconst")

    # DELETE UUID
    all_data.drop("tconst", axis=1, inplace=True)
    
    # save titles to different variable
    titles = all_data["primaryTitle"]
    all_data.drop("primaryTitle", axis=1, inplace=True)
    

    # scale and normalize data
    print("Scaling and normalizing data")
    scores = all_data["averageRating"]
    all_data.drop("averageRating", axis=1, inplace=True)
    scaler = StandardScaler()
    scaled_data = pd.DataFrame(
        data=scaler.fit_transform(all_data), columns=all_data.columns
    )
    scaled_data["averageRating"] = scores
    scaled_data["primaryTitle"] = titles

    print(f"Saving learning table to file {LEARNING_TABLE_FILE}")
    scaled_data.to_csv(LEARNING_TABLE_FILE, sep="\t", index=False)
    print("SAVED!")
    
    return scaled_data


learning_table = generate_learning_table()

titles = learning_table["primaryTitle"]
learning_table.drop("primaryTitle", axis=1, inplace=True)
# ML process
NUM_FOLDS = 7
y_param = learning_table["averageRating"]
x_param = learning_table.drop("averageRating", axis=1)


# test scoring
print("Testing scores")
kf = KFold(n_splits=NUM_FOLDS, shuffle=True, random_state=42)
model = make_pipeline(PolynomialFeatures(degree=1), Ridge(alpha=10.0))
score_ridge = cross_val_score(
    model,
    x_param,
    y_param,
    cv=kf,
    verbose=3,
)
print(f"RMSE with ridge: {score_ridge.mean()} +/- {score_ridge.std()}\n")

X_train, X_test, y_train, y_test, titles_train, titles_test = train_test_split(x_param, y_param, titles, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Example scores and predictions")
for i in range(10):
    print(f"Actual: {y_test.iloc[i]}, Predicted: {predictions[i]}, Title: {titles_test.iloc[i]}")

plt.hist(y_test, bins=10, edgecolor='black', label='Actual')
plt.hist(predictions, bins=10, edgecolor='red', label='Predicted')
plt.xlabel('Score')
plt.ylabel('Count')
plt.title('Score Distribution')
plt.legend()
plt.show()
