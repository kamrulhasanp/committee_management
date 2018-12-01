from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView, CreateView

from committee.forms import LeaderForm, MemberForm, CommitteeForm, SliderForm
from committee.models import Committee, Leader, Member, SlideView
from events.models import Event


class CommitteeListView(ListView):
    model = Committee
    template_name = 'committee/committee_list.html'


class CommitteeDetailView(generic.DetailView):
    template_name = 'committee/committee_detail.html'
    model = Committee

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print('event', self.kwargs['pk'])
        print('slider', self.kwargs['pk'])
        slide = SlideView.objects.filter(committee_id=self.kwargs['pk'])
        events = Event.objects.filter(committeeEvent_id=self.kwargs['pk'])
        print('all', events)
        print('all', slide)
        context['event_list'] = Event.objects.filter(committeeEvent_id=self.kwargs['pk'])
        context['slider'] = SlideView.objects.filter(committee_id=self.kwargs['pk'])
        return context


class CommitteeCreateView(CreateView, LoginRequiredMixin):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    form_class = CommitteeForm
    model = Committee
    template_name = 'committee/new_committee.html'

    # fields = ('name', 'descriptions', 'leaderNumber', 'memberNumber',)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('select_leader', args={self.object.pk})

    # def select_leader(request):
    #     heading_message = 'Select leaders'
    #     if request.method == 'GET':
    #         formset = LeaderFormset(request.GET or None)
    #     elif request.method == 'POST':
    #         formset = LeaderFormset(request.POST)
    #         if formset.is_valid():
    #             for form in formset:
    #                 name = form.cleaned_data.get('teacher')
    #                 if name:
    #                     Leader(teacher=name).save()
    #             return redirect('select_member')
    #     return render(request, 'committee/select_leaders.html', {
    #         'formset': formset,
    #         'heading': heading_message,
    #     })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def select_leader(request, pk):
    committe = Committee.objects.get(pk=pk)
    leader = Leader.objects.filter(committee=committe)
    print(leader)
    lenLeader = (len(leader))
    leader_number = committe.leaderNumber
    print(leader_number)
    if request.method == 'POST':
        leader_form = LeaderForm(request.POST)

        if leader_form.is_valid():
            leader_form.save(commit=False)
            teacher = leader_form.cleaned_data['teacher']
            print(teacher)
            # if teacher in leader:
            #     messages.warning(request, 'This leader is already save')
            # else:
            if len(leader) < leader_number:
                leader_form.committee = committe
                leader_form.save()

            else:
                messages.warning(request, 'You can\'t add more leader, please press Select member link')

        return redirect('select_leader', committe.pk)
    else:
        leader_form = LeaderForm()

    return render(request, 'committee/select_leaders.html',
                  {'leader_form': leader_form,
                   'committee': committe,
                   'lenLeader': lenLeader,
                   'leaderNumber': leader_number,
                   'leader': leader,
                   })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def select_member(request, pk):
    committee = Committee.objects.get(pk=pk)
    member = Member.objects.filter(committee=committee)
    leader = Leader.objects.filter(committee=committee)
    print(member)
    lenMember = (len(member))
    member_number = committee.memberNumber
    print(member_number)
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            member_form.save(commit=False)
            teacher = member_form.cleaned_data['teacher']
            print(teacher)
            # if teacher in leader:
            #     messages.warning(request, 'This leader is already save')
            # else:
            if len(member) < member_number:
                member_form.committee = committee
                member_form.save()
            else:
                messages.warning(request, 'You can\'t add more member, please press Finish link')
        return redirect('select_member', committee.pk)
    else:
        member_form = MemberForm()

    return render(request, 'committee/select_members.html',
                  {'member_form': member_form,
                   'committee': committee,
                   'lenMember': lenMember,
                   'memberNumber': member_number,
                   'member': member,
                   'leader': leader, })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def makeSliderView(request, pk):
    committee = get_object_or_404(Committee, pk=pk)
    slideimage = SlideView.objects.filter(committee=committee)
    print('committee is', committee)
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            committee = form.save(commit=False)

            if len(slideimage) < 2:
                """ committee.committee = committee.pk"""
            committee.save()
        else:
            messages.warning('You can\'t add more image')
        return redirect('addSlide ', committee.pk)
    else:
        form = SliderForm()

    return render(request, 'committee/new_slide.html',
                  {'committee': committee,
                   'form': form,
                   'slideimage': slideimage,
                   })
