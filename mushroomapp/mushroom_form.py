from django import forms
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from mushroomapp.preprocess_data import PreprocessData
from mushroomapp.request_prediction import RequestPrediction


class MushroomForm(forms.Form):
    capshape = forms.ChoiceField(label='Cap Shape', choices=[('b', 'bell'),
                                                             ('c', 'conical'),
                                                             ('x',  'convex'), ('f',
                                                                                'flat'),
                                                             ('k', 'knobbed'), ('s', 'sunken')])
    capsurface = forms.ChoiceField(label='Cap Surface', choices=[('f', 'fibrous'), ('g', 'grooves'),
                                                                 ('y', 'scaly'), ('s', 'smooth')])
    capcolor = forms.ChoiceField(label='Cap Color', choices=[('n', 'brown'), ('b', 'buff'),
                                                             ('c', 'cinnamon'), ('g',
                                                                                 'gray'), ('r', 'green'),
                                                             ('p', 'pink'), ('u',
                                                                             'purple'),
                                                             ('e', 'red'), ('w', 'white'), ('y', 'yellow')])
    bruises = forms.ChoiceField(label='Bruises', choices=[
                                ('t', 'yes'), ('f', 'no')])
    odor = forms.ChoiceField(label='Odor', choices=[('a', 'almond'), ('l', 'anise'), ('c', 'creosote'), (
        'y', 'fishy'), ('f', 'foul'), ('m', 'musty'), ('n', 'none'), ('p', 'pungent'), ('s', 'spicy')])
    gillattachment = forms.ChoiceField(label='Gill Attachment', choices=[(
        'a', 'attached'), ('d', 'descending'), ('f', 'free'), ('n', 'notched')])
    gillspacing = forms.ChoiceField(label='Gill Spacing', choices=[(
        'c', 'close'), ('w', 'crowded'), ('d', 'distant')])
    gillsize = forms.ChoiceField(label='Gill Size', choices=[(
        'b', 'broad'), ('n', 'narrow')])

    gillcolor = forms.ChoiceField(label='Gill Color', choices=[('k', 'black'), ('n', 'brown'), ('b', 'buff'),
                                                               ('h', 'chocolate'), ('g', 'gray'), ('r', 'green'), (
                                                                   'o', 'orange'), ('p', 'pink'), ('u', 'purple'), ('e', 'red'),
                                                               ('w', 'white'), ('y', 'yellow')])
    stalkshape = forms.ChoiceField(label='Stalk Shape', choices=[
                                   ('e', 'enlarging'), ('t', 'tapering')])
    stalkroot = forms.ChoiceField(label='Stalk Root', choices=[('b', 'bulbous'), ('c', 'club'), ('u', 'cup'),
                                                               ('e', 'equal'), ('z', 'rhizomorphs'), ('r', 'rooted'), ('?', 'missing')])
    stalksurfaceabovering = forms.ChoiceField(label='Stalk Surface Above Ring', choices=[('f', 'fibrous'),
                                                                                         ('y', 'scaly'), ('k', 'silky'), ('s', 'smooth')])
    stalksurfacebelowring = forms.ChoiceField(label='Stalk Surface Below Ring', choices=[('f', 'fibrous'),
                                                                                         ('y', 'scaly'), ('k', 'silky'), ('s', 'smooth')])

    stalkcolorabovering = forms.ChoiceField(label='Stalk Color Above Ring', choices=[('n', 'brown'), ('b', 'buff'),
                                                                                     ('c', 'cinnamon'), ('g', 'gray'), ('o', 'orange'), ('p', 'pink'), ('e', 'red'), ('w', 'white'), ('y', 'yellow')])
    stalkcolorbelowring = forms.ChoiceField(label='Stalk Color Below Ring', choices=[('n', 'brown'), ('b', 'buff'),
                                                                                     ('c', 'cinnamon'), ('g', 'gray'), ('o', 'orange'), ('p', 'pink'), ('e', 'red'), ('w', 'white'), ('y', 'yellow')])
    veiltype = forms.ChoiceField(label='Veil Type', choices=[(
        'p', 'partial'), ('u', 'universal')])
    veilcolor = forms.ChoiceField(label='Veil Color', choices=[(
        'n', 'brown'), ('o', 'orange'), ('w', 'white'), ('y', 'yellow')])
    ringnumber = forms.ChoiceField(label='Ring Number', choices=[
                                   ('n', 'none'), ('o', 'one'), ('t', 'two')])
    ringtype = forms.ChoiceField(label='Ring Type', choices=[('c', 'cobwebby'), ('e', 'evanescent'), ('f', 'flaring'),
                                                             ('l', 'large'), ('n', 'none'), ('p', 'pendant'), ('s', 'sheathing'), ('z', 'zone')])
    sporeprintcolor = forms.ChoiceField(label='Spore Print Color', choices=[('k', 'black'), ('n', 'brown'),
                                                                            ('b', 'buff'), ('h', 'chocolate'), ('r', 'green'), ('o', 'orange'), ('u', 'purple'), ('w', 'white'), ('y', 'yellow')])
    population = forms.ChoiceField(label='Population', choices=[('a', 'abundant'), (
        'c', 'clustered'), ('n', 'numerous'), ('s', 'scattered'), ('v', 'several'), ('y', 'solitary')])
    habitat = forms.ChoiceField(label='Habitat', choices=[(
        'g', 'grasses'), ('l', 'leaves'), ('m', 'meadows'), ('p', 'paths'), ('u', 'urban'), ('w', 'waste'), ('d', 'woods')])


def form(request):
    submitted = False
    if request.method == 'POST':
        form = MushroomForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            preprocess = PreprocessData(cd)
            preprocessed_values = preprocess.create_preprocessed_values()
            req = RequestPrediction(preprocessed_values)
            prediction = req.submit_dataframe()

            messages.add_message(request, messages.INFO, str(prediction))
            return HttpResponseRedirect('/form?submitted=True')

    else:
        form = MushroomForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'form/form.html', {'form': form, 'submitted': submitted})
