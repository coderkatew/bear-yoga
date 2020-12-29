from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact_form(request):
    """ View contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Message sent!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Cannot add this entry. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def contact(request):
    """ Submit contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Thanks for getting in touch!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'There was an error submitting your message. Please ensure the form is complete.')

    return redirect(reverse('home'))
