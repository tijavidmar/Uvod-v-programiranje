# =============================================================================
# Kodiranje v bazi 64
#
# Kodiranje v bazi 64 (an. Base64 encoding) je postopek, ki se pogosto uporablja za prenos binarnih, tj., ne-tekstovinh, vsebin. Vsebino zapišemo v bitnem zapisu (tj., zapisu sestavljenemu le iz `0` in `1`), ki ga nato na podlagi kodirne table s 64 znaki zakodiramo. Privzeli bomo, da so bitni zapisi vedno dolžine, ki je deljiva z 2.
# 
# Da podani bitni zapis zakodiramo, najprej preverimo, če je njegova dolžina deljiva s 6. Če je, ga razdelimo na segmente po 6 zaporednih bitov, nato pa uporabimo spodnjo kodirno tabelo (kodirna tabela je podana v nalogi). Sicer za vsak par manjkajočih bitov do deljivosti s 6 na konec bitnega zapisa dodamo `00` in zakodiramo popravljeni zapis. Dodamo torej `00` ali `0000`.
# Na konec zakodirane vsebine za vsak par dodanih ničel nato pripnemo po en znak `=`.
# 
# \[ \texttt{000000} \rightarrow \texttt{A} \quad \texttt{010000} \rightarrow \texttt{Q} \quad \texttt{100000} \rightarrow \texttt{g} \quad \texttt{110000} \rightarrow \texttt{w} \\
# \texttt{000001} \rightarrow \texttt{B} \quad \texttt{010001} \rightarrow \texttt{R} \quad \texttt{100001} \rightarrow \texttt{h} \quad \texttt{110001} \rightarrow \texttt{x} \\
# \texttt{000010} \rightarrow \texttt{C} \quad \texttt{010010} \rightarrow \texttt{S} \quad \texttt{100010} \rightarrow \texttt{i} \quad \texttt{110010} \rightarrow \texttt{y} \\
# \texttt{000011} \rightarrow \texttt{D} \quad \texttt{010011} \rightarrow \texttt{T} \quad \texttt{100011} \rightarrow \texttt{j} \quad \texttt{110011} \rightarrow \texttt{z} \\
# \texttt{000100} \rightarrow \texttt{E} \quad \texttt{010100} \rightarrow \texttt{U} \quad \texttt{100100} \rightarrow \texttt{k} \quad \texttt{110100} \rightarrow \texttt{0} \\
# \texttt{000101} \rightarrow \texttt{F} \quad \texttt{010101} \rightarrow \texttt{V} \quad \texttt{100101} \rightarrow \texttt{l} \quad \texttt{110101} \rightarrow \texttt{1} \\
# \texttt{000110} \rightarrow \texttt{G} \quad \texttt{010110} \rightarrow \texttt{W} \quad \texttt{100110} \rightarrow \texttt{m} \quad \texttt{110110} \rightarrow \texttt{2} \\
# \texttt{000111} \rightarrow \texttt{H} \quad \texttt{010111} \rightarrow \texttt{X} \quad \texttt{100111} \rightarrow \texttt{n} \quad \texttt{110111} \rightarrow \texttt{3} \\
# \texttt{001000} \rightarrow \texttt{I} \quad \texttt{011000} \rightarrow \texttt{Y} \quad \texttt{101000} \rightarrow \texttt{o} \quad \texttt{111000} \rightarrow \texttt{4} \\
# \texttt{001001} \rightarrow \texttt{J} \quad \texttt{011001} \rightarrow \texttt{Z} \quad \texttt{101001} \rightarrow \texttt{p} \quad \texttt{111001} \rightarrow \texttt{5} \\
# \texttt{001010} \rightarrow \texttt{K} \quad \texttt{011010} \rightarrow \texttt{a} \quad \texttt{101010} \rightarrow \texttt{q} \quad \texttt{111010} \rightarrow \texttt{6} \\
# \texttt{001011} \rightarrow \texttt{L} \quad \texttt{011011} \rightarrow \texttt{b} \quad \texttt{101011} \rightarrow \texttt{r} \quad \texttt{111011} \rightarrow \texttt{7} \\
# \texttt{001100} \rightarrow \texttt{M} \quad \texttt{011100} \rightarrow \texttt{c} \quad \texttt{101100} \rightarrow \texttt{s} \quad \texttt{111100} \rightarrow \texttt{8} \\
# \texttt{001101} \rightarrow \texttt{N} \quad \texttt{011101} \rightarrow \texttt{d} \quad \texttt{101101} \rightarrow \texttt{t} \quad \texttt{111101} \rightarrow \texttt{9} \\
# \texttt{001110} \rightarrow \texttt{O} \quad \texttt{011110} \rightarrow \texttt{e} \quad \texttt{101110} \rightarrow \texttt{u} \quad \texttt{111110} \rightarrow \texttt{+} \\
# \texttt{001111} \rightarrow \texttt{P} \quad \texttt{011111} \rightarrow \texttt{f} \quad \texttt{101111} \rightarrow \texttt{v} \quad \texttt{111111} \rightarrow \texttt{/} \]
# 
# Primer: Bitni zapisi `011000100110000101111010011000010011011000110100` (ki pripada nizu `baza64`) se zakodira v niz `YmF6YTY0`.
# 
# \[
#     \underbrace{\texttt{011000}}_\texttt{Y}
#     \underbrace{\texttt{100110}}_\texttt{m}
#     \underbrace{\texttt{000101}}_\texttt{F}
#     \underbrace{\texttt{111010}}_\texttt{6}
#     \underbrace{\texttt{011000}}_\texttt{Y}
#     \underbrace{\texttt{010011}}_\texttt{T}
#     \underbrace{\texttt{011000}}_\texttt{Y}
#     \underbrace{\texttt{110100}}_\texttt{0}
# \]
# 
# Bitni zapis `01100010011000010111101001100001` (ki pripada nizu `baza`), pa se zakodira v `YmF6YQ==`, saj smo na konec zapisa morali
# dodati dva para ničel, da smo dobili bitni zapis dolžine deljive s 6, saj je bila originalna dolžina zapisa 32. Ker smo dodali dva para ničel, smo na konec zakodirane vsebine dodali še `==`.
# 
# \[
#     \rlap{
#     \phantom{\underbrace{\texttt{011000}}_{}\underbrace{\texttt{100110}}_{}\underbrace{\texttt{000101}}_{}\underbrace{\texttt{111010}}_{}\underbrace{\texttt{011000}}_{}00}
#     \overbrace{\phantom{\texttt{0000}}}^{\texttt{==}}
#     }
#     \underbrace{\texttt{011000}}_\texttt{Y}
#     \underbrace{\texttt{100110}}_\texttt{m}
#     \underbrace{\texttt{000101}}_\texttt{F}
#     \underbrace{\texttt{111010}}_\texttt{6}
#     \underbrace{\texttt{011000}}_\texttt{Y}
#     \underbrace{\texttt{010000}}_\texttt{Q}
# \]
# =====================================================================@040211=
# 1. podnaloga
# Sestavite funkcijo `pravilna_koda`, ki preveri če je podani niz pravilno zakodiran
# v bazi 64, tj., da vsebuje pravilne znake in da je morebiti ustrezno dopolnjen z `=`.
# 
#     >>> pravilna_koda('YmF6YTY0')
#     True
#     >>> pravilna_koda('YmF6YTY0===')
#     False
#     >>> pravilna_koda('--++')
#     False
# =============================================================================
kodirna_tabela = {
    '000000': 'A', '010000': 'Q', '100000': 'g', '110000': 'w', 
    '000001': 'B', '010001': 'R', '100001': 'h', '110001': 'x', 
    '000010': 'C', '010010': 'S', '100010': 'i', '110010': 'y', 
    '000011': 'D', '010011': 'T', '100011': 'j', '110011': 'z', 
    '000100': 'E', '010100': 'U', '100100': 'k', '110100': '0', 
    '000101': 'F', '010101': 'V', '100101': 'l', '110101': '1', 
    '000110': 'G', '010110': 'W', '100110': 'm', '110110': '2', 
    '000111': 'H', '010111': 'X', '100111': 'n', '110111': '3', 
    '001000': 'I', '011000': 'Y', '101000': 'o', '111000': '4', 
    '001001': 'J', '011001': 'Z', '101001': 'p', '111001': '5', 
    '001010': 'K', '011010': 'a', '101010': 'q', '111010': '6', 
    '001011': 'L', '011011': 'b', '101011': 'r', '111011': '7', 
    '001100': 'M', '011100': 'c', '101100': 's', '111100': '8', 
    '001101': 'N', '011101': 'd', '101101': 't', '111101': '9', 
    '001110': 'O', '011110': 'e', '101110': 'u', '111110': '+', 
    '001111': 'P', '011111': 'f', '101111': 'v', '111111': '/',
}

