class MixinPrint:
    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.name},"  # type: ignore[attr-defined]
            f" {self.description}, {self.price}, {self.quantity})"  # type: ignore[attr-defined]
        )
