from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from mushroomapp.preprocess_data import PreprocessData

class Form(forms.Form):
    capshape = forms.ChoiceField(label='Cap Shape', choices=[('b', 'bell'), 
                                ('c','conical'), ('x','convex'), ('f', 'flat'),
                                ('k', 'knobbed'), ('s', 'sunken')])

def form(request):
    submitted = False
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd)
            preprocess = PreprocessData(cd)
            preprocess.myfunc()
      
            # assert False
            return HttpResponseRedirect('/form?submitted=True')
    else:
        form = Form()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'form/form.html', {'form': form, 'submitted': submitted})