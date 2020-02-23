def hello(name = None, **kwargs):
    if name:
        name = name.lower()
        name = name.capitalize()
        return "Hello, " + name + "!"
    else:
        return "Hello, World!"
