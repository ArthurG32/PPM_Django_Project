from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView
from website_PPM.models import Profile, Post
from django.contrib import messages
from members.forms import SignUpForm, UserEditForm, ChangePasswordForm, EditProfileInfoForm


class EditProfileInfoView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_info.html'
    form_class = EditProfileInfoForm
    #success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Profile info updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('show_profile', kwargs={'pk': self.kwargs['pk']})


class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    context_object_name = 'page_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_user = self.get_object()
        user = page_user.user
        context['user_posts'] = Post.objects.filter(author=user).order_by('-post_date')
        return context


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Save the user object
        user = form.save()

        # Create a profile for the user
        profile, created = Profile.objects.get_or_create(user=user)

        # Save the profile photo if provided
        photo = form.cleaned_data.get('photo')
        if photo:
            profile.photo = photo
            profile.save()

        # Save the profile description if provided
        description = form.cleaned_data.get('description')
        if description:
            profile.description = description
            profile.save()

        return super().form_valid(form)

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page if the user is not authenticated
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Credentials updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    #success_url = reverse_lazy('change_password')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Password changed successfully.')
        return redirect('home')