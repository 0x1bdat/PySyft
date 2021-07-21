# stdlib
import uuid

# relative
# syft relative
from ..tensor import AutogradTensor
from .op import Op


class InvertOp(Op):
    def forward(self, x: AutogradTensor) -> AutogradTensor:
        self.x = x

    def _backward(self, grad: AutogradTensor, backprop_id: uuid.UUID):
        if self.x.requires_grad:
            pass
