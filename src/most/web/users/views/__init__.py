SUCCESS_KEY = 'success'
MESSAGE_KEY = 'message'
ERRORS_KEY = 'errors'
DATA_KEY = 'data'
TOTAL_KEY = 'total_count'


def staff_check(user):
    if user.is_staff:
        return True
    else:
        return False