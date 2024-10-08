from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from calendario.models import atividades
import calendar
from datetime import datetime, date
from calendario.forms import AtividadesForm
from django.core.paginator import Paginator
from .models import Squad, FreezingPeriod
from .forms import SquadForm, FreezingPeriodForm
from django.db.models import F, Q
from .models import atividades, Squad
import locale
from rest_framework import viewsets
from .models import Squad, atividades, FreezingPeriod
from .serializers import SquadSerializer, AtividadesSerializer, FreezingPeriodSerializer

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors

import openpyxl
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
import calendar
from .models import atividades, Squad, FreezingPeriod
from django.db.models import F

import pandas as pd
from django.http import HttpResponse
from .models import atividades

from django.template.loader import render_to_string
from xhtml2pdf import pisa




# Definir o local para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@login_required
def calendario(request):
    # Obter parâmetros da URL
    mes = int(request.GET.get('month', date.today().month))
    ano = int(request.GET.get('year', date.today().year))
    view_mode = request.GET.get('view', 'calendario')  # 'calendario' ou 'lista'

    cal = calendar.monthcalendar(ano, mes)

    # Ordenar eventos por hora
    eventos = atividades.objects.filter(data__year=ano, data__month=mes).annotate(cor_area=F('area__cor')).order_by('data', 'hora')
    areas = Squad.objects.filter(atividades__data__year=ano, atividades__data__month=mes).distinct()

    freezing_periods = FreezingPeriod.objects.filter(start_date__year=ano, start_date__month=mes)

    context = {
        'cal': cal,
        'mes_atual': calendar.month_name[mes].capitalize(),
        'mes_atual_num': mes,
        'ano_atual': ano,
        'eventos': eventos,
        'areas': areas,
        'anterior_mes': mes - 1 if mes > 1 else 12,
        'proximo_mes': mes + 1 if mes < 12 else 1,
        'ano': ano,
        'freezing_periods': freezing_periods,
        'view_mode': view_mode  # Passar o modo de visualização para o template
    }

    if view_mode == 'lista':
        return render(request, 'calendario/lista.html', context)
    else:
        return render(request, 'calendario/calendario.html', context)

# Create your views here.
def home(request):
    return render(request, 'calendario/home.html')

