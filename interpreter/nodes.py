from dataclasses import dataclass


@dataclass
class CharacterNode:
    value: str

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AndNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}&&{self.node_b})"


@dataclass
class OrNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}||{self.node_b})"


@dataclass
class NegationNode:
    node: any

    def __repr__(self):
        return f"(~{self.node})"


@dataclass
class ExclusiveOrNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"


@dataclass
class ImplicationNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-->{self.node_b})"


@dataclass
class BiConditionalNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}<-->{self.node_b})"


@dataclass
class EquivalenceNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}=={self.node_b})"


@dataclass
class ForAllNode:
    node: any

    def __repr__(self):
        return f"(forall{self.node})"


@dataclass
class ExistsNode:
    node: any

    def __repr__(self):
        return f"(exists{self.node})"
