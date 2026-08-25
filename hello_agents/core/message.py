'''
Date: 2026-08-19 14:14:38
LastEditors: liuzhengliang
LastEditTime: 2026-08-19 14:41:36
Description: 
'''
"""消息系统"""
from typing import Optional, Dict, Any,Literal
from datetime import datetime
from pydantic import BaseModel


# 定义消息角色的类型，限制取值
MessageRole = Literal["user","assistant","system","tool"]

class Message(BaseModel):
    """消息类
    """
    content: str
    role:MessageRole
    timestamp:Optional[datetime] = None
    metadata: Optional[Dict[str,str]] = None

    def __init__(self,content:str,role:MessageRole,**kwargs) -> None:
        super().__init__(
            content=content,
            role=role,
            timestamp=kwargs.get("timestamp",datetime.now()),
            metadata=kwargs.get("metadata",{})
        )

    def to_dict(self)->Dict[str,Any]:
        return {
            "role":self.role,
            "content":self.content
        }

    def __str__(self) -> str:
        return f"[{self.role}] {self.content}"