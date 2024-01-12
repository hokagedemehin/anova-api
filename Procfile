web: gunicorn anova_backend.wsgi
# release: python manage.py makemigrations --noinput
# release: python manage.py collectstatic --noinput
release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
