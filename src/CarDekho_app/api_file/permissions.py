from rest_framework import permissions



#*****************CUSTOM PERMISSIONS****************
#*****************ADMIN OR READ_ONLY PERMISSION****************
class AdminOrReadOnlyPermission(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

#*****************REVIEW USER OR READ_ONLY PERMISSION****************
class ReviewUserOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.apiuser == request.user :
                return True
            else:
                return False