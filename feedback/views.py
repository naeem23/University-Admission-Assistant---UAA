from django.shortcuts import render, redirect
from .forms import FeedbackForm


# ------------------------------------
# ----------- FeedbackForm -----------
# ------------------------------------
def sendFeedback(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = FeedbackForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.save()
				return redirect('home:homepage')

		else:
			form = FeedbackForm()

		context ={
			'form': form,
		}
		return render(request, 'feedback/send_feedback.html', context)
