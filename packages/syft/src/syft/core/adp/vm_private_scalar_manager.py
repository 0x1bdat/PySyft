# future
from __future__ import annotations

# stdlib
from copy import deepcopy
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

# third party
from google.protobuf.reflection import GeneratedProtocolMessageType
import sympy as sp

# relative
from ...proto.core.adp.scalar_manager_pb2 import (
    VirtualMachinePrivateScalarManager as VirtualMachinePrivateScalarManager_PB,
)
from ...proto.core.adp.scalar_manager_pb2 import PrimeFactory as PrimeFactory_PB
from ..common.serde.deserialize import _deserialize as deserialize
from ..common.serde.serializable import serializable
from ..common.serde.serialize import _serialize as serialize
from .entity import Entity
from .scalar.gamma_scalar import GammaScalar
from ...logger import warning

@serializable()
class PrimeFactory:
    """IMPORTANT: it's very important that two tensors be able to tell that
    they are indeed referencing the EXACT same PrimeFactory. At present this is done
    by ensuring that it is literally the same python object. In the future, we will
    probaby need to formalize this. However, the main way this could go wrong is if we
    created some alternate way for checking to see if two prime factories 'sortof looked
    the same' but which in fact weren't the EXACT same object. This could lead to
    security leaks wherein two tensors think two different symbols in fact are the
    same symbol."""

    def __init__(self, prime: int = 1) -> None:
        self.prev_prime = prime

    def next(self) -> int:
        self.prev_prime = sp.nextprime(self.prev_prime)
        return self.prev_prime

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, PrimeFactory):
            return self.prev_prime == other.prev_prime
        return self == other

    def _object2proto(self) -> PrimeFactory_PB:
        return PrimeFactory_PB(prime=self.prev_prime)

    @staticmethod
    def _proto2object(
        proto: PrimeFactory_PB,
    ) -> PrimeFactory:
        return PrimeFactory(prime=proto.prime)

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        return PrimeFactory_PB


@serializable()
class VirtualMachinePrivateScalarManager:
    def __init__(
        self,
        prime_factory: Optional[PrimeFactory] = None,
        prime2symbol: Optional[Dict[Any, Any]] = None,
    ) -> None:

        self.prime_factory = (
            prime_factory if prime_factory is not None else PrimeFactory()
        )

        if prime2symbol is None:
            prime2symbol = {}

        self.prime2symbol = prime2symbol
        self.hash_cache = None

    def get_symbol(
        self,
        min_val: Union[bool, int, float],
        value: Union[bool, int, float],
        max_val: Union[bool, int, float],
        entity: Entity,
    ) -> int:
        # NOTE: this is overly conservative because it always creates a new scalar even when
        # a computationally equivalent one might exist somewhere already.

        gs = GammaScalar(
            min_val=min_val,
            value=value,
            max_val=max_val,
            entity=entity,
            prime=self.prime_factory.next(),
        )
        self.prime2symbol[gs.prime] = gs
        self.hash_cache = None
        return gs.prime

    def __hash__(self) -> int:
        if self.hash_cache is None:
            prime2symbol = frozenset(self.prime2symbol.items())
            self.hash_cache = hash(self.prime_factory.prev_prime) + hash(prime2symbol)
        return self.hash_cache

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, VirtualMachinePrivateScalarManager):
            return (
                self.prime_factory == other.prime_factory
                and self.prime2symbol == other.prime2symbol
            )
        return self == other

    @property
    def primes_allocated(self) -> list:
        return list(self.prime2symbol.keys())

    def copy(self) -> VirtualMachinePrivateScalarManager:
        return deepcopy(self)

    def _object2proto(self) -> VirtualMachinePrivateScalarManager_PB:
        return VirtualMachinePrivateScalarManager_PB(
            prime_factory=serialize(self.prime_factory),
            prime2symbol=serialize(self.prime2symbol),
        )

    @staticmethod
    def _proto2object(
        proto: VirtualMachinePrivateScalarManager_PB,
    ) -> VirtualMachinePrivateScalarManager:
        return VirtualMachinePrivateScalarManager(
            prime_factory=deserialize(proto.prime_factory),
            prime2symbol=deserialize(proto.prime2symbol),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        return VirtualMachinePrivateScalarManager_PB

    def combine_(self, vsm2: VirtualMachinePrivateScalarManager) -> None:
        """
        Combine two ScalarManagers by merging their prime factories.
        ASSUME: vsm1 is the source of truth; we won't be changing its prime numbers
        """

        if id(self.prime2symbol) != id(vsm2.prime2symbol):

            for prime_number, gs in vsm2.prime2symbol.items():
                if prime_number in self.prime2symbol:  # If there's a collision
                    new_prime = self.prime_factory.next()
                    gs.prime = new_prime
                    self.prime2symbol[new_prime] = gs
                else:
                    self.prime2symbol[gs.prime] = gs
        else:
            warning("Detected prime2symbol where two tensors were using the same dict")


