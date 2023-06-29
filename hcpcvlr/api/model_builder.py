import torch
from torch import nn


class BaseBuilder(nn.Module):
    def __init__(self, config):
        self.super.init(BaseBuilder, self)

    def forward(self):
        pass

