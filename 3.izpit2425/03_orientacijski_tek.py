# =============================================================================
# Orientacijski tek
#
# Na tekmovanju v orientacijskem teku imajo na voljo več tras za različne kategorije. 
# Ker si kategorije lahko delijo nekatere kontrolne točke, progo posamezne kategorije 
# označijo z zaporedjem oznak kontrolnih točk, na primer
# 
#     proga1 = ["START", "A", "B", "E", "CILJ"]
#     proga2 = ["START", "A", "C", "D", "E", "CILJ"]
# 
# 
# Sistem za čipiranje si zapisuje čas prihoda na posamezne kontrolne točke 
# glede na začetek tekmovanja.
# 
# Tek tekmovalca je predstavljen s seznamom oblike `(točka, čas)`. Seznam
# 
#     [("START", 16), ("A", 19), ("B", 22), ("E", 25), ("CILJ", 26)]
# 
# predstavlja tek, kjer je tekmovalec startal 16 minut po začetku tekmovanja,
# po treh minutah našel točko `A` in tekmovanje zaključil v 10 minutah.
# =====================================================================@043026=
# 1. podnaloga
# Tekmovalčev tek je veljaven, če je podano veljavno zaporedje točk:
# 
# * začne se s točko `START` in konča s točko `CILJ`,
# * vsebuje vse točke, ki spadajo v tekmovalčevo progo,
# * vse točke, ki spadajo v tekmovalčevo progo nastopajo v pravilnem zaporedju.
# (npr. če je določeno zaporedje točk na progi `ABE`, sta `AEB` in `AEBE` neveljavni zaporedji)
# 
# Morebitne točke, ki niso del trase se ignorirajo in ne vplivajo na veljavnost teka.
# 
# Napiši funkcijo `je_veljaven(tek, proga)`, ki sprejme podatke o teku ter zaporedje točk 
# na progi in preveri, če je tekmovalčev tek veljaven.
# 
# Primeri:
# 
#     >>> je_veljaven([("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)], proga1)
#     True
#     >>> je_veljaven([("START", 0), ("A", 5), ("B", 6), ("C", 9), ("E", 10), ("CILJ", 11)], proga1)
#     True
#     >>> je_veljaven([("START", 0), ("E", 3), ("A", 5), ("B", 6), ("CILJ", 11)], proga1)
#     False
#     >>> je_veljaven([("START", 0), ("A", 5), ("B", 6), ("CILJ", 11)], proga1)
#     False
# =============================================================================
def je_veljaven(tek, proga):
    if tek[0][0] != "START" or tek[-1][0] != "CILJ":
        return False

    # vzamemo samo točke iz proge
    filtriran = [(t, c) for t, c in tek if t in proga]

    # preverimo vrstni red glede na progo
    i = 0
    for t, c in filtriran:
        if t == proga[i]:
            i += 1
            if i == len(proga):
                return True

        elif t == "START" or t == "CILJ":
            continue
        else:
            # napačen vrstni red: če pride točka iz prihodnosti prehitro
            # (npr. E pred A)
            if t in proga and proga.index(t) > i:
                continue
            if t in proga and proga.index(t) < i:
                return False

    return i == len(proga)
# =====================================================================@043027=
# 2. podnaloga
# Napiši funkcijo `zmagovalec(tekmovalci, proga)`, ki poišče indeks zmagovalca
# v seznamu tekov vseh tekmovalcev v kategoriji. Zmagovalec je tekmovalec, ki je 
# uspešno našel vse kontrolne točke svoje proge v najkrajšem času od svojega
# začetka (čas na točki `START`).
# 
# Za tabelo:
# 
#     tekmovalci = [
#         [("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)],
#         [("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)],
#         [("START", 4), ("A", 9), ("B", 10), ("E", 14), ("CILJ", 16)],
#         [("START", 6), ("B", 11), ("E", 12), ("CILJ", 14)],
#         [("START", 8), ("A", 13), ("G", 17), ("B", 19), ("E", 23), ("CILJ", 27)],
#     ]
# 
# in progo `proga1` iz primera, je zmagovalec tekmovalec z zaporedno 
# številko 1, ki je s progo opravil v 9 minutah.
# Tekmovalec s številko 3 je sicer na cilj prišel hitreje, a je zgrešil točko "A", 
# zato njegov tek ni veljaven.
# =============================================================================

