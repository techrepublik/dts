https://github.com/techrepublik/dts/blob/main/static/dist/img/logo/logo1.jpg





# [Django AdminLTE](https://appseed.us/product/adminlte/django/)

Open-source **Django** project crafted on top of **[AdminLTE](https://appseed.us/product/adminlte/django/)**, an open-source and iconic `Bootstrap` design.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 [Django AdminLTE](https://appseed.us/product/adminlte/django/) - `Product page`
- 👉 [Django AdminLTE](https://adminlte-django.appseed-srv1.com/) - `LIVE Demo`

---

## 🚀 **[Black Friday Campaign](https://appseed.us/)** is LIVE: `65%Off`

> `React`, `Django`, `Flask`, and `NodeJs` starters crafted and actively supported by **AppSeed**
 
[![](https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/280080081-1e7c91c0-612f-4418-81e7-34c363378479.jpg)](https://appseed.us/)

<br />

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [PRO Version](https://appseed.us/product/material-dashboard2-pro/django/)    | 🚀 Custom - $1999 (plus VAT)         |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ **Django 4.1.12**                   | **Everything in Free**, plus:                                        | **Everything in PRO**, plus:       |
| ✓ Best Practices                      | ✅ **Premium Bootstrap Design**                                      | ✅ **1mo Custom Development**     | 
| ✓ Bootstrap Design                    | ✅ `Private REPO Access`                                             | ✅ **Dedicated Developer**        |
| ✓ `Docker`                            | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/)  | ✅ Weekly Sprints                 |
| ✓ `CI/CD` Flow via Render             | ✅ Deployment Assistance                                             | ✅ Technical SPECS                |
| ✓ `Free Support                       | -                                                                     | ✅ Documentation                  |
| -                                     | -                                                                     | ✅ **30 days Delivery Warranty**  |
| ------------------------------------  | ------------------------------------                                  | ------------------------------------|
| ✓ [LIVE Demo](https://adminlte-django.appseed-srv1.com/)  | 🚀 [LIVE Demo](https://django-material-dash2-pro.onrender.com/) | 🛒 `Order`: **[$1999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |  

![AdminLTE - Full-Stack Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/168842202-9b80a957-a375-4e6d-8247-2cc459267a86.png)

<br />

## Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`)

```bash
$ git clone https://github.com/app-generator/django-adminlte.git
$ cd django-adminlte
```

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-adminlte.git
$ cd django-adminlte
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                  # Project Configuration  
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views 
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models 
   |    |-- tests.py                     # Tests  
   |    |-- templates/                   # Theme Customisation 
   |         |-- includes                # 
   |              |-- custom-footer.py   # Custom Footer      
   |     
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize 

When a template file is loaded, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The theme used to style this starter provides the following files: 

```bash
# This exists in ENV: LIB/admin_adminlte
< UI_LIBRARY_ROOT >                      
   |
   |-- templates/                     # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- login.html           # Sign IN Page
   |    |    |-- register.html        # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html            # Masterpage
   |    |    |-- base-auth.html       # Masterpage for Auth Pages
   |    |
   |    |-- pages/       
   |         |-- index.html           # Dashboard Page
   |         |-- calendar.html        # Profile Page
   |         |-- *.html               # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

> For instance, if we want to **customize the footer.html** these are the steps:

- ✅ `Step 1`: create the `templates` DIRECTORY inside the `home` app
- ✅ `Step 2`: configure the project to use this new template directory
  - `core/settings.py` TEMPLATES section
- ✅ `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `home/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_adminlte/template/includes/footer.html`
  - Destination PATH: `<PROJECT_ROOT>home/templates/includes/footer.html`

> To speed up all these steps, the **codebase is already configured** (`Steps 1, and 2`) and a `custom footer` can be found at this location:

`home/templates/includes/custom_footer.html` 

By default, this file is unused because the `theme` expects `footer.html` (without the `custom-` prefix). 

In order to use it, simply rename it to `footer.html`. Like this, the default version shipped in the library is ignored by Django. 

In a similar way, all other files and components can be customized easily.

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## [PRO Version](https://appseed.us/product/material-dashboard2-pro/django/)   

This design is a pixel-perfect [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design inspired by Google's Material Design. `Material Dashboard 2 PRO` is built with over 300 frontend individual elements, like buttons, inputs, navbars, nav tabs, cards, or alerts, giving you the freedom of choosing and combining.

> Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Material2](https://github.com/app-generator/django-admin-material2-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Material Dashboard 2 Pro](https://user-images.githubusercontent.com/51070104/211141418-6b7886eb-6fb3-433e-91c9-2895c086099a.png)

<br />

---
[Django AdminLTE](https://appseed.us/product/adminlte/django/) - Open-Source **Django** starter provided by **[AppSeed](https://appseed.us/)**
