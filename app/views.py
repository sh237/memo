import datetime
from django.shortcuts import redirect, render
from django.views import generic
from .forms import BS4ScheduleForm, SimpleScheduleForm
from .models import Schedule
from . import mixins
from . import models

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'app/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class MonthWithFormsCalendar(mixins.MonthWithFormsMixin, generic.View):
    """フォーム付きの月間カレンダーを表示するビュー"""
    template_name = 'app/month_with_forms.html'
    model = Schedule
    date_field = 'date'
    form_class = SimpleScheduleForm
    def get(self, request, **kwargs): 
        context = self.get_month_calendar()
        return render(request, self.template_name, context)
        
    def post(self, request, **kwargs):
        context = self.get_month_calendar()
        formset = context['month_formset']
        if formset.is_valid():
            formset.save()
            return redirect('app:month_with_forms')

        return render(request, self.template_name, context) 

class MonthDetailCalendar(mixins.MonthCalendarMixin, generic.ListView):
    """詳細情報付きのカレンダーをユーザー毎に表示するビュー"""
    template_name = 'app/month_detail.html'
    queryset = models.Schedule.objects

    # レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "record_list"

    # テンプレートファイル連携

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context
 
class HomeView(generic.TemplateView):
    template_name = 'home.html'

class WelcomeView(generic.TemplateView):
    template_name = 'welcome.html'