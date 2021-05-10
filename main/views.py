from django.shortcuts import render, reverse, redirect
from django.conf import settings


from .mixins import (

	RedirectParams,
	APIMixin
)

'''
Basic view for selecting query
'''
def index(request):

	if request.method == "POST":
		cat = request.POST.get("cat", None)
		if cat:
			return RedirectParams(url = 'main:results', params = {"cat": cat})

	return render(request, 'main/index.html', {})



'''
Basic view for displaying results
'''
def results(request):

	cat = request.GET.get("cat", None)

	if cat:
		results = APIMixin(cat=cat).get_data()
		print (results)

		if results:
			context = {
				"results": results,
				"cat": cat,
			}

			return render(request, 'main/results.html', context)
	
	return redirect(reverse('main:home'))
