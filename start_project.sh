cd ~/
git clone https://github.com/sreenuvasulup/Residants.git Residants
virtualenv env
sleep 2
pip install Django==1.11
cd Residants
python manage.py runserver
