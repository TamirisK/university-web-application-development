from rest_framework.permissions import BasePermission
import logging

logger = logging.getLogger(__name__)

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors to edit or delete their posts.
    All users can view posts, but only authors can modify them.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        is_author = obj.author == request.user
        if not is_author:
            logger.warning(f"Unauthorized edit attempt by {request.user} on {obj}")
        return is_author