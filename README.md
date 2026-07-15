# Public Opinion Analysis Based on Sina Weibo

An end-to-end Chinese natural language processing project for collecting,
classifying, and analyzing public opinion from Sina Weibo hot-search topics
and user comments.

The project combines public-data collection, Chinese text preprocessing,
deep-learning-based topic classification, few-shot labeling, seven-class
emotion recognition, and result visualization.

> This project was originally developed as an academic NLP study and has been
> reorganized for portfolio presentation.

---

## Project Overview

Social media platforms contain large volumes of short, informal, and rapidly
changing text. Analyzing this content requires handling dynamic web pages,
informal Chinese expressions, emojis, topic-specific vocabulary, and limited
labeled data.

This project develops a Sina Weibo public-opinion analysis pipeline that:

1. Collects public hot-search topics and related comments
2. Cleans and preprocesses Chinese social-media text
3. Classifies hot-search topics into predefined news categories
4. Compares multiple neural text-classification architectures
5. Uses few-shot prompting to support dataset labeling
6. Performs seven-class emotion recognition on Weibo comments
7. Visualizes topic and sentiment distributions

---

## System Workflow

```text
Sina Weibo hot-search data
            ↓
API and web-based data collection
            ↓
Comment extraction and periodic storage
            ↓
Chinese text cleaning and tokenization
            ↓
Topic classification and clustering
            ↓
Few-shot label generation
            ↓
Seven-class emotion recognition
            ↓
Public-opinion analysis and visualization
```

---

## Main Components

### 1. Hot-Search Data Collection

The project retrieves public Sina Weibo hot-search topics through an API-based
workflow.

The data-processing pipeline:

- Requests current hot-search information
- Parses the returned JSON data
- Extracts topic titles and timestamps
- Appends new records to a Pandas DataFrame
- Periodically stores collected results in CSV format

The original implementation was designed to update the hot-search dataset
approximately once per hour.

---

### 2. Comment Collection

Two approaches were explored for collecting comments associated with trending
topics.

#### HTTP and HTML Parsing

Requests and BeautifulSoup were used to retrieve and parse publicly accessible
page content.

#### Selenium-Based Collection

Selenium WebDriver was used for dynamic pages requiring browser interaction,
scrolling, and delayed content loading.

The combined workflow first collects hot-search topics, generates corresponding
topic links, and then retrieves associated comments for further analysis.

> The data-collection code is historical and may require updates because
> website structures and access policies can change.

---

### 3. Chinese Text Preprocessing

The preprocessing pipeline includes:

- Chinese tokenization using Jieba
- Stop-word removal
- Newline and irrelevant-character removal
- Emoji normalization
- Duplicate and empty-text filtering
- Numerical encoding of class labels
- Train/test splitting at an 80:20 ratio

For neural text-classification experiments:

- Vocabulary size was limited to 10,000 tokens
- Text was converted into integer sequences
- Sequences were padded to a maximum length of 200

---

## Topic Classification

The project compares several neural architectures for Chinese text
classification:

- Multilayer Perceptron
- Convolutional Neural Network
- Recurrent Neural Network
- Long Short-Term Memory
- Gated Recurrent Unit
- CNN + LSTM
- Bidirectional LSTM
- TextCNN
- Attention
- Multi-Head Attention
- Attention + BiLSTM
- BiGRU + Attention
- Transformer

All models were trained using cross-entropy loss and the Adam optimizer.
Early stopping was applied to reduce overfitting.

Evaluation included:

- Accuracy
- Precision
- Recall
- F1 score
- Confusion matrix
- Cohen's Kappa
- Training and validation curves

### Model Comparison

The evaluated architectures produced classification accuracies ranging from
approximately 0.88 to 0.96 in the reported experiment.

The custom Transformer model achieved:

| Metric | Result |
|---|---:|
| Accuracy | 0.9543 |
| Precision | 0.9542 |
| Recall | 0.9543 |
| F1 score | 0.9542 |

Although several models achieved similar numerical performance, the Transformer
architecture was selected for hot-search classification because of its ability
to model contextual relationships in short Chinese text.

---

## Clustering Analysis

K-means clustering was initially evaluated for grouping hot-search topics.

The experiment showed that conventional K-means was not well suited to this
task because:

- Short Chinese texts produce sparse lexical features
- Hot-search entries are semantically condensed
- Synonyms and context-dependent meanings are difficult to capture
- Distance-based clustering may not reflect semantic similarity

This result motivated the use of supervised and Transformer-based
classification methods instead of relying only on conventional clustering.

---

## Few-Shot Labeling

A few-shot text-labeling workflow was developed using GPT-3.5.

The prompt contained:

- A fixed set of topic categories
- Task instructions
- Several labeled examples
- New unlabeled hot-search headlines

Example categories included:

- Entertainment
- Finance
- Education
- Technology
- Society
- Sports
- Culture

The generated labels were post-processed and compared with manually reviewed
results.

