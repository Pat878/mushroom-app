from django import forms
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from mushroomapp.preprocess_data import PreprocessData
from mushroomapp.request_prediction import RequestPrediction


class Form(forms.Form):
    capshape = forms.ChoiceField(label='Cap Shape', choices=[('b', 'bell'),
                                                             ('c', 'conical'), ('x',
                                                                                'convex'), ('f', 'flat'),
                                                             ('k', 'knobbed'), ('s', 'sunken')])


def form(request):
    submitted = False
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            preprocess = PreprocessData(cd)
            df = preprocess.create_preprocessed_dataframe()
            req = RequestPrediction(df)
            prediction = req.submit_dataframe()
            print(str(prediction) == "0.0")
            messages.add_message(request, messages.INFO, str(prediction))
            return HttpResponseRedirect('/form?submitted=True')

    else:
        form = Form()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'form/form.html', {'form': form, 'submitted': submitted})
