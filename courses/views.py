from django.shortcuts import render, get_object_or_404, redirect
from django.views import views #(Used to Convert view function to class based view)
from .models import Course
from .forms import CourseModelForm

# Create your views here.

class CourseObjectMixin(object):
    model = Course
    lookup = "id"

    def get_object(self):

         id = self.kwargs.get(se;f.lookup)
         obj = None
         if id is not None:
             obj = get_object_or_404(self.model, id=id)

         return obj






#BASE View Class = View

class CourseDeleteView(View):
    template_name = "courses/courses_delete.html"

    def get_object(self):

        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)

        return obj

    def get(self, request, *args, **kwargs):
        #GET method
        context={}
        obj = self.object.get()

        if obj is not None:
            context['object'] = obj

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        #GET method
        context={}
        obj = self.object.get()

        if obj is not None:
            obj.delete()
            context['object'] =None
            return redirect('courses/')

        return render(request,self.template_name, context)














class CourseUpdateView(View):
    template_name = "courses/courses_update.html"

    def get_object(self):

        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)

        return obj

    def get(self, request, *args, **kwargs):
        #GET method
        context={}
        obj = self.object.get()

        if obj is not None:
            forms = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        #GET method
        context={}
        obj = self.object.get()

        if obj is not None:
            forms = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form

        return render(request,self.template_name, context)





class CourseCreateView(View):
    template_name = "courses/courses_create.html"
    def get(self, request, *args, **kwargs):
        #GET method
        forms = CourseModelForm()
        context = {
            "form": form
        }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        #GET method
        forms = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()

        context = {
            "form": form
        }
        return render(request,self.template_name, context)

class CourseView(View):
    template_name = "contact.html"
    def get(self, request, *args, **kwargs):
        #GET method
        return render(request,self.template_name, {})

    # def post(self, request, *args, **kwargs):
    #     return render(request,'about.html', {})

#HttpMethod
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request,'about.html', {})

class CourseView(View):
    template_name = "courses/courses_detail.html"
    def get(self, request, id=None, *args, **kwargs):
        #GET method
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context["object"] = obj
        return render(request,self.template_name, context)

def my_fbv(request, *args, **kwargs):
        print(request.method)
        return render(request,'about.html', {})


class CourseListView(View):
    template_name = "courses/courses_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {"object_list": self.queryset()}
        return render(request,self.template_name,context)
