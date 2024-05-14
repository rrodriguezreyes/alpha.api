# Alpha.API

Alpha.API es una API construida con FastAPI para administrar productos y realizar cálculos de inversión.

## Estructura del Proyecto

El proyecto sigue una estructura de directorios básica:

- `app/`: Contiene el código fuente de la aplicación.
  - `api/`: Módulos que definen los puntos finales de la API.
  - `db/`: Módulos para interactuar con la base de datos.
  - `models/`: Definiciones de modelos de datos.
  - `services/`: Módulos para la lógica de negocio y los servicios.
- `main.py`: Punto de entrada principal de la aplicación.
- `requirements.txt`: Archivo que enumera todas las dependencias del proyecto.

Este proyecto ha sido desplegado en Azure y se ha creado una base de datos PostgreSQL en Azure. Puedes acceder al API en el siguiente enlace: https://alpha-calculator-api.azurewebsites.net/docs. Aquí puedes realizar pruebas sin necesidad de instalar nada en tu máquina local.

Se ha configurado un pipeline para la implementación continua. Cada vez que se realiza un push a la rama main, el API se actualiza automáticamente en Azure.

![image](https://github.com/rrodriguezreyes/alpha.api/assets/39017677/2530a4a4-36e0-4249-a944-3474db6b969f)

![image](https://github.com/rrodriguezreyes/alpha.api/assets/39017677/e29257ec-c574-4c44-b0f6-56b5c75e45ba)
![image](https://github.com/rrodriguezreyes/alpha.api/assets/39017677/6b042905-e475-48a5-abdd-efaf48997572)
![image](https://github.com/rrodriguezreyes/alpha.api/assets/39017677/08dd63e3-97c2-442c-ab02-a5e0c314c7e7)


## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/rrodriguezreyes/alpha.api.git


