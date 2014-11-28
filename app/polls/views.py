#-*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404,render #,render_to_response 
#from django.template import RequestContext,loader,Context
from django.http import HttpResponseRedirect #,HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Question,Choice
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

# Create your views here.

'''
def index(request):
    #对象
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    #要套用的模板，也可以直接用get_tenplate()
    template = loader.get_template('polls/index.html')
    #使用RequestContext渲染模板
    #request后的第一个参数传给视图的第一个参数，也算是对象
    context = RequestContext(request,{
        'latest_question_list':latest_question_list
        })
    return HttpResponse(template.render(context))
    #这里使用了RequestContext处理器，也可以用Context处理器实现，或render实现
    

方法一
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

方法二
可以用python的内建方法locals()代替字典
locals()返回一个包含当前作用域里面的所有变量和它们的值的字典
    context = Context({'latest_question_list':latest_question_list})
    return HttpResponse(template.render(context))
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_data')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

'''def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    template = loader.get_template('polls/detail.html')
    context = Context({'question':question})
    return HttpResponse(template.render(context))
'''
@csrf_exempt
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        '''return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })'''
        t = loader.get_template('polls/detail.html')
        c = Context({
            'question': p,
            'error_message': "You didn't select a choice.",
            })
        return HttpResponse(t.render(c))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

