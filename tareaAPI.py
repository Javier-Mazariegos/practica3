import random
from flask import Flask, url_for, request,redirect
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)

lista = []
def crear(n):
    global lista
    lista =[]
    for i in range(n):
        resultado = random.randint(0,1000)+ lista[i-1] if i!=0 else random.randint(0,100)
        lista.append(resultado)

@app.route("/linearsearch/<int:n>/<int:value>",methods=["GET"])
def linaer_search(n,value):
    global lista
    crear(n)
    r = "El numero no está en la lista"
    for i in range(len(lista)):
        if(value == lista[i]):
            r = "Se encontro en la posicion: " + i 
            break
    return r

@app.route("/binarysearch/<int:n>/<int:value>",methods=["GET"])
def binary_search(n,value):
    global lista
    crear(n)
    s = len(lista) -1
    i = 0 
    m = 0
    while True:
        if i <= s:
            m = int((i+s)/2)
            if(lista[m] == value):
                return "Se encontro en la posicion: " + m
            elif(lista[m] > value):
                s = m-1
            elif(lista[m] < value):
                i = m+1
        else:
            break
    return "El numero no está en la lista"


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

