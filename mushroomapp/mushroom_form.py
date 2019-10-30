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

# gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y
# stalk-shape: enlarging=e,tapering=t
# stalk-root: bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=?
# stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
# stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
# stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
# stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
    veiltype = forms.ChoiceField(label='Veil Type', choices=[(
        'p', 'partial'), ('u', 'universal')])
    veilcolor = forms.ChoiceField(label='Veil Color', choices=[(
        'n', 'brown'), ('o', 'orange'), ('w', 'white'), ('y', 'yellow')])
# ring-number: none=n,one=o,two=t
# ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z
# spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y
# population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y
    habitat = forms.ChoiceField(label='Habitat', choices=[(
        'g', 'grasses'), ('l', 'leaves'), ('m', 'meadows'), ('p', 'paths'), ('u', 'urban'), ('w', 'waste'), ('d', 'woods')])


def form(request):
    submitted = False
    if request.method == 'POST':
        form = MushroomForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            preprocess = PreprocessData(cd)
            df = preprocess.create_preprocessed_dataframe()
            req = RequestPrediction(df)
            prediction = req.submit_dataframe()

            messages.add_message(request, messages.INFO, str(prediction))
            return HttpResponseRedirect('/form?submitted=True')

    else:
        form = MushroomForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'form/form.html', {'form': form, 'submitted': submitted})
