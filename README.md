# vsm

This code implements **Vector Space Model** for information retrieval.

## Dependencies

NLTK

```bash
import nltk
packages = ['punkt', 'stopwords']
nltk.download(packages)
```

## Useful Links

[Natural Language Processing - Dan Jurafsky, Christopher Manning](https://www.coursera.org/course/nlp)

## Usage


```bash
Search query >>  drone
Score: filename
1.0: parrot_AR_drone.txt
1.0: mq-9_reaper.txt
```

## Data

- Robot Toy Dataset [(excerpts copied from Wikipedia)](https://en.wikipedia.org/wiki/Robot)

## Acknowledgement

While writing this code I took help from [Michael Nielsen's code](https://github.com/mnielsen/VSM)
