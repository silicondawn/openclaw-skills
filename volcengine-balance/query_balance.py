#!/usr/bin/env python3
"""
火山引擎余额查询脚本
从 OpenClaw 配置或环境变量读取 AK/SK，查询余额信息
"""

import os
import sys
import json
import argparse
from pathlib import Path

def get_config_path():
    """获取 OpenClaw 配置文件路径"""
    home = Path.home()
    config_paths = [
        home / ".openclaw" / "openclaw.json",
        home / ".openclaw" / "clawdbot.json",
    ]
    
    for path in config_paths:
        if path.exists():
            return path
    return None

def get_credentials_from_config():
    """从 OpenClaw 配置中获取火山引擎凭证"""
    config_path = get_config_path()
    if not config_path:
        return None, None
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 尝试从 models.providers.volcengine 获取
        if 'models' in config and 'providers' in config['models']:
            providers = config['models']['providers']
            if 'volcengine' in providers:
                volcengine_config = providers['volcengine']
                # 注意：这里可能需要 AK/SK，但配置中只有 API Key
                # 对于余额查询，可能需要单独的 AK/SK 配置
                api_key = volcengine_config.get('apiKey')
                if api_key:
                    print(f"从配置中找到 API Key: {api_key[:10]}...")
                    # 注意：余额查询可能需要 AK/SK，而不是 API Key
                    # 这里返回 None 表示需要单独配置 AK/SK
                    return None, None
        
        # 尝试从 env 配置获取
        if 'env' in config:
            env_config = config['env']
            access_key = env_config.get('VOLCENGINE_ACCESS_KEY')
            secret_key = env_config.get('VOLCENGINE_SECRET_KEY')
            if access_key and secret_key:
                return access_key, secret_key
        
    except Exception as e:
        print(f"读取配置失败: {e}")
    
    return None, None

def get_credentials():
    """获取火山引擎凭证，优先从环境变量，然后从配置"""
    # 1. 从环境变量获取
    access_key = os.getenv('VOLCENGINE_ACCESS_KEY')
    secret_key = os.getenv('VOLCENGINE_SECRET_KEY')
    
    if access_key and secret_key:
        return access_key, secret_key
    
    # 2. 从 OpenClaw 配置获取
    print("环境变量未设置，尝试从 OpenClaw 配置读取...")
    config_ak, config_sk = get_credentials_from_config()
    
    if config_ak and config_sk:
        return config_ak, config_sk
    
    # 3. 检查是否有 API Key（但余额查询需要 AK/SK）
    print("警告: 余额查询需要 AccessKey ID 和 Secret Key (AK/SK)")
    print("请从火山引擎控制台获取: https://console.volcengine.com/iam/keymanage/")
    print("然后设置环境变量:")
    print("  export VOLCENGINE_ACCESS_KEY=你的AccessKey ID")
    print("  export VOLCENGINE_SECRET_KEY=你的AccessKey Secret")
    
    return None, None

def query_balance(access_key, secret_key):
    """查询火山引擎余额"""
    try:
        import volcenginesdkbilling
        import volcenginesdkcore
        from volcenginesdkcore.rest import ApiException
    except ImportError:
        print("错误: 需要安装火山引擎 Python SDK")
        print("安装命令: pip install volcengine-python-sdk")
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
        if e.status == 403:
            print("错误: 认证失败，请检查 AK/SK 是否正确")
        elif e.status == 404:
            print("错误: API 接口不存在或路径错误")
        else:
            print(f"HTTP 状态码: {e.status}")
        return None
    except Exception as e:
        print(f"错误: {e}")
        return None

def format_balance(response):
    """格式化余额响应为易读格式"""
    if not response:
        return "无法获取余额信息"
    
    # 响应可能是字典或对象
    if hasattr(response, 'to_dict'):
        result = response.to_dict()
    elif isinstance(response, dict):
        result = response
    else:
        result = response
    # 辅助函数：获取值（支持字典和对象）
    def get_val(obj, key):
        if isinstance(obj, dict):
            return obj.get(key)
        return getattr(obj, key, None)
    
    output_lines = []
    
    output_lines.append("💰 火山引擎余额")
    output_lines.append("=" * 30)
    
    # 提取余额信息
    balance_info = []
    
    # 可用余额 = (现金余额 - 冻结金额) + 信控额度 - 欠费金额
    if get_val(result, 'available_balance') is not None:
        balance_info.append(("可用余额", f"{get_val(result, 'available_balance')} CNY"))
    
    if get_val(result, 'cash_balance') is not None:
        balance_info.append(("现金余额", f"{get_val(result, 'cash_balance')} CNY"))
    
    if get_val(result, 'freeze_amount') is not None:
        balance_info.append(("冻结金额", f"{get_val(result, 'freeze_amount')} CNY"))
    
    if get_val(result, 'credit_limit') is not None:
        balance_info.append(("信控额度", f"{get_val(result, 'credit_limit')} CNY"))
    
    if get_val(result, 'arrears_balance') is not None:
        balance_info.append(("欠费金额", f"{get_val(result, 'arrears_balance')} CNY"))
    
    # 添加账户 ID
    if get_val(result, 'account_id') is not None:
        balance_info.append(("账户 ID", str(get_val(result, 'account_id'))))
    
    # 格式化输出
    max_label_len = max(len(label) for label, _ in balance_info) if balance_info else 0
    for label, value in balance_info:
        padding = " " * (max_label_len - len(label))
        output_lines.append(f"{label}:{padding} {value}")
    
    # 添加说明
    output_lines.append("")
    output_lines.append("💡 说明:")
    output_lines.append("- 可用余额 = (现金余额 - 冻结金额) + 信控额度 - 欠费金额")
    output_lines.append("- 信控额度: 火山引擎授予的信用额度")
    output_lines.append("- 欠费金额: 未支付的账单金额")
    
    return "\n".join(output_lines)

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='查询火山引擎余额')
    parser.add_argument('--verbose', '-v', action='store_true', help='显示详细信息')
    args = parser.parse_args()
    
    print("火山引擎余额查询工具")
    print("=" * 50)
    
    # 获取凭证
    access_key, secret_key = get_credentials()
    
    if not access_key or not secret_key:
        print("\n错误: 无法获取火山引擎凭证")
        print("\n配置方法:")
        print("1. 设置环境变量:")
        print("   export VOLCENGINE_ACCESS_KEY=你的AccessKey ID")
        print("   export VOLCENGINE_SECRET_KEY=你的AccessKey Secret")
        print("\n2. 或在 OpenClaw 配置文件中添加:")
        print('   "env": {')
        print('     "VOLCENGINE_ACCESS_KEY": "你的AccessKey ID",')
        print('     "VOLCENGINE_SECRET_KEY": "你的AccessKey Secret"')
        print('   }')
        print("\n获取 AK/SK: https://console.volcengine.com/iam/keymanage/")
        sys.exit(1)
    
    if args.verbose:
        print(f"使用 AccessKey: {access_key[:8]}...")
    
    # 查询余额
    response = query_balance(access_key, secret_key)
    
    if response:
        formatted = format_balance(response)
        print("\n" + formatted)
        
        if args.verbose:
            print("\n" + "=" * 50)
            print("原始响应:")
            print(response)
    else:
        print("\n查询失败，请检查网络连接和凭证是否正确")
        sys.exit(1)

if __name__ == "__main__":
    main()