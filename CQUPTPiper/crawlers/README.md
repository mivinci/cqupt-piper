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

so, **Read all the comments in each Python file under this directory before you start writing any code. Read them goddamn carefully**

If you need to import, import from `CQUPTPiper`, **try not to import by relative path**.