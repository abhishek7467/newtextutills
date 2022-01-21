from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox value
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charactercount = request.GET.get('charactercount', 'off')

    removepunc = request.GET.get('removepunc', 'off')

    if removepunc == "on":
        punctuations = '''!@#$%^&*()-_{}[]:;"'\|<>,.?/~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyze_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyze_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = " "
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remove', 'analyze_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space  Remove', 'analyze_text': analyzed}
        djtext = analyzed

    if (charactercount == "on"):
        analyzed = djtext
        analyzed = len(analyzed)
        params = {'purpose': 'Number Of Character is :',
                  'analyze_text': analyzed}

    if (
            removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercount != "on"):
        return HttpResponse("Error..........")
    return render(request, 'analyze.html', params)

# aktextutil.epizy.com