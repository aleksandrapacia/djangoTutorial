from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """Main page for app Learning Logs"""
    return render(request, 'learning_logs/index.html')

def topics(request, topic_id):
    topic = Topic.objects.order_by(id=topic_id)
    entries = topic.entry_set.order_by('=date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)
