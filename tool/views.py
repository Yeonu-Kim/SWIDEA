from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q
from .models import DevTool
from .forms import DevToolForm

# Create your views here.
def index(request):
    tool_list = DevTool.objects.all()
    keyword = request.GET.get('keyword', '')
    if keyword:
        tool_list = tool_list.filter(
            Q(name__icontains=keyword)
        )
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest"
    if is_ajax_request:
        html = render_to_string(
            template_name="tool/tool_list.html", 
            context={"tool_list": tool_list}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data_dict)        
    return render(request, 'tool/tool_index.html', {'tool_list': tool_list})

def create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            tool = form.save()
            return redirect('tool:detail', pk=tool.id)
    else:
        form = DevToolForm()
    return render(request, 'tool/tool_create.html', {'form': form})

def detail(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    idea_list = tool.idea_set.all()
    return render(request, 'tool/tool_detail.html', {'tool': tool, 'idea_list': idea_list})

def modify(request, pk):
    tool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tool:detail', pk=pk)
    else:
        form=DevToolForm(instance=tool)
    return render(request, 'tool/tool_modify.html', {'form': form, 'pk': pk})

def delete(request, pk):
    if request.method == 'POST':
        tool = get_object_or_404(DevTool, pk=pk)
        tool.delete()
    return redirect('tool:index')