# =====================================================================@044332=
# 3. podnaloga
# Napiši funkcijo `izpisi(tek, proga, datoteka)`, ki v datoteko zapiše poročilo
# tekmovalčevega teka. Vsaka vrstica naj vsebuje oznako kontrolne točke, čas
# od začetka tekmovalčevega teka ter čas od predhodne kontrolne točke, kot kaže
# primer. Če tekmovalčev tek ni veljaven, naj se v datoteko
# zapiše le niz `DQ` (disqualified).
# 
# Za tek `[("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)]` in progo
# `proga1`, naj bo datoteka:
# 
#     START:    0    0
#     A:    2    2
#     B:    4    2
#     E:    5    1
#     CILJ:    9    4
# 
# Posamezne vrednosti v vrstici naj bodo med seboj ločene s 4 presledki.
# =============================================================================






































































































# ============================================================================@
# fmt: off
"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

# isort: off
import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request
import io
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class TimeoutError(Exception):
    pass


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield

    @staticmethod
    @contextmanager
    def time_limit(timeout_seconds=1):
        from signal import SIGINT, raise_signal
        from threading import Timer

        def interrupt_main():
            raise_signal(SIGINT)

        timer = Timer(timeout_seconds, interrupt_main)
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            raise TimeoutError
        finally:
            timer.cancel()


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding="utf-8") as f:
            source = f.read()
        part_regex = re.compile(
            r"# =+@(?P<part>\d+)=\s*\n"  # beginning of header
            r"(\s*#( [^\n]*)?\n)+?"  # description
            r"\s*# =+\s*?\n"  # end of header
            r"(?P<solution>.*?)"  # solution
            r"(?=\n\s*# =+@)",  # beginning of next part
            flags=re.DOTALL | re.MULTILINE,
        )
        parts = [
            {"part": int(match.group("part")), "solution": match.group("solution")}
            for match in part_regex.finditer(source)
        ]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]["solution"] = parts[-1]["solution"].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    "part": part["part"],
                    "solution": part["solution"],
                    "valid": part["valid"],
                    "secret": [x for (x, _) in part["secret"]],
                    "feedback": json.dumps(part["feedback"]),
                }
                if "token" in part:
                    submitted_part["token"] = part["token"]
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode("utf-8")
        headers = {"Authorization": token, "content-type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response["attempts"]:
            part["feedback"] = json.loads(part["feedback"])
            updates[part["part"]] = part
        for part in old_parts:
            valid_before = part["valid"]
            part.update(updates.get(part["part"], {}))
            valid_after = part["valid"]
            if valid_before and not valid_after:
                wrong_index = response["wrong_indices"].get(str(part["part"]))
                if wrong_index is not None:
                    hint = part["secret"][wrong_index][1]
                    if hint:
                        part["feedback"].append("Namig: {}".format(hint))

    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0MzAyNiwidXNlciI6MTE0MjJ9:1wWrOn:ZyPdPDEYILbDiSdikQ67jQvBFd5DSpVjZNUYY6MqbGI"
        try:
            proga1 = ["START", "A", "B", "E", "CILJ"]
            proga2 = ["START", "A", "C", "D", "E", "CILJ"]
            tek1 = [("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)] # True
            tek2 = [("START", 0), ("G", 3), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)]   # True
            tek3 = [("START", 0), ("E", 3), ("A", 5), ("B", 6), ("CILJ", 11)]  # False
            tek4 = [("START", 0), ("G", 3), ("A", 5), ("B", 6), ("CILJ", 11)]  # False
            tek5 = [("START", 5), ("A", 7), ("C", 12), ("D", 15), ("E", 18), ("CILJ", 22)]
            tek6 = [("START", 5), ("E", 2), ("A", 7), ("C", 12), ("D", 15), ("E", 18), ("CILJ", 22)]
            tek7 = [("START", 5), ("A", 7), ("B", 8), ("C", 12), ("D", 15), ("E", 18), ("CILJ", 22)]
            tek8 = [("A", 7), ("B", 8), ("C", 12), ("D", 15), ("E", 18), ("CILJ", 22)]
            tek9 = [("START", 5), ("A", 7), ("B", 8), ("C", 12), ("D", 15), ("E", 18)]
            tek10 = [("B", 8), ("C", 12), ("D", 15), ("E", 18)]
            tek11 = [("START", 0), ("A", 5), ("B", 6), ("E", 10), ("G", 11), ("CILJ", 12)]
            
            
            Check.equal(f'je_veljaven({tek1}, {proga1})', True)
            Check.equal(f'je_veljaven({tek2}, {proga1})', True)
            Check.equal(f'je_veljaven({tek3}, {proga1})', False)
            Check.equal(f'je_veljaven({tek4}, {proga1})', False)
            Check.equal(f'je_veljaven({tek5}, {proga1})', False)
            Check.equal(f'je_veljaven({tek5}, {proga2})', True)
            Check.equal(f'je_veljaven({tek6}, {proga2})', False)
            Check.equal(f'je_veljaven({tek7}, {proga2})', True)
            Check.equal(f'je_veljaven({tek8}, {proga2})', False)
            Check.equal(f'je_veljaven({tek9}, {proga2})', False)
            Check.equal(f'je_veljaven({tek10}, {proga2})', False)
            Check.equal(f'je_veljaven({tek11}, {proga1})', True)
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0MzAyNywidXNlciI6MTE0MjJ9:1wWrOn:7eH3srlB7Scw0r7TrCBZ6DJkIHKIpVZ8Y03AcNgHfdY"
        try:
            proga1 = ["START", "A", "B", "E", "CILJ"]
            tekmovalci1 = [
                [("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)],
                [("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)],
                [("START", 4), ("A", 9), ("B", 10), ("E", 14), ("CILJ", 16)],
                [("START", 6), ("B", 11), ("E", 12), ("CILJ", 14)],
                [("START", 8), ("A", 13), ("G", 17), ("B", 19), ("E", 23), ("CILJ", 27)],
            ]
            
            Check.equal(f"zmagovalec({tekmovalci1}, {proga1})", 1)
            
            proga = ["START", "A", "B", "E", "CILJ"]
            tekmovalci1 = [
                [("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)],
                [("START", 4), ("A", 9), ("B", 10), ("E", 14), ("CILJ", 16)],
                [("START", 6), ("B", 11), ("E", 12), ("CILJ", 14)],
                [("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)],
                [("START", 8), ("A", 13), ("G", 17), ("B", 19), ("E", 23), ("CILJ", 27)],
            ]
            
            Check.equal(f"zmagovalec({tekmovalci1}, {proga1})", 3)
            
            proga3 = ['START', 'N', 'O', 'K', 'A', 'F', 'L', 'M', 'CILJ']
            tekmovalci3 = [
                [('START', 10), ('N', 17), ('O', 35), ('K', 50), ('A', 54), ('F', 68), ('L', 74), ('M', 84), ('CILJ', 99)], 
                [('START', 12), ('N', 27), ('O', 40), ('K', 46), ('A', 48), ('F', 63), ('H', 72), ('L', 91), ('M', 110), ('CILJ', 124)], 
                [('START', 14), ('N', 27), ('O', 34), ('K', 37), ('A', 56), ('F', 67), ('L', 77), ('M', 97), ('CILJ', 104)], 
                [('START', 16), ('N', 22), ('O', 31), ('C', 44), ('K', 49), ('A', 61), ('F', 76), ('L', 88), ('M', 107), ('CILJ', 108)], 
                [('START', 18), ('N', 31), ('O', 35), ('K', 49), ('A', 50), ('F', 69), ('L', 77), ('M', 94), ('CILJ', 108)]
            ]
            # [89, 112, 90, 92, 90]
            Check.equal(f"zmagovalec({tekmovalci3}, {proga3})", 0)
            
            
            
            proga4 = ['START', 'H', 'D', 'M', 'K', 'E', 'N', 'J', 'B', 'C', 'F', 'G', 'L', 'I', 'CILJ']
            tekmovalci4 = [
                [('START', 19), ('H', 29), ('D', 35), ('M', 45), ('K', 62), ('E', 73), ('N', 88), ('J', 101), ('B', 113), ('C', 131), ('F', 149), ('G', 169), ('L', 188), ('I', 205), ('CILJ', 208)], 
                [('START', 22), ('H', 33), ('D', 39), ('M', 55), ('K', 59), ('E', 66), ('E', 79), ('N', 93), ('J', 95), ('B', 99), ('C', 109), ('F', 110), ('G', 111), ('L', 129), ('I', 138), ('CILJ', 150)], 
                [('START', 25), ('H', 40), ('D', 55), ('M', 71), ('K', 90), ('E', 95), ('N', 100), ('J', 105), ('B', 121), ('C', 122), ('F', 124), ('G', 135), ('L', 136), ('I', 147), ('CILJ', 155)], 
                [('START', 28), ('H', 43), ('D', 46), ('M', 57), ('K', 76), ('E', 86), ('N', 89), ('J', 92), ('B', 96), ('C', 105), ('F', 117), ('G', 129), ('L', 138), ('I', 156), ('CILJ', 176)], 
                [('START', 31), ('H', 33), ('D', 45), ('M', 51), ('K', 64), ('E', 69), ('N', 84), ('J', 94), ('B', 96), ('C', 114), ('F', 131), ('G', 151), ('L', 164), ('I', 172), ('CILJ', 180)], 
                [('START', 34), ('H', 43), ('D', 59), ('M', 78), ('K', 89), ('E', 106), ('N', 122), ('J', 139), ('B', 159), ('C', 167), ('F', 186), ('G', 205), ('L', 213), ('I', 223), ('CILJ', 238)], 
                [('START', 37), ('H', 49), ('D', 60), ('M', 67), ('K', 75), ('E', 78), ('N', 81), ('J', 84), ('B', 95), ('C', 99), ('F', 115), ('G', 119), ('L', 132), ('I', 133), ('CILJ', 146)], 
                [('START', 40), ('H', 47), ('D', 66), ('M', 77), ('K', 86), ('E', 101), ('N', 111), ('J', 125), ('B', 139), ('C', 151), ('F', 152), ('G', 169), ('L', 176), ('I', 189), ('CILJ', 194)]
            ]
            # [189, None, 130, 148, 149, 204, 109, 154]
            Check.equal(f"zmagovalec({tekmovalci4}, {proga4})", 6)
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0NDMzMiwidXNlciI6MTE0MjJ9:1wWrOn:CrM5RjNCtj4_-xrcNBB1pzj1TEQt2-ggZ2NwEjFM_dI"
        try:
            testi = [
                ([("START", 0), ("A", 5), ("B", 6), ("E", 10), ("CILJ", 11)], ["START", "A", "B", "E", "CILJ"], ["START:    0    0", "A:    5    5", "B:    6    1", "E:    10    4", "CILJ:    11    1"]),
                ([("START", 2), ("A", 4), ("B", 6), ("E", 7), ("CILJ", 11)], ["START", "A", "B", "E", "CILJ"], ["START:    0    0", "A:    2    2", "B:    4    2", "E:    5    1", "CILJ:    9    4"]),
                ([("START", 4), ("A", 9), ("B", 10), ("E", 14), ("CILJ", 16)], ["START", "A", "B", "E", "CILJ"], ["START:    0    0", "A:    5    5", "B:    6    1", "E:    10    4", "CILJ:    12    2"]),
                ([("START", 6), ("B", 11), ("E", 12), ("CILJ", 14)], ["START", "A", "B", "E", "CILJ"], ["DQ"]),
                ([("START", 8), ("A", 13), ("G", 17), ("B", 19), ("E", 23), ("CILJ", 27)], ["START", "A", "B", "E", "CILJ"], ["START:    0    0", "A:    5    5", "G:    9    4", "B:    11    2", "E:    15    4", "CILJ:    19    4"]),
            ]
            
            for i, (tek, proga, izhod) in enumerate(testi):
                izpisi(tek, proga, f"tek{i}.txt")
                Check.out_file(f"tek{i}.txt", izhod)
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token 84e315641c6ee8a604d15f2040d401fd6de0e83b"
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print("Rešitve so shranjene.")
        update_attempts(Check.parts, response)
        if "update" in response:
            print("Updating file... ", end="")
            backup_filename = backup(filename)
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(response["update"])
            print("Previous file has been renamed to {0}.".format(backup_filename))
            print("If the file did not refresh in your editor, close and reopen it.")
    Check.summarize()


if __name__ == "__main__":
    _validate_current_file()
