import os

from django.shortcuts import redirect
from django.views.generic.base import TemplateView


def index(request):
    return redirect('home')

class HomeView(TemplateView):
    template_name = 'index.html'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    aleatorio = []
    decrescente = []
    ordenados = []

    with open(os.path.join(BASE_DIR, 'sortions/numeros_aleatorios.txt'), 'r') as f:
        file_list = f.readlines()
        for i in file_list:
            aleatorio.append(int(i))

    with open(os.path.join(BASE_DIR, 'sortions/numeros_ordem_decrescente.txt'), 'r') as f:
        file_list = f.readlines()
        for i in file_list:
            aleatorio.append(int(i))

    with open(os.path.join(BASE_DIR, 'sortions/numeros_ordenados.txt'), 'r') as f:
        file_list = f.readlines()
        for i in file_list:
            aleatorio.append(int(i))

    def post(self, request):
        algoritmo1 = request.POST.get('algoritmo1')
        if (algoritmo1 == "selection_sort"):
            disposicao = request.POST.get('disposicao_dados')
            nos = request.POST.get('nos')
            lista =
            result = self.selection_sort(disposicao, nos)
        return result

    def return_list_disposition(self, request, disposicao):
        if("")

    def selection_sort(self, disposicao, nos):
        for i in range(len()): 
            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, nos): 
                if disposicao[min_idx] > A[j]: 
                    min_idx = j 
                    
            # Swap the found minimum element with  
            # the first element         
            A[i], A[min_idx] = A[min_idx], A[i] 
        
        # Driver code to test above 
        print ("Sorted array") 
        for i in range(len(A)): 
            print("%d" %A[i]),  

    def insertion_sort(self, request):
        pass

    def bubble_sort(self, request):
        pass

    def shell_sort(self, request):
        pass

    def quick_sort(self, request):
        pass
