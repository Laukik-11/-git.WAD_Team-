from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Announcement
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http.response import HttpResponse

# Create your views here.

# View to create an announcement


class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    fields = ["title", "body"]
    template_name = "announcements_form.html"
    success_url = reverse_lazy("announcements_list")

    # To test if the user is an admin
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponse("You have been denied")

    # To assign the requesting user as the creator the Announcement
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AnnouncementCreateView, self).form_valid(form)


# View to list all the assignments
class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = "announcements_list.html"
    paginate_by = 4
