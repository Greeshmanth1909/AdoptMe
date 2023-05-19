from django.shortcuts import render

# Create your views here.
def chat_view(request, *args, **kwargs):
    # chat stuff here
    context = dict()
    
    return render(request, 'chat/chatHome.html', context)