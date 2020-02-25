from rest_framework.permissions import BasePermission
from datetime import datetime,date

class IsStaffOrOwner(BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        return False

class Time(BasePermission):

    def has_object_permission(self,request,view,obj):
        Deff = obj.date - date.today()
        DeffInDays = Deff.days
        if  DeffInDays >= 3 :
            return True
        return False
