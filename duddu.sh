# after creating file as filename.sh -->run chmod u+x filename.sh

clear
cd /home/venkatesh/nfmain
. bin/activate
cd /home/venkatesh/duddu/duddu
python manage.py runserver 0.0.0.0:8030
