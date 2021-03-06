from rest_framework.permissions import BasePermission, AllowAny
from .models import ListObject, Item, ListrUser, OneOff

#Is allowed to view list
class IsListAllowed(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, ListObject):
            guestAccess = request.META['HTTP_GUEST']
            if(guestAccess and guestAccess == 'True'):
                if(request.method == "GET" or request.method == "PATCH"):
                    return True
            if(request.user in obj.collaborators.all()):
                if(request.method == "GET" or request.method == "PATCH"):
                    return True
            return obj.owner == request.user
        return obj.owner == request.user

#Is allowed to view item details(owner of list or collaborator of list)
class IsItemDetailAllowed(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Item):
            currentList = None
            try:
                currentList = ListObject.objects.get(static_id=obj.assigned_list)
            except:
                try:
                    currentList = OneOff.objects.get(static_id=obj.assigned_list)
                except:
                    currentList = None
            if(currentList):
                guestAccess = request.META['HTTP_GUEST']
                if(guestAccess and guestAccess == 'True'):
                    return True
                else:
                    return request.user.username == currentList.owner.username or request.user in currentList.collaborators.all()
            return False
        return False


class IsItemAllowed(BasePermission):
    def has_permission(self, request, view):
        listId = request.META['HTTP_LIST_ID']
        guestAccess = request.META['HTTP_GUEST']
        if(listId):
            currentList = None
            try:
                currentList = ListObject.objects.get(static_id=listId)
            except:
                currentList = None
            if(currentList != None):
                if(guestAccess and guestAccess == 'True'):
                    if(currentList.readOnly == True and request.method == "POST"):
                        return request.user.username == currentList.owner.username
                    else:
                        return True
                else:
                    if(currentList.readOnly == True and request.method == "POST"):
                        return request.user.username == currentList.owner.username
                    else:
                        return request.user.username == currentList.owner.username or request.user in currentList.collaborators.all()

            try:
                currentList = OneOff.objects.get(static_id=listId)
            except:
                currentList = None
            if(currentList != None):
                if(guestAccess and guestAccess == 'True'):
                    return True

            return False
        return False


#Owner of Item or Owner of List item is in
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user)
        if(str(request.user.username) in str(obj.assigned_list.owner)):
            return True
        if isinstance(obj, Item):
            print(request.user)
            return obj.owner == request.user
        return obj.owner == request.user

class IsKey(BasePermission):
    def has_permission(self, request, view):
        return True