def pravilna_koda(niz):
    veljavni = set(kodirna_tabela.values())
    # preštej '=' na koncu
    enacaji = 0
    while niz.endswith("="):
        enacaji += 1
        niz = niz[:-1]
    if enacaji > 2:
        return False
    # v preostanku ne sme biti '='
    if "=" in niz:
        return False
    # vsi ostali znaki morajo biti veljavni
    for znak in niz:
        if znak not in veljavni:
            return False
    return True    
# =====================================================================@040212=
# 2. podnaloga
# Sestavite funkcijo `zakodiraj`, ki sprejme bitni zapis (kot niz) in ga zakodira v bazi 64.
# 
#     >>> zakodiraj('000000')
#     'A'
#     >>> zakodiraj('011000100110000101111010011000010011011000110100')
#     'YmF6YTY0'
#     >>> zakodiraj('01100010011000010111101001100001')
#     'YmF6YQ=='
# =============================================================================
def zakodiraj(bitni_zapis):
    dodani_pari = 0
    if len(bitni_zapis) % 6 == 4:
        bitni_zapis += "00"
        dodani_pari = 1
    elif len(bitni_zapis) % 6 == 2:
        bitni_zapis += "0000"
        dodani_pari = 2
    rezultat = ""
    for i in range(0, len(bitni_zapis), 6):
        blok = bitni_zapis[i:i + 6]
        rezultat += kodirna_tabela[blok]
    rezultat += "=" * dodani_pari
    return rezultat
