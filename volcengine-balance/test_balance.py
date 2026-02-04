#!/usr/bin/env python3
"""
测试火山引擎余额查询
"""

import os
import sys
import volcenginesdkbilling
import volcenginesdkcore
from volcenginesdkcore.rest import ApiException

def get_balance():
    """查询火山引擎余额"""
    
    # 从环境变量获取 AK/SK
    access_key = os.getenv('VOLCENGINE_ACCESS_KEY')
    secret_key = os.getenv('VOLCENGINE_SECRET_KEY')
    
    if not access_key or not secret_key:
        print("错误: 需要设置 VOLCENGINE_ACCESS_KEY 和 VOLCENGINE_SECRET_KEY 环境变量")
        print("请从火山引擎控制台获取 AK/SK: https://console.volcengine.com/iam/keymanage/")
        return None
    
    try:
        # 配置 SDK
        configuration = volcenginesdkcore.Configuration()
        configuration.ak = access_key
        configuration.sk = secret_key
        configuration.region = "cn-beijing"  # 默认区域
        
        # 创建 API 客户端
        api_client = volcenginesdkcore.ApiClient(configuration)
        api_instance = volcenginesdkbilling.BILLINGApi(api_client)
        
        # 创建请求
        request = volcenginesdkbilling.QueryBalanceAcctRequest()
        
        # 调用 API
        print("正在查询火山引擎余额...")
        response = api_instance.query_balance_acct(request)
        
        return response
        
    except ApiException as e:
        print(f"API 调用失败: {e}")
        return None
    except Exception as e:
        print(f"错误: {e}")
        return None

def format_balance_response(response):
    """格式化余额响应"""
    if not response or not hasattr(response, 'result'):
        return "无法获取余额信息"
    
    result = response.result
    output = []
    
    output.append("💰 火山引擎余额")
    
    # 提取余额信息
    if hasattr(result, 'available_balance'):
        output.append(f"- 可用余额: {result.available_balance} CNY")
    
    if hasattr(result, 'cash_balance'):
        output.append(f"- 现金余额: {result.cash_balance} CNY")
    
    if hasattr(result, 'freeze_balance'):
        output.append(f"- 冻结金额: {result.freeze_balance} CNY")
    
    if hasattr(result, 'credit_limit'):
        output.append(f"- 信控额度: {result.credit_limit} CNY")
    
    if hasattr(result, 'arrear_balance'):
        output.append(f"- 欠费金额: {result.arrear_balance} CNY")
    
    if hasattr(result, 'account_status'):
        status = result.account_status
        status_text = "正常 ✅" if status == "normal" else f"{status} ⚠️"
        output.append(f"- 账户状态: {status_text}")
    
    return "\n".join(output)

if __name__ == "__main__":
    # 测试环境变量
    print("检查环境变量...")
    print(f"VOLCENGINE_ACCESS_KEY: {'已设置' if os.getenv('VOLCENGINE_ACCESS_KEY') else '未设置'}")
    print(f"VOLCENGINE_SECRET_KEY: {'已设置' if os.getenv('VOLCENGINE_SECRET_KEY') else '未设置'}")
    
    # 如果没有 AK/SK，尝试使用配置中的 API Key
    if not os.getenv('VOLCENGINE_ACCESS_KEY'):
        print("\n尝试从 OpenClaw 配置中获取 API Key...")
        # 这里可以添加从 openclaw.json 读取配置的逻辑
        
    print("\n" + "="*50)
    
    # 查询余额
    response = get_balance()
    
    if response:
        formatted = format_balance_response(response)
        print(formatted)
        
        # 打印原始响应用于调试
        print("\n" + "="*50)
        print("原始响应:")
        print(response)
    else:
        print("查询失败")