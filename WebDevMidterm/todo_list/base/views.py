from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.db import transaction

from .models import Task
from .forms import TaskForm
from .forms import PositionForm

class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('tasks')


class RegisterPage(FormView):
  template_name = 'base/register.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super(RegisterPage, self).form_valid(form)

  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('tasks')
    return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
  model = Task
  context_object_name = 'tasks'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_tasks = context['tasks'].filter(user=self.request.user)

    search_input = self.request.GET.get('search-area') or ''
    if search_input:
      user_tasks = user_tasks.filter(title__icontains=search_input)

    category_filter = self.request.GET.get('category') or ''
    if category_filter:
      user_tasks = user_tasks.filter(category=category_filter)

    sort_by = self.request.GET.get('sort_by') or 'created'
    if sort_by in ['created', 'deadline', 'title']:
      user_tasks = user_tasks.order_by(sort_by)

    context['tasks'] = user_tasks
    context['count'] = user_tasks.filter(complete=False).count()
    context['search_input'] = search_input
    context['category_filter'] = category_filter
    context['sort_by'] = sort_by
    context['categories'] = [choice[0] for choice in Task.CATEGORY_CHOICES]

    return context


class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  form_class = TaskForm
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  form_class = TaskForm
  success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')

  def get_queryset(self):
    owner = self.request.user
    return self.model.objects.filter(user=owner)


class TaskReorder(View):
  def post(self, request):
    form = PositionForm(request.POST)

    if form.is_valid():
      positionList = form.cleaned_data["position"].split(',')

      with transaction.atomic():
        self.request.user.set_task_order(positionList)

    return redirect(reverse_lazy('tasks'))