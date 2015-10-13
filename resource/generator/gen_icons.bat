@echo off
pyrcc4 -py3 ../ExtAppIcons.qrc > ../../ui/ExtAppIcons_rc.py
python genqrc.py ../icons ../../ui/AppIcons.py
mv AppIcons.qrc ../
