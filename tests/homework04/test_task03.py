from homework04.task03 import my_precious_logger


def test_stdout_output(capsys):
    text = "OK"
    my_precious_logger(text)
    assert capsys.readouterr().out == text


def test_stderr_output(capsys):
    text = "error: file not found"
    my_precious_logger(text)
    assert capsys.readouterr().err == text
