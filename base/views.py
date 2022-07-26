from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Medicine
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST' :
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'register.html', {'form':form})


class add_medicine(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['name','dosage', 'frequency']
class Add_receipt(LoginRequiredMixin, CreateView):
    model=Medicine
    template_name='add_medicine.html'
    form_class = add_medicine
    def get_success_url(self):
        return reverse('account', kwargs={'username':self.request.user.username})
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class Account(LoginRequiredMixin,DetailView):
    model=Medicine
    template_name='account.html'
    context_object_name='medicines'
    def get_object(self, **kwargs):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Medicine.objects.filter(user=self.request.user)

class Update(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model=Medicine
    template_name='add_medicine.html'
    fields=['name','dosage','frequency']
    def get_success_url(self):
        return reverse('account', kwargs={'username':self.request.user.username})
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
class Delete(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model=Medicine
    template_name='delete.html'
    def get_success_url(self):
        return reverse('account', kwargs={'username':self.request.user.username})

class MyLoginView(LoginView):
    def get_success_url(self):
        return reverse('account', kwargs={'username':self.request.user.username})

