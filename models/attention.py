import torch
import torch.nn as nn
import torch.nn.functional as F
from models import common


class NonLocalAttention(nn.Module):
    def __init__(self, channel=128, reduction=2, ksize=1, scale=3, stride=1, softmax_scale=10, average=True,
                 res_scale=1, conv=common.default_conv):
        super(NonLocalAttention, self).__init__()
        self.res_scale = res_scale
        self.conv_match1 = common.BasicBlock(conv, channel, channel // reduction, 1, bn=False, act=nn.PReLU()).cuda()
        self.conv_match2 = common.BasicBlock(conv, channel, channel // reduction, 1, bn=False, act=nn.PReLU()).cuda()
        self.conv_assembly = common.BasicBlock(conv, channel, channel, 1, bn=False, act=nn.PReLU()).cuda()

    def forward(self, input):
        x_embed_1 = self.conv_match1(input)
        x_embed_2 = self.conv_match2(input)
        x_assembly = self.conv_assembly(input)

        N, C, H, W = x_embed_1.shape
        x_embed_1 = x_embed_1.permute(0, 2, 3, 1).view((N, H * W, C))
        x_embed_2 = x_embed_2.view(N, C, H * W)
        score = torch.matmul(x_embed_1, x_embed_2)  # (N, H*W, H*W)
        score = F.softmax(score, dim=2)
        x_assembly = x_assembly.view(N, -1, H * W).permute(0, 2, 1)   # (N, H*W, -1)(N, H*W, 2C)
        x_final = torch.matmul(score, x_assembly)  # (N, H*W, -1)
        return x_final.permute(0, 2, 1).view(N, -1, H, W) + self.res_scale * input
