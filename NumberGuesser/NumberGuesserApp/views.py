import random
from django.shortcuts import render, redirect
from .forms import GuessForm

def guess_number(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)

    number = request.session['number']
    message = ''
    sound = 'default'

    if request.method == 'POST':
        if 'reset' in request.POST:
            request.session['number'] = random.randint(1, 100)
            return redirect('guess')
        
        form = GuessForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data['guess']
            if guess < number:
                if number - guess < 5:
                    message = "So close! A little more and you're there!"
                    sound = 'close'
                else:
                    message = "Hmm... Think bigger. Quite a bit bigger."
                    sound = 'low'
            elif guess > number:
                if guess - number < 5:
                    message = "Oh! Very near! Just a little less next time!"
                    sound = 'close'
                else:
                    message = "Too far up! Try dialing it down."
                    sound = 'high'
            else:
                message = "Ha! You got it right!"
                sound = 'success'
                request.session['number'] = random.randint(1, 100)
    else:
        form = GuessForm()

    return render(request, 'guess.html', {
        'form': form,
        'message': message,
        'sound': sound
    })
