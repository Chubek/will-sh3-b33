# Will I Find Love, Master?
This repository contains code that trains four deep and shallow models and backend to serve them. The code for the training is found in the notebook inside the notebook folder.

I used [data from OkCupid](https://www.kaggle.com/andrewmvd/okcupid-profiles) to train four models where the target is "status" column of the data. Status being single, married, in relationship, etc. 

## Shallow Models

There are two shallow models in this model. One's a gradient boost using XGBoost, and one's an OVR SVM using Libsvm through Sklearn. 

## Deep Models

There's a simple feed-forward model that takes the same input features as the shallow models. This model had a high accuracy, and was constructed using Keras. 

## Preprocessors

There's an overall of 15 preprocessors. You can find a list of them in the `.env` file that I have linked below.

## Essay Classifier

I have fine-tuned BERT on the 9 essays of this dataset. All 9 essays at once. But the latent space is a free-for-all, just write everything you feel like that represents you!

## Tokenizer

It's the BERT tokenizer that comes  with the `transformers` library.

# Where do I download the models?

I haven't included the models in this repositry because it's a bad practice to do so. You can download my `.env` file from here, and put it in the root folder. Then you can launch `app.py`, and use Postman to send requests. 

Link:
```
https://cdn.discordapp.com/attachments/797919965264085092/887168285982982144/env
```

**NOTE:** Add a period to the beginning of the file name, i.e. make it `.env`.

The frontend is coming soon!