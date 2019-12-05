import os

from django.shortcuts import redirect
from django.views.generic.base import TemplateView


def index(request):
    return redirect('home')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class HomeView(TemplateView):
    template_name = 'index.html'
    aleatorio = []
    decrescente = []
    ordenados = []

    def __init__(self):
        with open(os.path.join(BASE_DIR, 'sortions/numeros_aleatorios.txt'), 'r') as f:
            file_list = f.readlines()
            for i in file_list:
                self.aleatorio.append(int(i))

        with open(os.path.join(BASE_DIR, 'sortions/numeros_ordem_decrescente.txt'), 'r') as f:
            file_list = f.readlines()
            for i in file_list:
                self.decrescente.append(int(i))

        with open(os.path.join(BASE_DIR, 'sortions/numeros_ordenados.txt'), 'r') as f:
            file_list = f.readlines()
            for i in file_list:
                self.ordenados.append(int(i))


    def post(self, request):
        algoritmo1 = request.POST.get('algoritmo1')
        if (algoritmo1 == "selection_sort"):
            disposicao = request.POST.get('disposicao_dados')
            nos = int(request.POST.get('nos'))
            lista = self.return_list_disposition(disposicao)
            result = self.selection_sort(lista, nos)
            print(result)

    def return_list_disposition(self, disposicao):
        if(disposicao == "option1"):
            return self.ordenados
        elif(disposicao == "option2"):
            return self.decrescente
        return self.aleatorio

    def selection_sort(self, lista, nos):
        del lista[nos:]
        for i in range(0, len(lista)): 
            d=lista.index(min(lista[i:]))
            c=lista[i]
            lista[i]=min(lista[i:])
            lista[d]=c
        return lista

    def insertion_sort(self, request):
        pass

    def bubble_sort(self, request):
        pass

    def shell_sort(self, request):
        pass

    def quick_sort(self, request):
        pass
