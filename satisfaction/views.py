from django.shortcuts import render, redirect
from .models import Visite
from .forms import AvisForm
from django.views.decorators.csrf import  csrf_protect
from .utils import getTicketDetails


def can_feedback(code):
    if Visite.objects.filter(code=code).exists():
        return False, 'Code déjà scanné ⚠️'
    result = getTicketDetails(code)
    if not result:
        return False, 'Code incorrecte ⚠️'
    return True, result[0]

@csrf_protect
def page_emojis(request):
    form = AvisForm()
    if request.method == 'POST':
        success, message = can_feedback(request.POST['code'])
        if not success:
            return render(request, 'fail.html', {'error': message})
        form = AvisForm(request.POST)
        if form.is_valid():
            visite = Visite.objects.create(code = message[0], ref_pat = message[1], specialite = message[2], service = message[3])
            avis = form.save()
            avis.visite = visite
            avis.save()
            return render(request, 'success.html', {'message': message[1]})
    return render(request, 'avis_form.html', {'form': form })

@csrf_protect
def page_merci(request):
    return render(request, 'success.html')

@csrf_protect
def page_scanned(request):
    return render(request, 'fail.html')

@csrf_protect
def page_scan(request):
    if request.method == 'POST':
        success, message = can_feedback(request.POST['code'])
        if not success:
            return render(request, 'fail.html', {'error': message})
        else:
            return redirect('avis_form', code=request.POST['code'])
    return render(request, 'scan.html')