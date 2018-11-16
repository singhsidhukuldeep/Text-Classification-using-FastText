
# Note: This example code is written for Python 3.6+!
import json
from pathlib import Path

reviews_data = Path("dataset") / "review.json"
fasttext_data = Path("fasttext_dataset.txt")

with reviews_data.open() as input, fasttext_data.open("w") as output:
    for line in input:
        review_data = json.loads(line)

        rating = review_data['stars']
        text = review_data['text'].replace("\n", " ")

        fasttext_line = "__label__{} {}".format(rating, text)

        output.write(fasttext_line + "\n")