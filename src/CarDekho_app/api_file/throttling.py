#************************************CUSTOM THROTTLING************************************
from rest_framework.throttling import UserRateThrottle


class ReviewDetailThrottle(UserRateThrottle):
    scope = "throttling_for_review_details"

class ReviewListThrottling(UserRateThrottle):
    scope= 'throttling_for_review_list'