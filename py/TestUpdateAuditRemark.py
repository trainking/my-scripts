# coding: utf-8

# 检查一个项目中的所有的审核页面的“audit_remark”字段必输选项
# 有两套路径下存在审核页面：
#   - protected/views/所属类文件夹/_audit.php
#   - protected/modules/所属module文件夹/views/所属类文件夹/_audit.php
# 检查审核页面是否存在了“'required' => true,”或者“"required" => true,”

import os
import re

CLASS_PATH = r"D:\xampp\htdocs\ROS_PC"  # 项目根路径
viewsPath = CLASS_PATH + os.sep +"protected" + os.sep + "views"
modulePath = CLASS_PATH + os.sep + "protected" + os.sep + "modules"

# 所有审核页面的路径
auditPagePathList = []

# 主函数
def main():
    # step 1: viewsPath 的处理
    getViewsAuditPath(viewsPath)

    # step 2: modulePath 的处理
    moduleDir = os.listdir(modulePath)
    for item in moduleDir:
        tempViewsPath = modulePath + os.sep + item + os.sep + "views"
        if os.path.exists(tempViewsPath) and os.path.isdir(tempViewsPath):
            getViewsAuditPath(tempViewsPath)

    # step 3: 检查文件中是否存在必填选项
    pattern = re.compile(r"(\'required\' => true)|(\"required\" => true)")
    judge(pattern)
    print "is Done"


# 找出指定views目录下的所有审核页面
def getViewsAuditPath(path):
    pathList = os.listdir(path)
    for item in pathList:
        tempPath = path + os.sep + item
        if os.path.isdir(tempPath) and os.path.exists(tempPath + "\_audit.php"):
            auditPagePathList.append(tempPath + "\_audit.php")

def judge(pattern):
    for itemPath in auditPagePathList:
        reader = open(itemPath)
        line = reader.readline()
        while not line is None and not line is '':
            matchResult = pattern.findall(line)    # 使用findall可以匹配，match存在匹配不了的问题
            if not matchResult == []:
                print matchResult
                print itemPath
                reader.close()
                break
            line = reader.readline()

        reader.close

if __name__ == '__main__':
    main()
