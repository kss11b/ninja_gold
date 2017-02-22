from django.shortcuts import render, redirect
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'log' not in request.session:
        request.session['log']= []
    return render(request, 'main/index.html')
def calculation(request):
    if request.method == 'POST':

        if request.POST['action'] == 'farm':
            num = (random.randrange(10,20))
            request.session['gold']+= num
        if request.POST['action'] == 'cave':
            num = (random.randrange(5,10))
            request.session['gold']+= num
        if request.POST['action'] == 'house':
            num = (random.randrange(0,5))
            request.session['gold']+= num
        if request.POST['action'] == 'casino':
            num = (random.randrange(-50,50))
            request.session['gold']+= num
        if num < 0:
            state="lost"
        else:
            state="earned"
        string = "You {} {} gold from the {}".format(state, num, str(request.POST['action']))
        request.session['log'].append(string)
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
