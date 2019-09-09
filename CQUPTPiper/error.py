from CQUPTPiper.lang import Instruction, EN, CH


class Error:

    instruction: EN or CH = Instruction

    @classmethod
    def new(cls, errmsg: str) -> str:
        return errmsg

    @classmethod
    def subcommand(cls, cmd: str) -> str:
        return f"{cls.instruction.ERROR_UNRECOGNIZED_SUBCOMMAND} '{cmd}'"

    @classmethod
    def option(cls, opt: str) -> str:
        return f"{cls.instruction.ERROR_INVALID_OPTION} '{opt}'"

    @classmethod
    def argument(cls, arg: str) -> str:
        return f"{cls.instruction.ERROR_INVALID_ARGUMENT} '{arg}'"

    @classmethod
    def noption(cls) -> str:
        return cls.instruction.ERROR_NO_OPTION