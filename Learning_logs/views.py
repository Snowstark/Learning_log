from django.shortcuts import render

from .models import Topic


def index(request):
    """Page of Learning_log"""
    return render(request, 'Learning_logs/index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'Learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show special topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'Learning_logs/topic.html', context)