@login_required
def products(request):
    return render(request, 'calendario/products.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

def exit(request):
    logout(request)
    return(redirect('home'))

@login_required
def adicionar(request):
    data = {}
    data['form'] = AtividadesForm()
    return render(request, 'calendario/adicionar.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        form = AtividadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar')  # Redirecionar para a página inicial após salvar o evento
        else:
            form = AtividadesForm()
    print(form)
    return render(request, 'adicionar.html', {'form': form})

@login_required
def create_squad(request):
    if request.method == 'POST':
        form = SquadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_squads')  # Redirecione para a página inicial ou outra página de sua escolha
    else:
        form = SquadForm()
    return render(request, 'calendario/create_squad.html', {'form': form})

@login_required
def edit_squad(request, id):
    squad = get_object_or_404(Squad, id=id)
    if request.method == 'POST':
        form = SquadForm(request.POST, instance=squad)
        if form.is_valid():
            form.save()
            return redirect('list_squads')
    else:
        form = SquadForm(instance=squad)
    return render(request, 'calendario/edit_squad.html', {'form': form})

@login_required
def delete_squad(request, id):
    squad = get_object_or_404(Squad, id=id)
    if request.method == 'POST':
        squad.delete()
        return redirect('list_squads')
    return render(request, 'calendario/delete_squad.html', {'squad': squad})

def add_freezing_period(request):
    if request.method == 'POST':
        form = FreezingPeriodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_freezing_periods')
    else:
        form = FreezingPeriodForm()
    return render(request, 'calendario/add_freezing_period.html', {'form': form})

def edit_freezing_period(request, pk):
    freezing_period = get_object_or_404(FreezingPeriod, pk=pk)
    if request.method == 'POST':
        form = FreezingPeriodForm(request.POST, instance=freezing_period)
        if form.is_valid():
            form.save()
            return redirect('list_freezing_periods')
    else:
        form = FreezingPeriodForm(instance=freezing_period)
    return render(request, 'calendario/edit_freezing_period.html', {'form': form})


def delete_freezing_period(request, pk):
    freezing_period = get_object_or_404(FreezingPeriod, pk=pk)
    if request.method == 'POST':
        freezing_period.delete()
        return redirect('list_freezing_periods')
    return render(request, 'calendario/delete_freezing_period.html', {'freezing_period': freezing_period})

@login_required
def detalhes_atividade(request, pk):
    data = {}
    data['db'] = atividades.objects.get(pk=pk)
    print(data)
    return render(request, 'calendario/detalhes_atividade.html', data)

@login_required
def edit_atividade(request, pk):
    data = {}
    data['db'] = atividades.objects.get(pk=pk)
    data['form'] = AtividadesForm(instance=data['db'])
    return render(request, 'calendario/adicionar.html', data)

@login_required
def update(request, pk):
    data = {}
    data['db'] = atividades.objects.get(pk=pk)
    form = AtividadesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
       form.save()
    return redirect('listar')

@login_required
def delete(request, pk):
    db = atividades.objects.get(pk=pk)
    print(db)
    db.delete()
    return redirect('listar')

def gerar_excel(request,mes, ano):

    if not mes or not ano:
        return HttpResponse("Mês ou ano não foram fornecidos.", content_type="text/plain")

    # Filtrar dados com base no mês e ano fornecidos
    eventos = atividades.objects.filter(data__year=ano, data__month=mes).values('data', 'hora', 'titulo', 'area__nome')
    print(eventos)

    # Criar o DataFrame
    df = pd.DataFrame(list(eventos))

    # Verificar se o DataFrame está vazio
    if df.empty:
        return HttpResponse("Nenhum dado disponível para gerar o relatório.", content_type="text/plain")

    # Renomear colunas para uma apresentação melhor no Excel
    df.columns = ['Data', 'Hora', 'Título', 'Área']

    # Gerar o arquivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=relatorio_{mes}_{ano}.xlsx'

    # Escrever o DataFrame no arquivo Excel
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return response


def gerar_pdf(request):
    mes = 6
    ano = 2024

    # Filtrar dados e criar DataFrame
    eventos = atividades.objects.filter(data__year=ano, data__month=mes).values('data', 'hora', 'titulo', 'area__nome')
    df = pd.DataFrame(list(eventos))
    print(df)

    # Verificar se o DataFrame está vazio
    if df.empty:
        return HttpResponse("Nenhum dado disponível para gerar o relatório.", content_type="text/plain")

    # Converter DataFrame para HTML
    df.columns = ['Data', 'Hora', 'Título', 'Área']
    html_table = df.to_html(index=False)

    # Criar um contexto para o template
    context = {
        'mes': mes,
        'ano': ano,
        'tabela': html_table,
    }

    # Renderizar o template HTML com a tabela
    html = render_to_string('calendario/relatorio_template.html', context)

    # Converter o HTML para PDF usando xhtml2pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=relatorio.pdf'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', content_type='text/plain')
    return response


class SquadViewSet(viewsets.ModelViewSet):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

class AtividadesViewSet(viewsets.ModelViewSet):
    queryset = atividades.objects.all()
    serializer_class = AtividadesSerializer

class FreezingPeriodViewSet(viewsets.ModelViewSet):
    queryset = FreezingPeriod.objects.all()
    serializer_class = FreezingPeriodSerializer

# opções de listagem.
@login_required
def listar_atividades(request):
    data = {}
    search = request.GET.get('search')

    if search:
        data['db'] = atividades.objects.filter(titulo__icontains=search).order_by('data', 'hora')
    else:
        data['db'] = atividades.objects.all().order_by('data')

    all = data['db']

    paginator = Paginator(all, 8)
    pages = request.GET.get('page')

    data['db'] = paginator.get_page(pages)

    return render(request, 'calendario/listar_atividades.html', data)

@login_required
def list_squads(request):
    squads = Squad.objects.all()
    return render(request, 'calendario/list_squads.html', {'squads': squads})

@login_required
def list_freezing_periods(request):
    freezing_periods = FreezingPeriod.objects.all()
    return render(request, 'calendario/list_freezing_periods.html', {'freezing_periods': freezing_periods})

@login_required
def listar_atividades_area(request, area_id, mes, ano):
    eventos = atividades.objects.filter(data__year=ano, data__month=mes, area_id=area_id)
    area = Squad.objects.get(id=area_id)

    context = {
        'eventos': eventos,
        'mes_atual': calendar.month_name[mes],
        'ano_atual': ano,
        'area': area,
    }
    return render(request, 'calendario/listar_atividades_area.html', context)



