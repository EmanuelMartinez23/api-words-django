from rest_framework import permissions

# Custom permissions
class WordUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET
        if request.method in permissions.SAFE_METHODS:
            # check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.created_by == request.user