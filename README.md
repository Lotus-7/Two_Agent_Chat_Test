# 两个 Agent 对话

基于 deepseek-chat 模型，实现两个 Agent 对话（模拟心理医生和患者对话）。

## 项目结构

```txt
├── prompt/
│   ├── patient_prompt.yaml    # 患者 prompt
│   └── therapist_prompt.yaml  # 心理医生 prompt
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py.     # 模型配置
│   │   ├── therapist.py       # 心理医生 Agent
│   │   └── patient.py         # 患者 Agent
│   ├── memory/
│   │   ├── __init__.py
│   │   └── dialogue_context.py  # 对话上下文
│   └── main.py                  # 主程序
└── README.md
```

## 使用说明

确保安装 Python 和 openai 库。

```bash
pip install openai
```

### 配置

在 `src/agents/base_agent.py` 中配置你的 DeepSeek API KEY 密钥。

```python
self.client = OpenAI(
            api_key="YOUR_API_KEY",
            base_url="https://api.deepseek.com"
        )
```

### 运行

```bash
python src/main.py
```
