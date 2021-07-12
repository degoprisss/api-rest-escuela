from django.core.mail import send_mail

from school.celery import app


@app.task(name='student-email-task')
def student_email(email):
    print('Se envió el correo')
    send_mail(
        subject='De nuevo estamos probando 2',
        message='Gracias por agregar un nuevo libro',
        from_email='sistema@gmail.com',
        recipient_list=[email],
        fail_silently=False
    )
