def make_html(element):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{element}>{func(*args, **kwargs)}</{element}>"

        return wrapper

    return decorator
