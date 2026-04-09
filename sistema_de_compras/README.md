# 🛒 Sistema básico de gestión de compras

Este proyecto es un programa en Python que permite gestionar una lista de compras desde la consola. Fue desarrollado como práctica de programación y trabajo colaborativo usando Git y GitHub.

---

## 📌 Características

El sistema permite:

* ➕ Agregar productos a una lista
* 📋 Mostrar todos los productos registrados
* 💰 Calcular el total de la compra
* 🔍 Filtrar productos por precio (mayores a un valor)
* 🔁 Ejecutarse en un ciclo hasta que el usuario decida salir

---

## 🧱 Estructura del proyecto

```
sistema_de_compras/
│
├── main.py          # Archivo principal (menú)
├── productos.py     # Funciones para manejar productos
├── calculos.py      # Funciones de cálculos y filtros
└── README.md
```

---

## ⚙️ Requisitos

* Python 3.x instalado

---

## ▶️ Cómo ejecutar el programa

1. Clonar el repositorio:

```
git clone https://github.com/jekani-009/sistema_de_compras.git
```

2. Entrar a la carpeta:

```
cd sistema_de_compras
```

3. Ejecutar el programa:

```
python main.py
```

---

## 🧠 Uso del programa

Al ejecutar el programa, aparecerá un menú con opciones:

```
1. Agregar producto
2. Mostrar productos
3. Calcular total
4. Filtrar productos
5. Salir
```

Solo debes ingresar el número de la opción deseada.

---

## 👥 Trabajo en equipo

Este proyecto fue desarrollado usando Git y GitHub con trabajo en ramas:

* Rama `feature-productos`: manejo de productos
* Rama `feature-calculos`: cálculos y filtros

Cada integrante trabajó en su propia rama y luego se integraron los cambios mediante Pull Requests.

---

## 🔄 Flujo de trabajo con Git

1. Crear una rama:

```
git checkout -b nombre-rama
```

2. Guardar cambios:

```
git add .
git commit -m "Descripción del cambio"
```

3. Subir cambios:

```
git push origin nombre-rama
```

4. Crear Pull Request en GitHub

---

## 🚀 Posibles mejoras

* Guardar productos en archivos (.json o .txt)
* Agregar validaciones de entrada
* Mejorar la interfaz en consola
* Crear interfaz gráfica

---

## 📄 Licencia

Este proyecto es de uso educativo.

