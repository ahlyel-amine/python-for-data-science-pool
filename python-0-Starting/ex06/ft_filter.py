def ft_filter(function , iterable) -> filter:
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
