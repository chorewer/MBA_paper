# MBA_paper

langchain 构建的 RAG 程序

## 项目结构

<!-- ├─ └─ │ -->

```md
.
├── connector # 连接器
│ ├── llm # 大模型
│ └── vector # 向量存储库
├── example.env 示例环境
└── README.md # 本文件
```

## 项目启动

1. 复制根目录 example.env 中的信息到新建的.env 下，并将 dashscope_api 修改为自己的 api-key
2. 在 connector/llm/model_config.py 当中，检查个人的 qwen 模型配置
