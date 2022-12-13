# Exploring Internal Linguistic Representations of a Multilingual BERT Model

This repository examines how languages are categorized in an BERT multilingual model and compares them to a human understanding of language proximity and classification. The code is simple and leverages the use of a pretrained model, 'bert-base-multilingual-cased'. A simple similaririty metric, Cosine distance, is used to determine if the model's internal word-level representation is able to identify syntactic and semantic similarities among languages and whether there is an affinity for script instead.

The following languages are of particular interest:

1) Japanese, Korean, and Chinese: Japanese and Korean are more similair syntantically compared to Chinese, however, in terms of script, Japanese and Chinese are more similair.

2) Arabic, Urdu, Hindi: Urdu and Hindi are mutually intelligeble. Urdu, however, is written using an Arabic derived script and has a higher influence from Arabic, while Hindi is written using the Devanagari script.

3) Indo-European languages, specifically English, French, and German. Both English and German have a Germanic root and French is a Romance language. They all share a Roman script.

Example 1)

words = [
             "Happiness",
             "幸せ" #Japanese,
             "幸福" #Chinese,
             "행복" #Korean,
             "Glück" #German,
             "Bonheur #French
]


![image](https://user-images.githubusercontent.com/118930981/207137500-527d900e-74a8-4d3d-8c6e-bad17de16d12.png)

This example shows that the internal representation may have a preference for script. English and French are shown as more similair, instead of German, which has an accented letter in this example that is not found in English. Also, the Chinese and Japanese words, both of which share one character, have the highest similarity at .89.

Example 2)

words = [
             "نام" #Urdu,
             "नाम" #Hindi,
             "اسم" #Arabic
]

![image](https://user-images.githubusercontent.com/118930981/207137082-49621465-0bf6-4bb8-bbd2-a39d7d33df7d.png)

The words in Urdu and Hindi for name are the same. This example contradicts the observation from the first one, in that the Hindi word is showing higher similarity with Arabic, although Urdu and Arabic share the same script.


Given the above two examples, the categorization of language at the word-level in this BERT multilingual model seem to not be consistent with human categorization of language.
