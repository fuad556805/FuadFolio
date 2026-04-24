from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent — I'll reply soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
