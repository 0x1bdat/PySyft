# third party
import pytest

# syft absolute
import syft as sy


@pytest.mark.libsyft
def test_libsyft() -> None:
    hello = sy.libsyft.hello_rust()
    assert hello == "Hello Rust 🦀"
