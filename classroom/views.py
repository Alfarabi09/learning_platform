from django.shortcuts import render, redirect, get_object_or_404
from .models import Classroom, Assignment, CompletedAssignment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import AssignmentForm

@login_required
def dashboard(request):
    classrooms = request.user.classrooms.all()
    return render(request, 'classroom/dashboard.html', {'classrooms': classrooms})

@login_required
def classroom_detail(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    assignments = classroom.assignments.all()
    return render(request, 'classroom/classroom_detail.html', {'classroom': classroom, 'assignments': assignments})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    total_assignments = Assignment.objects.all().count()
    completed_assignments_count = request.user.completed_assignments.count()
    
    if total_assignments == 0:
        completion_percentage = 0
    else:
        completion_percentage = (completed_assignments_count / total_assignments) * 100

    context = {
        'total_assignments': total_assignments,
        'completed_assignments_count': completed_assignments_count,
        'completion_percentage': completion_percentage
    }
    
    return render(request, 'profile.html', context)

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()

    return render(request, 'assignment_form.html', {'form': form})

@login_required
def mark_assignment_completed(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.completed_by.add(request.user)
    return redirect('assignments_list')

def assignment_list(request):
    assignments = Assignment.objects.all()
    for assignment in assignments:
        print(assignment.classroom.students.all()) 
    return render(request, 'assignment_list.html', {'assignments': assignments})

class ClassroomListView(ListView):
    model = Classroom
    template_name = 'classroom_list.html'

class ClassroomCreateView(CreateView):
    model = Classroom
    fields = ['name', 'description', 'students']
    template_name = 'classroom_form.html'
    success_url = '/classrooms/'

class ClassroomDetailView(DetailView):
    model = Classroom
    template_name = 'classroom_detail.html'

class ClassroomUpdateView(UpdateView):
    model = Classroom
    fields = ['name', 'description', 'students']
    template_name = 'classroom_form.html'
    success_url = '/classrooms/'

class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        for assignment in queryset:
            print(assignment.classroom.students.all()) 
        return queryset

class AssignmentCreateView(CreateView):
    model = Assignment
    fields = ['title', 'description', 'due_date', 'classroom']
    template_name = 'assignment_form.html'
    success_url = '/assignments/'
    
    def get_context_data(self, **kwargs):
        context = super(AssignmentCreateView, self).get_context_data(**kwargs)
        context['classrooms'] = Classroom.objects.all()
        return context

class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment_detail.html'

class AssignmentUpdateView(UpdateView):
    model = Assignment
    fields = ['title', 'description', 'due_date', 'classroom']
    template_name = 'assignment_form.html'
    success_url = '/assignments/'