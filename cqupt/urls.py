URL_BASE='http://jwzx.cqupt.edu.cn'

URL_LOGIN=f'{URL_BASE}/login.php'
URL_CAPTCHA=f'{URL_BASE}/createValidationCode.php'
URL_CHECK_LOGIN=f'{URL_BASE}/checkLogin.php'

# 各类数据在 HTML 的标签id: # 原始成绩总表: id='cjAllTab-cjzb'
# 排名和绩点: id='cjAllTab-zypm'
# 各类统考成绩: id='ui-id-5'
URL_GPA=f'{URL_BASE}/student/chengjiPm.php'

# 各类数据在 HTML 的标签id: # 学分统计表: id='AxfTjTable'
URL_CREDIT=f'{URL_BASE}/student/xkxfTj.php'

# 各类数据在 HTML 的标签id: # 学费: id='pTable'
URL_FINANCE=f'{URL_BASE}/student/jfInfo.php'

# 考试安排 #id='stuKsTab-ks'
URL_TASKS=f'{URL_BASE}/student/ksap.php'

# 学生照片 
URL_STUDENT_PHOTO=f'{URL_BASE}/showstupic.php?xh='