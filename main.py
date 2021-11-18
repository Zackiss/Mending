import ast
import inspect
from functools import wraps


class Butler(object):
    def __init__(self):
        self.catalogs = {}

    def catalog(self, catalog: str):
        catalog_name = catalog
        print(self.catalogs[catalog_name])

    def register(self, catalog: str, times: int, _license: any, func):
        catalog_name = catalog
        try:
            if times != 0:
                if self.catalogs[catalog_name]:
                    self.catalogs[catalog_name].append([times, _license, func])
                else:
                    self.catalogs[catalog_name] = [[times, _license, func]]
            else:
                raise ValueError('Unexpected times given: 0')
            if times < -1:
                raise ValueError('Unexpected times given: {0}'.format(times))
        except KeyError:
            self.catalogs[catalog_name] = [[times, _license, func]]

    def exist(self, catalog: str):
        catalog_name = catalog
        if self.catalogs[catalog_name]:
            return True

    class NodeVisitor(ast.NodeVisitor):
        def __init__(self):
            self.result = []

        def visit_FunctionDef(self, node):
            for nodes in node.decorator_list:
                if isinstance(nodes, ast.Call):
                    name = nodes.func.attr if isinstance(nodes.func, ast.Attribute) else nodes.func.id
                    catalog_name = nodes.keywords[0].value.value
                    self.result.append([name, catalog_name])
                else:
                    name = nodes.attr if isinstance(nodes, ast.Attribute) else nodes.id
                    catalog_name = nodes.keywords[0].value.value
                    self.result.append([name, catalog_name])
            self.generic_visit(node)

    def get(self, func):
        _source = inspect.getsource(func)
        _node = ast.parse(_source)
        visitor = self.NodeVisitor()
        visitor.visit(_node)
        return {'catalog_name': visitor.result[0][1],
                'available_license': [_[1] for _ in self.catalogs[visitor.result[0][1]]]}


class Queue(object):
    def __init__(self, Butler_: object):
        self.Butler_ = Butler_

    def print(self, catalog: str):
        catalog_name = catalog
        try:
            queue = self.Butler_.catalogs[catalog_name]
        except KeyError:
            raise KeyError['Catalog {0} not found'.format(catalog_name)]
        index = 1
        print('\t')
        for datas in [{'times_left': _[0], 'license': _[1], 'function_name': _[2].__name__} for _ in queue]:
            print(str(index)+'. '+catalog_name+':')
            for key, value in datas.items():
                print('\t', str(key)+": "+str(value))
            index += 1
        print('\t')

    def get(self, catalog: str):
        catalog_name = catalog
        try:
            queue = self.Butler_.catalogs[catalog_name]
        except KeyError:
            raise KeyError['Catalog {0} not found'.format(catalog_name)]
        return [{'times_left': _[0], 'license': _[1], 'function_name': _[2].__name__} for _ in queue]

    def append(self, catalog: str, event: list):
        catalog_name = catalog
        try:
            if len(event) == 3:
                if type(event[0]) == int:
                    if inspect.isfunction(event[2]):
                        self.Butler_.catalogs[catalog_name].append(event)
                    else:
                        raise TypeError['{0} is not a function'.format(str(event[2]))]
                else:
                    raise TypeError['Type for "times" not match: {0} given, int required'.format(str(type(event[0])))]
            else:
                raise ValueError['Given list should have 3 variables']
        except KeyError:
            raise KeyError['Catalog {0} not found'.format(catalog_name)]

    def len(self, catalog: str):
        catalog_name = catalog
        return len(self.Butler_.catalogs[catalog_name])

    def pop(self, catalog: str, index: int):
        catalog_name = catalog
        self.Butler_.catalogs[catalog_name].pop(index)

    def replace(self, catalog: str, event: list, index: int):
        catalog_name = catalog
        try:
            if len(event) == 3:
                if type(event[0]) == int:
                    if inspect.isfunction(event[2]):
                        if index == 0:
                            self.Butler_.catalogs[catalog_name].pop(0)
                            self.Butler_.catalogs[catalog_name] = [event] + self.Butler_.catalogs[catalog_name]
                        elif index == len(self.Butler_.catalogs[catalog_name]) - 1 and index > 0:
                            self.Butler_.catalogs[catalog_name].pop(len(self.Butler_.catalogs[catalog_name]) - 1)
                            self.Butler_.catalogs[catalog_name].append(event)
                        else:
                            self.Butler_.catalogs[catalog_name] = self.Butler_.catalogs[catalog_name][0:index] + \
                                                                  [event] + \
                                                                  self.Butler_.catalogs[catalog_name][index + 1:]
                    else:
                        raise TypeError['{0} is not a function'.format(str(event[2]))]
                else:
                    raise TypeError['Type for "times" not match: {0} given, int required'.format(str(type(event[0])))]
            else:
                raise ValueError['Given list should have 3 variables']
        except KeyError:
            raise KeyError['Catalog {0} not found'.format(catalog_name)]

    def clear(self, catalog: str):
        catalog_name = catalog
        self.Butler_.catalogs[catalog_name] = []
        pass


class Overwrite(object):
    def __init__(self):
        self.Butler = Butler()
        self.Queue = Queue(self.Butler)
        self._license = None

    def entrance(self, catalog):
        catalog_name = catalog

        def coat(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if self.Butler.exist(catalog_name):
                    _ = -1
                    while _ < (len(self.Butler.catalogs[catalog_name]) - 1):
                        _ += 1
                        if self.Butler.catalogs[catalog_name][_][1] == self._license:
                            self.Butler.catalogs[catalog_name][_][2]()
                            if self.Butler.catalogs[catalog_name][_][0] == -1:
                                break
                            else:
                                if self.Butler.catalogs[catalog_name][_][0] > 1:
                                    self.Butler.catalogs[catalog_name][_][0] -= 1
                                    break
                                else:
                                    self.Butler.catalogs[catalog_name].pop(_)
                                    break
                    else:
                        func(*args, **kwargs)
                else:
                    func(*args, **kwargs)

            return wrapper

        return coat

    def claim(self, user_operating: list):
        self._license = user_operating
