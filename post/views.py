from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from .models import Posteo
from .forms import PostForm
from django.template import loader


def index(request):
    latest_post_list = Posteo.objects.order_by('-pub_date')
    template = loader.get_template('post/index.html')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            n_message = form.cleaned_data['message']
            date = timezone.now()
            form = createMessage(n_message,date)
    else:
        form = PostForm()

    context = {
        'latest_question_list': latest_post_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))


def createMessage(message,date):
    new = Posteo(question_text=message, pub_date=date)
    new.save()
    return PostForm()
