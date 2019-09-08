```
  _____  _____  _     _ ______ _______    ______ _
 / ____|/ ___ \| |   | |  __  \__   __|  |  __  (_)
| |    | |   | | |   | | |__| |  | |     | |__| |_ ____    ___ _ __
| |    | |  _| | |   | |  ____/  | |     |  ____/ |  __ \ / _ \ '__\
| |___ | |__\  | |___| | |       | |     | |    | | |__| |  __/ |
 \____/ \____/\_\_____/|_|       |_|     |_|    |_|  ___/ \___|_|
                                                  |_|
```

![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-blue) ![](https://img.shields.io/badge/Python-3%2B-yellowgreen)

🤯 CQUPT Piper is a command line tool to get info from [jwzx.cqupt.edu.cn](jwzx.cqupt.edu.cn). (Wired On)

[简体中文](https://github.com/Mivinci/cqupt-piper/blob/master/README_ZH.md)

## Installation

```bash
pip install CQUPTPiper
```

## Usage

Just run:

```bash
piper
```

And you will go through an authorization if it is the first time you use it.

Then you will see something like a shell for you to input your commands.

### Get Scripts

##### Get your photo

```bash
> get photo
```

##### Get the photo of other students

```bash
> get photo 2017213056
```

##### Get the credit obained till now

```bash
> get credit
```

##### Get the credit of a school-year

```bash
> get credit 2018
```

##### Get the gpa of a school-year

```bash
> get gpa 2018
```

##### Get the tuition fee of a school-year

```bash
> get fee 2018
```

##### Get the tasks of the current semester

```bash
> get tasks
```



### Contribution

You can help create better `crawlers` under directory [crawlers](https://github.com/Mivinci/cqupt-piper/tree/master/CQUPTPiper/crawlers). 

Fork this repo and commit your request!

## Todo

- [x] **Sign in to jwzx.cqupt.edu.cn**
    - [x] Manually&Antomatically recognizing captcha

- [ ] **Get Scripts** (Waiting for ya!)

## License

© XJJ, 2019~datetime.now()

Released under the [MIT License](https://github.com/Mivinci/cqupt-piper/blob/master/LICENSE)