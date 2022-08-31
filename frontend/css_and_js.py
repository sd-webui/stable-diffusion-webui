from os import path


def readTextFile(*args):
    dir = path.dirname(__file__)
    entry = path.join(dir, *args)
    with open(entry, "r", encoding="utf8") as f:
        data = f.read()
    return data


def css(opt):
    styling = readTextFile("css", "styles.css")
    if not opt.no_progressbar_hiding:
        styling += readTextFile("css", "no_progress_bar.css")
    return styling


def js(opt):
    data = readTextFile("js", "index.js")
    data = "(z) => {" + data + "; return z ?? [] }"
    return data


# Wrap the typical SD method call into async closure for ease of use
# Supplies the js function with a params object
# That includes all the passed arguments and input from Gradio: x
def call_SD(sd_method, **kwargs):
    if "x" not in kwargs.keys():
        kwargs["x"] = "x"
    params = "{" + ",".join(f"{k}:{v}" for k, v in kwargs.items()) + "}"
    return f"async (x) => {{ return await SD.{sd_method}({params}) ?? []; }}"
