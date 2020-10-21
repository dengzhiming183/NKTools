# NKTools
Some tools for NK OA

## Tool list
- weekly_report 周报定时提交

## Usage
1. fork本项目
2. 点击项目中 Seeting->Secrets->New Secrets 添加参数

- weekly_report 参数列表

| Key | Remark |
|:-:|:-:|
| OA_USERNAME | OA登录用户名 |
| OA_PASSWORD | OA登录密码 |
| OA_IS_SUBMIT | 是否提交(true/false) |
| MAIL_USERNAME | 发件人用户名 |
| MAIL_PASSWORD | 发件人密码 |
| MAIL_RECEIVER | 收件人邮箱 |

3. 点击项目中 Actions->Workflow->Run workflow