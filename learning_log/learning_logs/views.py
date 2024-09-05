from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Main page for app Learning Logs"""
    return render(request, 'learning_logs/index.html')

# A view of topics 
def topics(request):
    # here we store a set retrieved and store as topics
    topics = Topic.objects.order_by('data_added')
    # this is a context which later on will be sent to a template 
    # the context is basically a dictionary containing keys (names used in template to retrieve the data)
    # and values (are the data which is sent to a template)
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)