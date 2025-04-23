from django import forms
from student_management_app.models import Courses, SessionYearModel, Staffs

class DateInput(forms.DateInput):
    input_type = "date"
try:
        proctors = Staffs.objects.all()
        proctor_list = [(proctor.id, proctor.admin.username) for proctor in proctors]
except Exception as e:
        print(e)
        proctor_list = []

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    proctor_id = forms.ChoiceField(label="Proctor", choices=proctor_list, widget=forms.Select(attrs={"class":"form-control"}))

    # For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = [(course.id, course.course_name) for course in courses]
    except Exception as e:
        print(e)
        course_list = []

    # For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = [(session_year.id, f"{session_year.session_start_year} to {session_year.session_end_year}") for session_year in session_years]
    except Exception as e:
        print(e)
        session_year_list = []
        for session_year in session_year:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)

    # For Displaying Proctors
    try:
        proctors = Staffs.objects.all()
        proctor_list = [(proctor.id, proctor.admin.username) for proctor in proctors]
    except Exception as e:
        print(e)
        proctor_list = []

    gender_list = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    proctor_id = forms.ChoiceField(label="Proctor", choices=proctor_list, widget=forms.Select(attrs={"class":"form-control"}))

class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    proctor_id = forms.ChoiceField(label="Proctor", choices=proctor_list, widget=forms.Select(attrs={"class":"form-control"}))

    # For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = [(course.id, course.course_name) for course in courses]
    except Exception as e:
        print(e)
        course_list = []

    # For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = [(session_year.id, f"{session_year.session_start_year} to {session_year.session_end_year}") for session_year in session_years]
    except Exception as e:
        print(e)
        session_year_list = []
        for session_year in session_year:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    # For Displaying Proctors
    try:
        proctors = Staffs.objects.all()
        proctor_list = [(proctor.id, proctor.admin.username) for proctor in proctors]
    except Exception as e:
        print(e)
        proctor_list = []

    gender_list = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    proctor_id = forms.ChoiceField(label="Proctor", choices=proctor_list, widget=forms.Select(attrs={"class":"form-control"}))
