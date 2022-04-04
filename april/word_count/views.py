from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    sentence=str(request.POST.get("sentence"))
    sentence_to_list = sentence.split()

    dict={}
    
    for word in sentence_to_list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    word_count = list(dict.items())
    
    return render(request, "result.html", {'word_count': word_count})
