from django.shortcuts import render

def index(request):
	context = {
		'title':'Django Project mywebsite2',
		'heading':'Website ini dibuat Menggunakan Bootstrap, JS',
		'subheading':'Gilbran',
	}
	return render(request, 'index.html', context)