from django.shortcuts import render
from .models import Estudiante, Asistencia

def dashboard(request):

    total_estudiantes = Estudiante.objects.count()

    total_huellas = Estudiante.objects.exclude(
        huella_id__isnull=True
    ).count()

    asistencias_hoy = Asistencia.objects.count()

    ultima_asistencia = Asistencia.objects.order_by(
        '-fecha_hora'
    ).first()

    contexto = {
        'total_estudiantes': total_estudiantes,
        'total_huellas': total_huellas,
        'asistencias_hoy': asistencias_hoy,
        'ultima_asistencia': ultima_asistencia
    }

    return render(
        request,
        'core/dashboard.html',
        contexto
    )

def estudiantes(request):

    estudiantes = Estudiante.objects.all().order_by('nombre')

    return render(
        request,
        'core/estudiantes.html',
        {
            'estudiantes': estudiantes
        }
    )