The experiment showed that few-shot labeling could efficiently support dataset
construction, but label quality was highly dependent on prompt clarity and
example selection.

---

## Seven-Class Emotion Recognition

Sentiment and emotion analysis was performed using PaddleHub's ERNIE Tiny model
and the OCEMOTION Chinese emotion dataset.

The model was configured for seven-class text classification.

### Training Configuration

| Parameter | Value |
|---|---:|
| Model | ERNIE Tiny |
| Maximum sequence length | 128 |
| Optimizer | AdamW |
| Learning rate | 2e-5 |
| Epochs | 4 |
| Batch size | 16 |

### Reported Performance

| Metric | Result |
|---|---:|
| Test accuracy | 0.5939 |
| Precision | 0.5150 |
| Recall | 0.4775 |
| F1 score | 0.4906 |

The results indicate moderate emotion-classification performance. The experiment
also highlights the difficulty of transferring a general Chinese emotion model
to short, informal, and topic-dependent Weibo comments.

---

## Example Public-Opinion Analysis

The trained emotion model was applied to comments associated with a selected
Weibo trending topic.

The reported emotion distribution was:

| Emotion | Number of comments |
|---|---:|
| Sadness | 99 |
| Anger | 85 |
| Like | 70 |
| Happiness | 55 |
| Disgust | 13 |

Emoji cleaning was applied before classification to reduce noise in the textual
input.

This case study demonstrates how the pipeline can summarize the emotional
composition of online discussions while also revealing limitations related to
model generalization and domain-specific language.

---

## Repository Contents

```text
weibo-public-opinion-analysis/
├── README.md
├── OCEMOTION.csv
├── emoji2zh.json
├── nlp_weibo_part2_main.ipynb
├── sina_wibo_claw.py
├── tyc.txt
├── weibo_comments_claw.ipynb
├── weibo_hotsearch_link_claw.ipynb
├── weibo_nlp_comments_combined.xlsx
└── weibo_part1_train_model.ipynb
```

A future cleanup may reorganize the repository into:

```text
weibo-public-opinion-analysis/
├── README.md
├── requirements.txt
├── data/
├── notebooks/
├── src/
├── figures/
└── docs/
```

---

## Technologies

### Natural Language Processing

- Jieba
- Chinese text preprocessing
- Tokenization and sequence padding
- Topic classification
- Emotion recognition
- Few-shot labeling

### Machine Learning

- TensorFlow
- Keras
- PaddleHub
- ERNIE Tiny
- Transformer
- RNN
- LSTM
- GRU
- CNN
- Attention mechanisms
- K-means

### Data Collection and Analysis

- Python
- Requests
- BeautifulSoup
- Selenium
- Pandas
- NumPy
- Jupyter Notebook
- Matplotlib
- Scikit-learn

---

## Key Findings

- API-based retrieval and browser automation can be combined to collect
  dynamic public social-media data.
- Conventional K-means clustering performs poorly on sparse and semantically
  condensed Chinese hot-search text.
- Several neural classifiers achieved strong results on the original
  seven-category text-classification dataset.
- Transformer-based classification provided a practical balance between
  performance and contextual modeling.
- Few-shot labeling can accelerate dataset creation, but results depend heavily
  on prompt quality.
- ERNIE Tiny provided moderate seven-class emotion-recognition performance,
  indicating that domain adaptation remains necessary for informal Weibo text.

---

## Limitations

- Website structures and anti-automation mechanisms may change
- The historical crawler may no longer run without modification
- Hot-search titles are shorter than the news articles used for model training
- Dataset mismatch can reduce classification generalizability
- Emotion labels are subjective and context dependent
- The reported ERNIE Tiny results leave substantial room for improvement
- Public social-media samples may not represent the broader population
- Few-shot labels require manual review and validation

---

## Privacy and Responsible Use

This repository is intended only for academic and portfolio demonstration.

Before public release, datasets and notebooks should be checked for:

- Authentication cookies
- API credentials
- User identifiers
- Profile links
- Personal contact information
- Raw private or sensitive comments
- Local file paths

Only anonymized and publicly appropriate sample data should be included.

Users are responsible for complying with platform policies, privacy
requirements, and applicable laws.

---

## Future Work

Potential improvements include:

- Fine-tuning a Chinese pretrained language model directly on Weibo hot-search data
- Constructing a domain-specific hot-search classification dataset
- Improving class balance in the emotion dataset
- Adding stronger contextual and emoji representations
- Evaluating modern Chinese language models
- Introducing temporal trend analysis
- Building an interactive public-opinion visualization dashboard
- Adding topic evolution and event-detection components

---

## Author

**Ruixin Chen**

- [GitHub](https://github.com/MarcyChen-ruixin)
- [LinkedIn](https://www.linkedin.com/in/ruixinchen421/)
- [Google Scholar](https://scholar.google.com/citations?user=hcnreTAAAAAJ&hl=en)

---

## Use

This repository is provided as an academic and portfolio demonstration.

No license for reuse or redistribution is granted unless explicitly stated.
