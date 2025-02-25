from rest_framework.throttling import UserRateThrottle

# custom throttling
class WordCreateThrottle(UserRateThrottle):
    scope = 'word-create'

class WordUpdateThrottle(UserRateThrottle):
    scope = 'word-update'

class WordDeleteThrottle(UserRateThrottle):
    scope = 'word-delete'

class ThemeCreateThrottle(UserRateThrottle):
    scope = 'theme-create'

class ThemeUpdateThrottle(UserRateThrottle):
    scope = 'theme-update'

class ThemeDeleteThrottle(UserRateThrottle):
    scope = 'theme-delete'

