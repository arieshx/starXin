"""
自动变量：
$@  当前目标
$<  第一个前置条件
$?  指代比目标更新的所有前置条件
$^  指代所有前置条件
$*  指代匹配符 % 匹配的部分， 比如% 匹配 f1.txt 中的f1 ，$* 就表示 f1。
$(@D) 和 $(@F) 分别指向 $@ 的目录名和文件名。比如，$@是 src/input.c，那么$(@D) 的值为 src ，$(@F) 的值为 input.c。
$(<D) 和 $(<F) 分别指向 $< 的目录名和文件名。
自动变量手册 ： https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
"""

"""
g++ 选项：

-fPIC           如果支持这种目标机,编译器就输出位置无关目标码.适用于动态连接(dynamic linking),即使分支需要大范围 转移.

连接器选项(LINKER OPTION)
-llibrary       连接名为library的库文件
-shared	        生成一个共享目标文件，常搭配 -fPIC 使用

总体选项(Overall Option)
-o	指定输出文件，如果没有使用 -o 选项,默认的输出结果是:可执行文件为 a.out

目录选项(DIRECTORY OPTION)
-Idir	在头文件搜索路径列表中添加 dir 目录
-Ldir	在 -l 选项库文件搜索路径列表中添加 dir 目录
"""


