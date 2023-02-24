from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
	return render(request, 'BackEndBase.html')
def collegedashboard(request):
	return render(request, 'teacher-dashboard.html')
def studentdashboard(request):
	return render(request, 'student-dashboard.html')
def studentlist(request):
	return render(request, 'students.html')
def studentdetail(request):
	return render(request, 'student-details.html')
def addstudent(request):
	return render(request, 'add-student.html')
def editstudent(request):
	return render(request, 'edit-student.html')
def collegelist(request):
	return render(request, 'teachers.html')
def collegedetails(request):
	return render(request, 'teacher-details.html')
def addcollege(request):
	return render(request, 'add-teacher.html')
def editcollege(request):
	return render(request, 'edit-teacher.html')
def subjectdetails(request):
	return render(request, 'subjects.html')
def addsubject(request):
	return render(request, 'add-subject.html')
def editsubject(request):
	return render(request, 'edit-subject.html')
def feescollections(request):
	return render(request, 'fees-collections.html')
def expenses(request):
	return render(request, 'expenses.html')
def salary(request):
	return render(request, 'salary.html')
def addfeescollection(request):
	return render(request, 'add-fees-collection.html')
def addexpenses(request):
	return render(request, 'add-expenses.html')
def addsalary(request):
	return render(request, 'add-salary.html')
def exam(request):
	return render(request, 'exam.html')
def notification(request):
	return render(request, 'notification.html')
def profile(request):
	return render(request, 'profile.html')
def inbox(request):
	return render(request, 'inbox.html')
#Login View
# def login(request):
#     if not request.user.is_authenticated:
#         fm = AuthenticationForm(request=request, data=request.POST)
#         if fm.is_valid():
#             uname = fm.cleaned_data['username']
#             upass = fm.cleaned_data['password']
#             user = authenticate(username=uname, password=upass)
#             if user is not None:
#                 if user.is_active:
#                     request.session.set_expiry(600)
#                     login(request, user)
#                     messages.success(request, 'Logged in successfully !!')
#                     return HttpResponseRedirect('/profile/')
#         else:
#             fm = AuthenticationForm()
#         return render(request,'login.html', {'form':fm})
#     else:
#         return HttpResponseRedirect('/profile/')
def login(request):
	return render(request, 'BackEndBase.html')
def register(request):
	return render(request, 'register.html')
def forgotpassword(request):
	return render(request, 'forgot-password.html')
