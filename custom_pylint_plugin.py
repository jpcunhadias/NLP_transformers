import ast

import pylint.checkers
import pylint.interfaces


class FunctionNameChecker(pylint.checkers.BaseChecker):
    __implements__ = pylint.interfaces.IAstroidChecker

    name = "function-name-checker"
    priority = -1
    msgs = {
        "C9999": (
            "Function name should be lowercase and separated by underscores",
            "function-name-in-lowercase-and-underscores",
            "Function name is not in lowercase and underscore-separated",
        )
    }
    options = ()

    def visit_functiondef(self, node):
        if not node.name.islower() or "_" not in node.name:
            self.add_message("function-name-in-lowercase-and-underscores", node=node)


class VariableNameChecker(pylint.checkers.BaseChecker):
    __implements__ = pylint.interfaces.IAstroidChecker

    name = "variable-name-checker"
    priority = -1
    msgs = {
        "C9998": (
            "Variable name should be lowercase and separated by underscores",
            "variable-name-in-lowercase-and-underscores",
            "Variable name is not in lowercase and underscore-separated",
        )
    }
    options = ()

    def visit_assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                if not target.name.islower() or "_" not in target.name:
                    self.add_message(
                        "variable-name-in-lowercase-and-underscores", node=target
                    )


class LineLengthChecker(pylint.checkers.BaseChecker):
    __implements__ = pylint.interfaces.IAstroidChecker

    name = "line-length-checker"
    priority = -1
    msgs = {
        "C9997": (
            "Line length should be at most 79 characters",
            "line-length",
            "Line length is greater than 79 characters",
        )
    }
    options = ()

    def visit_astroid_module(self, node):
        for line in node.file_stream().readlines():
            if len(line.rstrip("\r\n")) > 79:
                self.add_message("line-length", line=line)


def register(linter):
    linter.register_checker(FunctionNameChecker(linter))
    linter.register_checker(VariableNameChecker(linter))
    linter.register_checker(LineLengthChecker(linter))
