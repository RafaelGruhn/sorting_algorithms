import os

from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
import time
import sys
sys.setrecursionlimit(1000000)


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
        context = {}
        for i in range(1, 3):
            context['algoritmo' + str(i)] = request.POST.get('algoritmo' + str(i))
            disposicao = request.POST.get('disposicao_dados')
            lista = self.return_list_disposition(disposicao)
            nos = int(request.POST.get('nos'))
            del lista[nos:]
            context['nos'] = nos

            start_time = time.time()
            if (context.get('algoritmo' + str(i)) == "selection_sort"):
                lista = self.selection_sort(lista)

            elif (context.get('algoritmo' + str(i)) == "insertion_sort"):
                lista = self.insertion_sort(lista)

            elif (context.get('algoritmo' + str(i)) == "bubble_sort"):
                lista = self.bubble_sort(lista)

            elif (context.get('algoritmo' + str(i)) == "shell_sort"):
                lista = self.shell_sort(lista)
            else:
                lista = self.quick_sort(lista)
            result = (time.time() - start_time)

            context['resultado' + str(i)] = result
        return render(request, self.template_name, context)

    def return_list_disposition(self, disposicao):
        if(disposicao == "option1"):
            return self.ordenados
        elif(disposicao == "option2"):
            return self.decrescente
        return self.aleatorio

    def selection_sort(self, lista):
        for i in range(0, len(lista)): 
            d=lista.index(min(lista[i:]))
            c=lista[i]
            lista[i]=min(lista[i:])
            lista[d]=c
        return lista

    def insertion_sort(self, lista):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i-1
            while j >= 0 and key < lista[j]:
                    lista[j + 1] = lista[j]
                    j -= 1
            lista[j + 1] = key
        return lista

    def bubble_sort(self, lista):
        for passnum in range(len(lista)-1,0,-1):
            for i in range(passnum):
                if lista[i]>lista[i+1]:
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
        return lista

    def shell_sort(self, lista):
        gap = lista.__len__() // 2
        while gap > 0:
            for i in range(gap, lista.__len__()):
                temp = lista[i]
                j = i
                while j >= gap and lista[j - gap] > temp:
                    lista[j] = lista[j - gap]
                    j -= gap
                lista[j] = temp
            gap //= 2
        return lista

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            return self.quick_sort([x for x in lista[1:] if x < lista[0]]) + \
                [lista[0]] + \
                self.quick_sort([x for x in lista[1:] if x >= lista[0]])
