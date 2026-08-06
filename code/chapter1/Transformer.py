'''
Date: 2026-06-17 16:16:22
LastEditors: liuzhengliang
LastEditTime: 2026-07-30 16:07:54
Description: 模拟实现transformer架构
'''
import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    """位置编码模块"""
    def forward(self,x):
        pass


class MultiHeadAttention(nn.Module):
    """多头注意力机制模块
    """
    def __init__(self,d_model,num_heads) -> None:
        super(MultiHeadAttention,self).__init__()
        assert d_model % num_heads == 0,"d_model 必须能被 num_heads 整除"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        # 定义 Q, K, V 和输出的线性变换层
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self,query,key,value,mask):
        pass


class PositionWiseFeedForward(nn.Module):
    """位置前馈网络模块
    """
    def forward(self, x):
        pass


# 编码器核心层

class EncoderLayer(nn.Module):
    def __init__(self,d_model,num_heads,d_ff,dropout) -> None:
        super(EncoderLayer,self).__init__()
        self.self_attn = MultiHeadAttention()
        self.feed_forward = PositionWiseFeedForward()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self,x,mask):
        # 残差链接与层归一化将在后续讲解
        # 1. 多头自注意力
        attn_output = self.self_attn(x,x,x,mask)
        x = self.norm1(x+self.dropout(attn_output))

        # 2. 前馈网络
        ff_output = self.feed_forward(x)
        x = self.norm2(x+self.dropout(ff_output))
        
        return x


# 解码器核心

class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout) -> None:
        super(DecoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention() # 待实现
        self.cross_attn = MultiHeadAttention() # 待实现
        self.feed_forward = PositionWiseFeedForward() # 待实现
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, encoder_output, src_mask, tgt_mask):
        # 1. 掩码多头自注意力 (对自己)
        attn_output = self.self_attn(x, x, x, tgt_mask)
        x = self.norm1(x + self.dropout(attn_output))

        # 2. 交叉注意力 (对编码器输出)
        cross_attn_output = self.cross_attn(x, encoder_output, encoder_output, src_mask)
        x = self.norm2(x + self.dropout(cross_attn_output))

        # 3. 前馈网络
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))

        return x