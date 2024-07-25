---
title: FINETUNING LANGUAGE MODELS - CAN I PATENT THIS?
colorFrom: gray
colorTo: purple
sdk: streamlit
sdk_version: 1.21.0
app_file: app.py
pinned: false
---

# Finetuning Language Models- CAN I PATENT THIS?

************************

Milestone-3 notebook: https://github.com/srikanthnaidu1234/AI_project/blob/main/AI-project/src/AI_USPTO_milestone_3_Srikanth_Naidu.ipynb

Hugging Face App:
Patent Predictor APP: https://huggingface.co/spaces/srikanth0008/AI_Project_USPTO
Sentimental Analysis APP: https://huggingface.co/spaces/srikanth0008/Sentiment_Analysis_App


Landing Page for the App: https://sites.google.com/view/language-mode-patent-predictor/home

App Demonstration Video: https://github.com/srikanthnaidu1234/AI_project/blob/milestone-4/AI-project/src/Demo_USPTO_app.mp4

The tuned model shared to the Hugging Face Hub: https://huggingface.co/srikanth0008/tuned-for-patentability/tree/main

************************

## Summary

***********

**milestone1:** https://github.com/srikanthnaidu1234/AI_project/blob/main/AI-project/src/Milestone1_README.md

**milestone2:** https://github.com/srikanthnaidu1234/AI_project/blob/main/AI-project/src/Milestone2_README.md

**milestone3:** https://github.com/srikanthnaidu1234/AI_project/blob/main/AI-project/src/Milestone3_README.md

Dataset: https://github.com/suzgunmirac/hupd

**Data Preprocessing**

The load_dataset function to load all the patent applications that were filed to the USPTO in January 2016. We specify the date ranges of the training and validation sets as January 1-21, 2016 and January 22-31, 2016, respectively. This is a smaller dataset.AS mention in the [the Harvard USPTO patent dataset](https://github.com/suzgunmirac/hupd) paper.

 There are two datasets: train and validation. Here are the steps:

 - Label-to-index mapping for the decision status field
 - map the 'abstract' and 'claims' sections and tokenize them using pretrained('distilbert-base-uncased') tokenizer
 - format them
 - use DataLoader with batch_size = 16

**milestone3:**

The following notebook has the tuned model. There are 6 classes in the Harvard USPTO patent dataset and I decided to encode them as follow:

decision_to_str = {'REJECTED': 0, 'ACCEPTED': 1, 'PENDING': 1, 'CONT-REJECTED': 0, 'CONT-ACCEPTED': 1, 'CONT-PENDING': 1}

so that I can get a patentability score between 0 and 1.

The pertained-model 'distilbert-base-uncased' from the Hugging face hub and fine-tune it with the Harvard USPTO patent dataset


milestone3 notebook: https://github.com/srikanthnaidu1234/AI_project/blob/main/AI-project/src/AI_USPTO_milestone_3_Srikanth_Naidu.ipynb

The tuned model shared to the Hugging Face Hub: https://huggingface.co/srikanth0008/tuned-for-patentability/tree/main

**milestone4:**

Please see Milestone4 Documentation.md: https://github.com/srikanthnaidu1234/AI_project/blob/main/AI-project/README.md

Here is the landing page for my app: https://sites.google.com/view/language-mode-patent-predictor/home


                              **************

