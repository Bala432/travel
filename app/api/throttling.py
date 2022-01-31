from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class AttractionListThrottle(UserRateThrottle):
    scope = 'attraction-list'
    
class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'