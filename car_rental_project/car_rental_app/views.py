from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm  # Assuming you have created a SignupForm in forms.py

def index_view(request):
    # Your logic for the homepage view goes here
    return render(request, 'index.html') 


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            messages.success(request, 'Registered successfully!')  # Display success message
            return redirect('success_page')  # Redirect to a success page or any other URL
        else:
            messages.error(request, 'Form submission failed. Please check the data.')  # Display error message
    else:
        form = SignupForm()
    
    return render(request, 'signup_modal.html', {'form': form})
