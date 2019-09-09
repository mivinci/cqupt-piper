from CQUPTPiper.cli import SubCommand


if __name__ == "__main__":
    subcmd = SubCommand("This is subcommand test", "0.0.1")
    group = subcmd.add_group("get")
    group.add_argument("photo", "-p", "crawl photo of student", argname='学号', type=int)
    group.add_argument("credit", "-c", "crawl credit of a school-year", argname='年份', type=int)

    # print(subcmd.commands)

    # args = subcmd.parse("get -c 2019")

    print(subcmd.print_help())
