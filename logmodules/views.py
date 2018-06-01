from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

from .models import Log
from .forms import LogForm

from datetime import datetime

class IndexView(generic.ListView):
    context_object_name = 'list'
    model = Log
    template_name = 'logmodules/log_list.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        result = {}
        event_dates = Log.objects.values('event_date').order_by('event_date').distinct()
        dates_list = [log['event_date'].strftime('%Y-%m-%d') for log in event_dates]
        for date in dates_list:
            daily_events = []
            for evt in Log.objects.all().filter(event_date=date):
                evt.event_time = evt.event_time.strftime('%H:%M')
                daily_events.append(evt)
            result[date] = daily_events
        context['logs_map'] = result 
        return context

def log_list(request, pk):
    logs = Log.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'logmodules/log_list.html', {'logs':logs, 'dt': datetime.now()})


def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'lomodules/log_detail.html', {'log': logs})


class LogEntry(CreateView):
    model = Log
    fields = ['line',]

    def get_initial(self):
        initial = super(LogEntry, self).get_initial()
        return initial

    def form_valid(self, form):
        Log = form.save(commit=False)
        Log.username = self.request.user.username
        Log.save()
        return super(LogEntry, self).form_valid(form)

class LogUpdate(UpdateView):
    model = Log
    fields = ['line`']


class LogDelete(DeleteView):
    model = Log
    success_url = reverse_lazy('logmodules:list')
