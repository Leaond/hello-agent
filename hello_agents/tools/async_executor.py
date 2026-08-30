"""异步工具执行器"""

import asyncio
import  concurrent.futures
from typing import Dict
from .registry import ToolRegistry

class AsyncToolExecutor:
    """异步工具执行器"""

    def __init__(self,registry: ToolRegistry,max_workers:int = 4):
        self.registry = registry
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers)