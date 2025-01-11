class MixinPrint:
    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        values = []
        for key, value in self.__dict__.items():
            if value is not None:
                values.append(repr(value))
        return f"{self.__class__.__name__}({', '.join(values)})"
