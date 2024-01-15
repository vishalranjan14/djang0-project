from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return render(request, './templates/calculator/home.html')

def index(request):
    context={
        'variable':"this is my first variable"
    }
    return render(request,'index.html',context)
def home(request):
    return HttpResponse("this is a django server123")

def about(request):
    return HttpResponse("this is a about page ")

def peek(request):
    return HttpResponse("this is a peek page ")

def members(request):
    return HttpResponse("this is a members page ")


def success_page(request):
    return HttpResponse("this is a success page ")

def success_page(request):
    return

def careers(request):
     return render(request,'careers.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero!'
        else:
            result = 'Invalid operation'

        return render(request, 'calculator/home.html', {'result': result})

    return HttpResponse('Method not allowed')