# =====================================================================@040213=
# 3. podnaloga
# Sestavite funkcijo `odkodiraj`, ki sprejme niz zakodiran v bazi 64 in ga odkodira v bitni zapis (kot niz). Privzamete lahko, da je zakodirani niz veljaven.
# 
#     >>> odkodiraj('A')
#     '000000'
#     >>> odkodiraj('YmF6YTY0')
#     '011000100110000101111010011000010011011000110100'
#     >>> odkodiraj('YmF6YQ==')
#     '01100010011000010111101001100001'
# =============================================================================
def odkodiraj(niz):
    st_enacajev = niz.count("=")

    niz = niz.rstrip("=")

    rezultat = ""

    for znak in niz:
        for biti, crka in kodirna_tabela.items():
            if crka == znak:
                rezultat += biti
                break

    if st_enacajev > 0:
        rezultat = rezultat[:-2 * st_enacajev]

    return rezultat





































































































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
        ] = "eyJwYXJ0Ijo0MDIxMSwidXNlciI6MTE0MjJ9:1wWE7D:c60oBbSLtzaMngHHoEf6U49SYpfJ9VUr2_hzQqg2g3o"
        try:
            kodirna_tabela = {
                '000000': 'A', '010000': 'Q', '100000': 'g', '110000': 'w', 
                '000001': 'B', '010001': 'R', '100001': 'h', '110001': 'x', 
                '000010': 'C', '010010': 'S', '100010': 'i', '110010': 'y', 
                '000011': 'D', '010011': 'T', '100011': 'j', '110011': 'z', 
                '000100': 'E', '010100': 'U', '100100': 'k', '110100': '0', 
                '000101': 'F', '010101': 'V', '100101': 'l', '110101': '1', 
                '000110': 'G', '010110': 'W', '100110': 'm', '110110': '2', 
                '000111': 'H', '010111': 'X', '100111': 'n', '110111': '3', 
                '001000': 'I', '011000': 'Y', '101000': 'o', '111000': '4', 
                '001001': 'J', '011001': 'Z', '101001': 'p', '111001': '5', 
                '001010': 'K', '011010': 'a', '101010': 'q', '111010': '6', 
                '001011': 'L', '011011': 'b', '101011': 'r', '111011': '7', 
                '001100': 'M', '011100': 'c', '101100': 's', '111100': '8', 
                '001101': 'N', '011101': 'd', '101101': 't', '111101': '9', 
                '001110': 'O', '011110': 'e', '101110': 'u', '111110': '+', 
                '001111': 'P', '011111': 'f', '101111': 'v', '111111': '/',
            }
            
            tests = [
                ('YmF6YTY0', True),
                ('YmF6YTY0===', False),
                ('YmF6YQ==', True),
                ('YmF6', True),
                ('YmF6=', True),
                ('YmF6==', True),
                ('YmF6YQ===', False),
                ('YmF==6YQ', False),
                ('===', False),
                ('čšž', False),
                ('+++', True),
                ('//==', True),
                ('--++', False)
            ]
            
            for s, r in tests:
                if not Check.equal(f'pravilna_koda({repr(s)})', r,  env={'kodirna_tabela': kodirna_tabela}):
                    break
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
        ] = "eyJwYXJ0Ijo0MDIxMiwidXNlciI6MTE0MjJ9:1wWE7D:fn5A6tD-tyGHvBfydMKBUm4ocGkyRVFz4UeamcWsokA"
        try:
            testi = [
                ('000000', 'A'),
                ('011000100110000101111010011000010011011000110100', 'YmF6YTY0'),
                ('01100010011000010111101001100001', 'YmF6YQ=='),
                ('011000100110000101111010', 'YmF6'),
                ('0110001001100001011110100110000100110110', 'YmF6YTY='),
                ('0111000001110010011001010110010001100001011101000110111101110010', 'cHJlZGF0b3I='),
                ('0110010001110010011010010110110001101100', 'ZHJpbGw='),
                ('01110010011001010110110001101001011001010111011001100101', 'cmVsaWV2ZQ=='),
                ('0110001101101111011011110111000001100101011100100110000101110100011010010111011001100101', 'Y29vcGVyYXRpdmU='),
                ('0110110101101111011101010111001001101110011010010110111001100111', 'bW91cm5pbmc='),
                ('011001000110111101101100011011000110000101110010', 'ZG9sbGFy'),
                ('01110110011010010110110001101100011000010110011101100101', 'dmlsbGFnZQ=='),
                ('01110111011000010110100101110100', 'd2FpdA=='),
                ('0110001101101000011000010111001001101001011100110110110101100001011101000110100101100011', 'Y2hhcmlzbWF0aWM='),
                ('0110101001110101011001000110011101100101', 'anVkZ2U='),
                ('011001010111100001100011011001010110010101100100', 'ZXhjZWVk'),
                ('01101100011001010110000101101011', 'bGVhaw=='),
                ('0111001101110101011100100111000001110010011010010111001101100101', 'c3VycHJpc2U='),
                ('011001000110111101100011011101000110111101110010', 'ZG9jdG9y'),
                ('01110111011000010111001001101101', 'd2FybQ=='),
                ('011100110110100101110100', 'c2l0'),
                ('011100000110110001100001011110010110010101110010', 'cGxheWVy'),
                ('01110010011001010110111001110100', 'cmVudA=='),
                ('011000100110000101101110011010010111001101101000', 'YmFuaXNo'),
                ('0110010101101100011000100110111101110111', 'ZWxib3c='),
                ('011100000111001001100001011010010111001101100101', 'cHJhaXNl'),
                ('0110001001110101011010010110110001100100', 'YnVpbGQ='),
                ('011100000110111101110111011001000110010101110010', 'cG93ZGVy'),
                ('0111001101110100011100100110100101110000', 'c3RyaXA='),
                ('011001010111100001100011011101010111001101100101', 'ZXhjdXNl'),
                ('0111001101101110011000010111001001101100', 'c25hcmw='),
                ('01110010011000010111010001100101', 'cmF0ZQ=='),
                ('011001010111001101110100011000010111010001100101', 'ZXN0YXRl'),
                ('011100000111010101101110011010010111001101101000', 'cHVuaXNo'),
                ('011101000111011101101001011101000110001101101000', 'dHdpdGNo'),
                ('011000100111001001100101011000010110101101100110011000010111001101110100', 'YnJlYWtmYXN0'),
                ('011000100111010101100010011000100110110001100101', 'YnViYmxl'),
                ('01101110011011110111010001100101', 'bm90ZQ=='),
                ('01101000011010010111001101110100011011110111001001111001', 'aGlzdG9yeQ=='),
                ('01100011011000010111001101100101', 'Y2FzZQ=='),
                ('01110111011000010110110001101011', 'd2Fsaw=='),
                ('01101101011001010110000101101110011010010110111001100111', 'bWVhbmluZw=='),
                ('01100110011000010110110001110011011010010110011001111001', 'ZmFsc2lmeQ=='),
                ('01100010011001010110111001100101011001100110100101110100', 'YmVuZWZpdA=='),
                ('011101000110100001110010011101010111001101110100', 'dGhydXN0'),
                ('011001000110010101100010011000010111010001100101', 'ZGViYXRl'),
                ('01110000011100100110111101100100011101010110001101110100011010010110111101101110', 'cHJvZHVjdGlvbg=='),
                ('011011100110111101110010011011010110000101101100', 'bm9ybWFs'),
                ('0110001101101000011000010111001001100001011000110111010001100101011100100110100101110011011101000110100101100011', 'Y2hhcmFjdGVyaXN0aWM='),
                ('01110000011100100110000101111001', 'cHJheQ=='),
                ('011101000111001001100101011000010111001101110101011100100110010101110010', 'dHJlYXN1cmVy'),
                ('011001010110111001110011011101010111001001100101', 'ZW5zdXJl'),
                ('011000100110000101110010011100100110010101101100', 'YmFycmVs'),
                ('01100011011011110111001001110010011001010111001101110000011011110110111001100100', 'Y29ycmVzcG9uZA=='),
                ('01110010011001010111001101101111011011000111010101110100011010010110111101101110', 'cmVzb2x1dGlvbg=='),
            ]
            
            kodirna_tabela = {
                '000000': 'A', '010000': 'Q', '100000': 'g', '110000': 'w', 
                '000001': 'B', '010001': 'R', '100001': 'h', '110001': 'x', 
                '000010': 'C', '010010': 'S', '100010': 'i', '110010': 'y', 
                '000011': 'D', '010011': 'T', '100011': 'j', '110011': 'z', 
                '000100': 'E', '010100': 'U', '100100': 'k', '110100': '0', 
                '000101': 'F', '010101': 'V', '100101': 'l', '110101': '1', 
                '000110': 'G', '010110': 'W', '100110': 'm', '110110': '2', 
                '000111': 'H', '010111': 'X', '100111': 'n', '110111': '3', 
                '001000': 'I', '011000': 'Y', '101000': 'o', '111000': '4', 
                '001001': 'J', '011001': 'Z', '101001': 'p', '111001': '5', 
                '001010': 'K', '011010': 'a', '101010': 'q', '111010': '6', 
                '001011': 'L', '011011': 'b', '101011': 'r', '111011': '7', 
                '001100': 'M', '011100': 'c', '101100': 's', '111100': '8', 
                '001101': 'N', '011101': 'd', '101101': 't', '111101': '9', 
                '001110': 'O', '011110': 'e', '101110': 'u', '111110': '+', 
                '001111': 'P', '011111': 'f', '101111': 'v', '111111': '/',
            }
            
            
            for bit, b64 in testi:
                if not Check.equal(f'zakodiraj("{bit}")', b64, env={'kodirna_tabela': kodirna_tabela}):
                    break
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
        ] = "eyJwYXJ0Ijo0MDIxMywidXNlciI6MTE0MjJ9:1wWE7D:nkkm5enoGInB4LoD8JCkYjaCzcLyOq-UUPKJDkOnKoM"
        try:
            testi = [
                ('000000', 'A'),
                ('011000100110000101111010011000010011011000110100', 'YmF6YTY0'),
                ('01100010011000010111101001100001', 'YmF6YQ=='),
                ('011000100110000101111010', 'YmF6'),
                ('0110001001100001011110100110000100110110', 'YmF6YTY='),
                ('0111000001110010011001010110010001100001011101000110111101110010', 'cHJlZGF0b3I='),
                ('0110010001110010011010010110110001101100', 'ZHJpbGw='),
                ('01110010011001010110110001101001011001010111011001100101', 'cmVsaWV2ZQ=='),
                ('0110001101101111011011110111000001100101011100100110000101110100011010010111011001100101', 'Y29vcGVyYXRpdmU='),
                ('0110110101101111011101010111001001101110011010010110111001100111', 'bW91cm5pbmc='),
                ('011001000110111101101100011011000110000101110010', 'ZG9sbGFy'),
                ('01110110011010010110110001101100011000010110011101100101', 'dmlsbGFnZQ=='),
                ('01110111011000010110100101110100', 'd2FpdA=='),
                ('0110001101101000011000010111001001101001011100110110110101100001011101000110100101100011', 'Y2hhcmlzbWF0aWM='),
                ('0110101001110101011001000110011101100101', 'anVkZ2U='),
                ('011001010111100001100011011001010110010101100100', 'ZXhjZWVk'),
                ('01101100011001010110000101101011', 'bGVhaw=='),
                ('0111001101110101011100100111000001110010011010010111001101100101', 'c3VycHJpc2U='),
                ('011001000110111101100011011101000110111101110010', 'ZG9jdG9y'),
                ('01110111011000010111001001101101', 'd2FybQ=='),
                ('011100110110100101110100', 'c2l0'),
                ('011100000110110001100001011110010110010101110010', 'cGxheWVy'),
                ('01110010011001010110111001110100', 'cmVudA=='),
                ('011000100110000101101110011010010111001101101000', 'YmFuaXNo'),
                ('0110010101101100011000100110111101110111', 'ZWxib3c='),
                ('011100000111001001100001011010010111001101100101', 'cHJhaXNl'),
                ('0110001001110101011010010110110001100100', 'YnVpbGQ='),
                ('011100000110111101110111011001000110010101110010', 'cG93ZGVy'),
                ('0111001101110100011100100110100101110000', 'c3RyaXA='),
                ('011001010111100001100011011101010111001101100101', 'ZXhjdXNl'),
                ('0111001101101110011000010111001001101100', 'c25hcmw='),
                ('01110010011000010111010001100101', 'cmF0ZQ=='),
                ('011001010111001101110100011000010111010001100101', 'ZXN0YXRl'),
                ('011100000111010101101110011010010111001101101000', 'cHVuaXNo'),
                ('011101000111011101101001011101000110001101101000', 'dHdpdGNo'),
                ('011000100111001001100101011000010110101101100110011000010111001101110100', 'YnJlYWtmYXN0'),
                ('011000100111010101100010011000100110110001100101', 'YnViYmxl'),
                ('01101110011011110111010001100101', 'bm90ZQ=='),
                ('01101000011010010111001101110100011011110111001001111001', 'aGlzdG9yeQ=='),
                ('01100011011000010111001101100101', 'Y2FzZQ=='),
                ('01110111011000010110110001101011', 'd2Fsaw=='),
                ('01101101011001010110000101101110011010010110111001100111', 'bWVhbmluZw=='),
                ('01100110011000010110110001110011011010010110011001111001', 'ZmFsc2lmeQ=='),
                ('01100010011001010110111001100101011001100110100101110100', 'YmVuZWZpdA=='),
                ('011101000110100001110010011101010111001101110100', 'dGhydXN0'),
                ('011001000110010101100010011000010111010001100101', 'ZGViYXRl'),
                ('01110000011100100110111101100100011101010110001101110100011010010110111101101110', 'cHJvZHVjdGlvbg=='),
                ('011011100110111101110010011011010110000101101100', 'bm9ybWFs'),
                ('0110001101101000011000010111001001100001011000110111010001100101011100100110100101110011011101000110100101100011', 'Y2hhcmFjdGVyaXN0aWM='),
                ('01110000011100100110000101111001', 'cHJheQ=='),
                ('011101000111001001100101011000010111001101110101011100100110010101110010', 'dHJlYXN1cmVy'),
                ('011001010110111001110011011101010111001001100101', 'ZW5zdXJl'),
                ('011000100110000101110010011100100110010101101100', 'YmFycmVs'),
                ('01100011011011110111001001110010011001010111001101110000011011110110111001100100', 'Y29ycmVzcG9uZA=='),
                ('01110010011001010111001101101111011011000111010101110100011010010110111101101110', 'cmVzb2x1dGlvbg=='),
            ]
            
            kodirna_tabela = {
                '000000': 'A', '010000': 'Q', '100000': 'g', '110000': 'w', 
                '000001': 'B', '010001': 'R', '100001': 'h', '110001': 'x', 
                '000010': 'C', '010010': 'S', '100010': 'i', '110010': 'y', 
                '000011': 'D', '010011': 'T', '100011': 'j', '110011': 'z', 
                '000100': 'E', '010100': 'U', '100100': 'k', '110100': '0', 
                '000101': 'F', '010101': 'V', '100101': 'l', '110101': '1', 
                '000110': 'G', '010110': 'W', '100110': 'm', '110110': '2', 
                '000111': 'H', '010111': 'X', '100111': 'n', '110111': '3', 
                '001000': 'I', '011000': 'Y', '101000': 'o', '111000': '4', 
                '001001': 'J', '011001': 'Z', '101001': 'p', '111001': '5', 
                '001010': 'K', '011010': 'a', '101010': 'q', '111010': '6', 
                '001011': 'L', '011011': 'b', '101011': 'r', '111011': '7', 
                '001100': 'M', '011100': 'c', '101100': 's', '111100': '8', 
                '001101': 'N', '011101': 'd', '101101': 't', '111101': '9', 
                '001110': 'O', '011110': 'e', '101110': 'u', '111110': '+', 
                '001111': 'P', '011111': 'f', '101111': 'v', '111111': '/',
            }
            
            
            for bit, b64 in testi:
                if not Check.equal(f'odkodiraj("{b64}")', bit, env={'kodirna_tabela': kodirna_tabela}):
                    break
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
