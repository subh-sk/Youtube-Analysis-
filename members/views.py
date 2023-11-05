from django.shortcuts import render 
from django.template import loader
from django.http import HttpResponse 
import sys
import subprocess
from django.http import HttpResponseRedirect
from .main import main
from django.http import JsonResponse

def form_submit(request):
    if request.method == 'POST':

        global youtube_url,keyword
        youtube_url = request.POST.get('youtube_url')
        keyword = request.POST.get('keyword')
        
        fetch=main(youtube_url=youtube_url,keyword=keyword)
        print("fetch = ",fetch)
        return render(request, 'search.html', {'fetch': fetch})
        # return JsonResponse({'comments': fetch})
    else:
        return render(request, 'index.html')


# def search(request):
#     template = loader.get_template('a.html')
#     return HttpResponse(template.render())

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
# if __name__=='__main__':
#     input = "explore"
#     # user_input = input.strip().lower()
#     # print("usr_input =",user_input)
#     # user_input =  suggest_correction(user_input,word_list=list(apps_to_fetch))
#     # if main(user_input=user_input)!=0:
#     #       sys.exit()
#     # else:
#     #       exe_list = exe_fetch()
#     #       exe_search(app_name=input,exe_files=exe_list)
#     main_search(input=input)