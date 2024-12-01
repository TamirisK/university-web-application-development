from rest_framework.throttling import UserRateThrottle

class PremiumUserRateThrottle(UserRateThrottle):
    rate = '1000/hour'

    def get_cache_key(self, request, view):
        if request.user.groups.filter(name='Premium').exists():
            return None
        return super().get_cache_key(request, view)