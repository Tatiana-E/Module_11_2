from inspect import getmodule


def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_att = dir(obj)
    obj_meth = [method for method in obj_att if callable(getattr(obj, method))]
    obj_mod = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': obj_att, 'methods': obj_meth, 'module': obj_mod}
    return info

number_info = introspection_info(42)
print(number_info)

str_info = introspection_info('Urban')
print(str_info)

dict_info = introspection_info({'Max':12, 'Joy':24, 'Rick':38})
print(dict_info)



