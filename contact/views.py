from django.shortcuts import render

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
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
