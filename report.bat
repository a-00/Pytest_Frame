@echo off

:: 设置报告路径
set REPORT_PATH=.\report

:: 打开命令行窗口并执行allure open命令
start cmd /k "allure open %REPORT_PATH%"
