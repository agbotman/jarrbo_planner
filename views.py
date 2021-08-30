from django.shortcuts import render

def jarrbo_planner(request):
    return render(request, 'jarrbo_planner.html',)
    
def jarrbo_planner_two(request):
    return render(request, 'jarrbo_planner_two.html',)

def jarrbo_planner_three(request):
    return render(request, 'jarrbo_planner_three.html',)
