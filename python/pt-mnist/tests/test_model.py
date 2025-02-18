import torch
from models.simple_nn import SimpleNN


def test_build():
    simple_nn = SimpleNN()
    model = simple_nn.build()

    assert isinstance(model, torch.nn.Module)
    children = list(model.children())

    # Verify the number of layers
    assert len(children) == 5  # Flatten, Linear, ReLU, Linear, Softmax

    # Verify types of layers
    assert isinstance(children[0], torch.nn.Flatten)
    assert isinstance(children[1], torch.nn.Linear)
    assert isinstance(children[2], torch.nn.ReLU)
    assert isinstance(children[3], torch.nn.Linear)
    assert isinstance(children[4], torch.nn.Softmax)

    # Verify the properties of the linear layers
    assert children[1].out_features == 128
    assert children[3].out_features == 10


if __name__ == "__main__":
    test_build()
    print("All tests passed!")
