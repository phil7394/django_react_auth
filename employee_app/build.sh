cd frontend/emp-app
npm run build
cd ../../../
source venv/bin/activate
python manage.py collectstatic
deactivate

