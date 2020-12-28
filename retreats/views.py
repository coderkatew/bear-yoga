from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Retreat
from retreats.forms import RetreatForm


def retreats(request):
    """ A view to show upcoming retreats """
    retreats = Retreat.objects.all()
    context = {
        'retreats': retreats,
    }
    return render(request, 'retreats/retreats.html', context)


@login_required
def add_retreat(request):
    """ Add retreat to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can complete this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RetreatForm(request.POST, request.FILES)
        if form.is_valid():
            retreat = form.save()
            messages.info(request, 'Entry added!')
            return redirect(reverse('retreat_detail', args=[retreat.id]))
        else:
            messages.error(request, 'Cannot add this entry. Please ensure the form is valid.')
    else:
        form = RetreatForm()

    template = 'retreats/add_retreat.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_retreat(request, retreat_id):
    """ Edit existing retreat entry  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can complete this action.')
        return redirect(reverse('home'))

    retreat = get_object_or_404(Retreat, pk=retreat_id)
    if request.method == 'POST':
        form = RetreatForm(request.POST, request.FILES, instance=retreat)
        if form.is_valid():
            form.save()
            messages.info(request, 'Entry updated!')
            return redirect(reverse('retreat_detail', args=[retreat.id]))
        else:
            messages.error(request, 'Cannot update this entry. Please ensure form is complete.')
    else:
        form = RetreatForm(instance=retreat)
        messages.info(request, f'You are editing {retreat.name}')

    template = 'retreats/edit_retreat.html'
    context = {
        'form': form,
        'retreat': retreat,
    }

    return render(request, template, context)


def retreat_detail(request, retreat_id):
    """ A view to show the retreat detail page """

    retreat = get_object_or_404(Retreat, pk=retreat_id)

    context = {
        'retreat': retreat,
    }

    return render(request, 'retreats/retreat_detail.html', context)


@login_required
def delete_retreat(request, retreat_id):
    """ Delete a retreat entry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can complete this action.')
        return redirect(reverse('home'))
        
    retreat = get_object_or_404(Retreat, pk=retreat_id)
    retreat.delete()
    messages.info(request, 'Entry deleted!')
    return redirect(reverse('retreats'))