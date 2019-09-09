"""
This package contains all the crawlers that're used in CQUPTPiper.
If jwzx.cqupt.edu.cn changes, those crawlers will be no longer used,
new crawlers must be constructed in time.

So far, crawlers are able to get:
    credit,
    fee of each year,
    gpa and ranks of each year,
    tasks of current semester,
    photo of student by studend ID.

URL for each information are written as comments in each Python file,
but do not write the urls directly in your code, cuz all urls can be called from

    piper.urls

Plus, DO NOT edit any code outside this package.
"""
