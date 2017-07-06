from django.shortcuts import render, redirect
from profileapp.models import Profile
from django.views.generic import TemplateView
from profileapp.forms import UserEditProfile


class ProfileView(TemplateView):
    template_name = "profile.html"

    def profiles(self):
        return Profile.objects.all()


def edit_profile(request):
    user = Profile.objects.get(id=request.user.id)

    if request.method == "POST":
        form = UserEditProfile(request.POST, instance=user)

        # if form.is_valid():
        #     profile = form.save(commit=False)
        #     profile.ip_address = request.META['REMOTE_ADDR']
        #     profile.user = request.user
        #     profile.save()
        #     return redirect('profile')

        if form.is_valid():
            form.save(commit=False)
            return redirect('profile')
    else:
        form = UserEditProfile(instance=user)
        args = {'form': form}
        return render(request, 'edit.html', args)


def get_models(request):
    profile_list = list(Profile.objects.all())
    print(profile_list)
    return request