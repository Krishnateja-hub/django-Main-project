from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import StudentForm

# Create your views here.

def register(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            form=StudentForm()
            return redirect('student_list')
    else:
        form=StudentForm()
    return render(request,'myapp/register.html',{'form':form})
def students(request):
    student=Student.objects.all()
    return render(request,'myapp/students.html',{'student_list':student})  
def edit(request,id):
    student=Student.objects.get(pk=id) 
    if request.method=='POST':  
      form = StudentForm(request.POST,instance=student)
      if form.is_valid():
          form.save(commit=True)  
          return redirect('student_list')
      else:
          {'error':'Form object data not valid'}
    else:
        form=StudentForm(instance=student)  
    return render(request,'myapp/edit.html',{'form':form,'student':student})  
def show(request,id):
    student=Student.objects.get(pk=id)
    return render(request,'myapp/show.html',{'student':student})  
def delete(request,id):
    student=Student.objects.get(pk=id)
    if request.method=='POST':
        student.delete()
        return redirect('student_list')
    return render(request,'myapp/delete.html',{'student':student})
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
