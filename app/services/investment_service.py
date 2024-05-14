from datetime import datetime, timedelta
from app.db import investment_repository
from app.models.investment import InvestmentRequest, InvestmentResponse

async def calculate_investment_dates(request: InvestmentRequest) -> InvestmentResponse:
    try:
        # Obtener la configuración del producto
        product_properties = await investment_repository.get_configuration(request.product_id)

        # Obtener la hora operativa
        hora_operativa = product_properties["operational_hour"]

        # Calcular las fechas de inversión
        fecha_inicio = datetime.strptime(request.fecha_creacion, "%Y-%m-%d %H:%M:%S")
        plazo = request.plazo

        # Ajustar la fecha de inicio según el horario operativo
        if fecha_inicio.hour <= hora_operativa.hour:
            dias_a_sumar = product_properties["days_creation_below_operational_hour"]
        else:
            dias_a_sumar = product_properties["days_creation_above_operational_hour"]

        # Ajustar la fecha de inicio para reinversiones
        if request.en_reinversion:
            if fecha_inicio.hour <= hora_operativa.hour:
                dias_a_sumar = product_properties["days_creation_below_operational_hour_reinvestment"]
            else:
                dias_a_sumar = product_properties["days_creation_above_operational_hour_reinvestment"]

        fecha_inicio += timedelta(days=dias_a_sumar)
        # Obtener la lista de días feriados
        dias_feriados = await investment_repository.get_holidays()

        # Calcular la fecha de fin inicial
        fecha_fin = fecha_inicio + timedelta(days=plazo)

        # Ajustar la fecha de fin para que no sea un día festivo ni fin de semana
        while fecha_fin.weekday() >= 5 or fecha_fin.date() in dias_feriados:
            fecha_fin += timedelta(days=1)

        # Calcular plazo real (añadiendo 1 para incluir el día de inicio)
        plazo_real = (fecha_fin - fecha_inicio).days

        return InvestmentResponse(
            product_id=request.product_id,
            plazo=plazo,
            fechaInicio=fecha_inicio.strftime("%Y-%m-%d"),
            fechaFin=fecha_fin.strftime("%Y-%m-%d"),
            plazoReal=plazo_real
        )

    except Exception as e:
        # Manejar errores
        raise e
