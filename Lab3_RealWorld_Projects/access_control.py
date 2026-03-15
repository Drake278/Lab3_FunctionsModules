import functools

def compute_access_level(control, favorite_artist):
    """
    Computes access level based on CONTROL_NUM and artist length.
    Formula: access_level = CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    """
    return (control * 3) + len(favorite_artist)

def validate_access(level, control):
    """
    Compares access level against threshold.
    Threshold: CONTROL_NUM * 5
    """
    threshold = control * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"



def audit_log(func):
    """
    A decorator that logs the start and completion of the authorization.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n[LOG] Authorization Started")
        result = func(*args, **kwargs)
        print("[LOG] Authorization Completed")
        return result
    return wrapper


@audit_log
def signal_shutdown(power):
    """
    Recursively decrements signal strength until it reaches 0.
    """
    # Print current signal strength
    print(f"Current Signal Strength: {power}")
    
    # Base Case: stop when power is 0
    if power == 0:
        return 0
    
    # Recursive Case: call itself with power - 1
    # We add 1 to count the current call
    return 1 + signal_shutdown(power - 1)