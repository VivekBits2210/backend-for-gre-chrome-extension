from django.http import JsonResponse
import pickle
import random

words = pickle.load(open("./gre_chrome/all_words_with_freq_and_meaning.pkl", "rb"))


def index(request):
    return JsonResponse(
        {"message": f"Welcome to gre_chrome backend"},
    )


def fetch_word(request):
    datapoint = random.choice(words)
    datapoint["word"] = datapoint["word"].capitalize()
    return JsonResponse(datapoint)
