from django.shortcuts import render
from .forms import ExampleForm  # make sure this line exists

def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
