from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from building.models import Build
from .models import Testimonials, Agents, Agency
from .forms import UserLoginForm
from travelling.models import Travel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class LandingPageView(View):
    def get(self, request):
        buildings = Build.objects.all()
        travels = Travel.objects.all()
        users = User.objects.all()
        agents = Agents.objects.all()
        testimonials = Testimonials.objects.all()
        context = {
            'testimonials': testimonials,
            'buildings': buildings,
            "users": users,
            'travels': travels,
            'agents': agents,

        }

        return render(request, 'main/index.html', context)


class ContactListView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class BlogListView(View):
    def get(self, request):
        return render(request, 'main/blog-grid.html')


class AboutListView(View):
    def get(self, request):
        agents = Agents.objects.all()
        context = {
            'agents': agents
        }
        return render(request, 'main/about.html', context)


class TestimonialView(View):
    def get(self, request):
        testimonials = Testimonials.objects.all()
        context = {
            'testimonials': testimonials
        }
        return render(request, 'main/testimonial.html', context)


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            # Add error handling here for password mismatch
            return render(request, 'auth/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            # Add error handling here for existing user
            return render(request, 'auth/register.html', {'error': 'Username already exists'})

        user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        user.set_password(password_1)
        user.save()
        return redirect('login')


class UserLoginView(View):
    def get(self, request):
        forms = AuthenticationForm()
        return render(request, 'auth/login.html', {'form': forms})

    def post(self, request):
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request, user)
            return redirect('landing')

        return render(request, 'auth/login.html', {'forms': forms})


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("register")


class AgentListView(View):
    def get(self, request):
        search = request.GET.get("search")
        agents = Agents.objects.all()

        if search:
            agents = agents.filter(name__icontains=search)

        context = {
            "agents": agents,
            'search': search,
        }
        return render(request, "main/agents-grid.html", context)

    def post(self, request):
        search = request.POST.get("search")
        agents = Agents.objects.all()

        if search:
            agents = agents.filter(name__icontains=search)

        context = {
            "agents": agents,
            'search': search,
        }
        return render(request, "main/agents-grid.html", context)


class AgentUpdateView(View):
    def get(self, request, id):
        agent = get_object_or_404(Agents, id=id)
        context = {'agent': agent}
        return render(request, 'agent-update.html', context)

    def post(self, request, id):
        agent = get_object_or_404(Agents, id=id)
        agent.first_name = request.POST.get('first_name')
        agent.last_name = request.POST.get('last_name')
        agent.image = request.POST.get('image')
        agent.email = request.POST.get('email')
        agent.phone_number = request.POST.get('phone_number')
        agent.save()
        return redirect('agent-update', id=agent.id)

class AgentDeleteView(View):
    def get(self, request, id):
        agent = Agents.objects.get(id=id)
        agent.delete()
        return redirect('agent-update')


class AgentDetailView(View):
    def get(self, request, id):
        agent = Agents.objects.get(id=id)
        context = {
            'agent': agent
        }
        return render(request, 'main/agent-single.html', context)
