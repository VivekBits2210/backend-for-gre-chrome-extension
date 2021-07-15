from django.http import JsonResponse
import pickle
import random

words = pickle.load(open("./gre_chrome/difficulty_to_words_map.pkl", "rb"))


def index(request):
    return JsonResponse(
        {"message": f"Welcome to gre_chrome backend"},
    )


def fetch_word(request):
    difficulty = request.GET.get("difficulty")
    if difficulty is None:
        difficulty = "1"
    datapoint = random.choice(words[difficulty])
    return JsonResponse(datapoint)
