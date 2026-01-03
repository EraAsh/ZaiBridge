#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
代码混淆保护模块
用于保护敏感代码不被轻易逆向分析
"""

import base64
import hashlib
import random
import string
from typing import Any, Callable


class StringObfuscator:
    """字符串混淆器"""
    
    @staticmethod
    def encode(text: str) -> str:
        """编码字符串"""
        # 使用 base64 + 简单的 XOR 混淆
        encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        # 简单的字符替换
        char_map = str.maketrans(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
            'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba9876543210-_'
        )
        return encoded.translate(char_map)
    
    @staticmethod
    def decode(encoded: str) -> str:
        """解码字符串"""
        # 反向字符替换
        char_map = str.maketrans(
            'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba9876543210-_',
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        )
        decoded = encoded.translate(char_map)
        return base64.b64decode(decoded.encode('utf-8')).decode('utf-8')


class TokenProtector:
    """Token 保护器"""
    
    @staticmethod
    def mask_token(token: str, show_chars: int = 8) -> str:
        """脱敏显示 token"""
        if not token or len(token) <= show_chars * 2:
            return token
        return f"{token[:show_chars]}...{token[-show_chars:]}"
    
    @staticmethod
    def hash_token(token: str) -> str:
        """生成 token 的哈希值用于日志记录"""
        return hashlib.sha256(token.encode('utf-8')).hexdigest()[:16]


class CodeObfuscator:
    """代码混淆器"""
    
    @staticmethod
    def generate_random_name(prefix: str = 'var') -> str:
        """生成随机变量名"""
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{prefix}_{suffix}"
    
    @staticmethod
    def obfuscate_function(func: Callable) -> Callable:
        """混淆函数（装饰器）"""
        func.__name__ = CodeObfuscator.generate_random_name('func')
        func.__doc__ = None
        return func


# 预定义的混淆字符串常量
class ObfuscatedStrings:
    """混淆的字符串常量"""
    
    # API 端点
    DISCORD_API = StringObfuscator.encode("https://discord.com/api/v9")
    ZAI_API = StringObfuscator.encode("https://zai.is")
    
    # 请求头
    AUTH_HEADER = StringObfuscator.encode("Authorization")
    CONTENT_TYPE = StringObfuscator.encode("Content-Type")
    USER_AGENT = StringObfuscator.encode("User-Agent")
    DARKKNIGHT_HEADER = StringObfuscator.encode("x-zai-darkknight")
    
    # Cookie 名称
    TOKEN_COOKIE = StringObfuscator.encode("token")
    
    @classmethod
    def get_discord_api(cls) -> str:
        return StringObfuscator.decode(cls.DISCORD_API)
    
    @classmethod
    def get_zai_api(cls) -> str:
        return StringObfuscator.decode(cls.ZAI_API)
    
    @classmethod
    def get_auth_header(cls) -> str:
        return StringObfuscator.decode(cls.AUTH_HEADER)
    
    @classmethod
    def get_content_type(cls) -> str:
        return StringObfuscator.decode(cls.CONTENT_TYPE)
    
    @classmethod
    def get_user_agent(cls) -> str:
        return StringObfuscator.decode(cls.USER_AGENT)
    
    @classmethod
    def get_darkknight_header(cls) -> str:
        return StringObfuscator.decode(cls.DARKKNIGHT_HEADER)
    
    @classmethod
    def get_token_cookie(cls) -> str:
        return StringObfuscator.decode(cls.TOKEN_COOKIE)


def protect_sensitive_data(data: Any, mask: bool = True) -> Any:
    """保护敏感数据"""
    if isinstance(data, str):
        if mask and len(data) > 16:
            return TokenProtector.mask_token(data)
        return data
    elif isinstance(data, dict):
        return {k: protect_sensitive_data(v, mask) for k, v in data.items()}
    elif isinstance(data, list):
        return [protect_sensitive_data(item, mask) for item in data]
    return data


if __name__ == '__main__':
    # 测试混淆功能
    test_string = "Hello, World!"
    encoded = StringObfuscator.encode(test_string)
    decoded = StringObfuscator.decode(encoded)
    
    print(f"原始: {test_string}")
    print(f"编码: {encoded}")
    print(f"解码: {decoded}")
    print(f"匹配: {test_string == decoded}")
    
    # 测试 token 脱敏
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    print(f"\n原始 token: {token}")
    print(f"脱敏 token: {TokenProtector.mask_token(token)}")
    print(f"哈希 token: {TokenProtector.hash_token(token)}")