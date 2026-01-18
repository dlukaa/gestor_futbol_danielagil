# ⚽ Gestor de Fútbol (Odoo App)

![Odoo](https://img.shields.io/badge/Odoo-16.0%2B-purple?style=for-the-badge&logo=odoo) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python) ![License](https://img.shields.io/badge/License-LGPL--3-green?style=for-the-badge)

## 📖 Descripción

**Gestor de Fútbol** es un módulo completo para Odoo diseñado para la administración integral de clubes deportivos. Permite centralizar la gestión de equipos, personal técnico, jugadores y el seguimiento de competiciones.

Este módulo ha sido desarrollado como parte de la **Práctica 11** de Sistemas de Gestión Empresarial.

📄 **[Ver Memoria del Proyecto (PDF)](Gil_Rodríguez_Daniela_Memoria_ProyectooOdoo_DAM25.pdf)**

---

## ✨ Características Principales

🔹 **Gestión de Clubes**: Registro detallado de clubes de fútbol.
🔹 **Base de Datos de Jugadores**: Perfiles completos con estadísticas y datos personales.
🔹 **Cuerpo Técnico**: Administración de entrenadores y staff.
🔹 **Competiciones y Partidos**: Seguimiento de torneos, jornadas y resultados en tiempo real.
🔹 **Vistas Intuitivas**: Interfaz amigable totalmente integrada con el backend de Odoo.

---

## 🚀 Instalación

Sigue estos pasos para instalar el módulo en tu instancia de Odoo:

1.  **Clonar el repositorio**:
    Navega a la carpeta `addons` de tu instalación de Odoo y clona este proyecto:
    ```bash
    git clone https://github.com/dlukaa/gestor_futbol_danielagil.git
    ```

2.  **Actualizar lista de aplicaciones**:
    - Activa el **Modo Desarrollador** en Odoo.
    - Ve a *Aplicaciones* > *Actualizar lista de aplicaciones*.

3.  **Instalar el módulo**:
    - Busca `Gestor de Fútbol` en la barra de búsqueda.
    - Haz clic en **Activar**.

---

## 📂 Estructura del Módulo

El proyecto sigue la estructura estándar de Odoo:

```plaintext
gestor_futbol/
├── controllers/      # Controladores web
├── models/           # Definición de modelos (tablas y lógica)
├── security/         # Reglas de acceso y permisos (CSV)
├── views/            # Vistas XML (Formularios, Listas, Kanban)
├── demo/             # Datos de demostración
├── __manifest__.py   # Metadatos del módulo
└── __init__.py       # Inicializador del paquete Python
```

---

## 👤 Autor

Desarrollado por **Daniel Gil**.
*Repositorio GitHub*: [dlukaa/gestor_futbol_danielagil](https://github.com/dlukaa/gestor_futbol_danielagil)

