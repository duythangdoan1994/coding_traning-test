from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm


def home(requests):
	if requests.method == "POST":
		print(requests.POST)
	title = "Welcome" 
	form = SignUpForm(requests.POST or None)
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		# form.save()
		print(requests.POST['email'])
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
	context = {
		"title": "Thanks you"
	}
	return render(requests, "home.html", context)