from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic

from committee.models import Committee
from events.form import EventForm, PostForm
from events.models import Event, Post


@login_required
def createEvent(request, pk):
    committee = get_object_or_404(Committee, pk=pk)
    print('committee is', committee)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            committeeEvent = form.save(commit=False)
            committeeEvent.committeeEvent = committee
            committeeEvent.author = request.user
            committeeEvent.save()
            return redirect('event_detail', committeeEvent.pk)
    else:
        form = EventForm()
    return render(request, 'event/new_event.html', {
        'form': form
    })


class EventDetailView(generic.DetailView):
    template_name = 'event/event_detail.html'
    model = Event

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print('post', self.kwargs['pk'])
        post = Post.objects.filter(event_id=self.kwargs['pk'])
        print('all', post)
        context['post_list'] = Post.objects.filter(event_id=self.kwargs['pk'])
        return context


class EventListView(generic.ListView):
    template_name = 'event/event_list.html'
    model = Event


@login_required
def creatPost(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            eventPost = form.save(commit=False)
            eventPost.event = event
            eventPost.author = request.user
            eventPost.save()
            return redirect('event_detail', eventPost.pk)
    else:
        form = PostForm()
        return render(request, 'event/new_post.html', {
            'form': form})
