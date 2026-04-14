# =============================================================================
# Polinomi
#
# Definirajte razred `Polinom`, s katerim predstavimo polinom v
# spremenljivki $x$. Polinom predstavimo s seznamom njegovih koeficientov,
# kjer je $k$-ti element seznama koeficient pri $x^k$.
# 
# Na primer, polinom $x^3 + 2x + 7$ predstavimo s `Polinom([7, 2, 0, 1])`.
# Razmislite, kaj predstavlja `Polinom([])`. Zadnji koeficient v seznamu
# mora biti neničelen.
# =====================================================================@001741=
# 1. podnaloga
# Sestavite konstruktor `__init__(self, koef)`, ki nastavi objektu
# nastavi atribut `koef` (koeficienti polinoma). Zgled:
# 
#     >>> p = Polinom([7, 2, 0, 1])
#     >>> p.koef
#     [7, 2, 0, 1]
# 
# _Pozor_: Če kasneje spremenimo seznam, ki smo ga kot argument podali
# konstruktorju, se koeficienti polinoma ne smejo premeniti. Seznama,
# ki smo ga podali kot argument, konstruktor prav tako ne sme spremeninjati.
# Zgled:
# 
#     >>> l = [2, 0, 1]
#     >>> p = Polinom(l)
#     >>> l.append(3)
#     >>> p.koef
#     [2, 0, 1]
# =============================================================================
class Polinom:
    def __init__(self, koef):
        self.koef = koef[:]
        while len(self.koef) > 0 and self.koef[-1] == 0:
            self.koef.pop()
# =====================================================================@001742=
# 2. podnaloga
# Sestavite metodo `stopnja`, ki vrne stopnjo polinoma. Zgled:
# 
#     >>> p = Polinom([7, 2, 0, 1])
#     >>> p.stopnja()
#     3
# 
# _Opomba_: Za razpravo glede stopnje ničelnega polinoma glejte [članek
# na Wikipediji](http://en.wikipedia.org/wiki/Degree_of_a_polynomial#Degree_of_the_zero_polynomial).
# =============================================================================
    def stopnja(self):
        if len(self.koef) == 0:
            return float("-inf")
        return len(self.koef) - 1
# =====================================================================@001743=
# 3. podnaloga
# Sestavite metodo `__repr__`, ki vrne niz oblike
# `'Polinom([a_0, …, a_n])'`, kjer so `a_0, …, a_n` koeficienti polinoma.
# Zgled:
# 
#     >>> p = Polinom([5, 0, 1])
#     >>> p
#     Polinom([5, 0, 1])
# =============================================================================
    def __repr__(self):
        return f"Polinom({self.koef})"
# =====================================================================@001744=
# 4. podnaloga
# Sestavite metodo `__eq__(self, other)` za primerjanje polinomov. Zgled:
# 
#     >>> Polinom([3, 2, 0, 1]) == Polinom([3, 2])
#     False
#     >>> Polinom([3, 2, 1, 0]) == Polinom([3, 2, 1])
#     True
# =============================================================================
    def __eq__(self, other):
        return self.koef == other.koef
# =====================================================================@001745=
# 5. podnaloga
# Sestavite metodo `__call__(self, x)`, ki izračuna in vrne vrednost
# polinoma v `x`. Pri izračunu vrednosti uporabite Hornerjev algoritem.
# Če definiramo metodo `__call__`, objekt postane "klicljiv" (tj. lahko
# ga kličemo, kakor da bi bil funkcija). Zgled:
# 
#     >>> p = Polinom([3, 2, 0, 1])
#     >>> p(1)
#     6
#     >>> p(-3)
#     -30
#     >>> p(0.725)
#     4.8310781249999994
# =============================================================================
    def __call__(self, x):
        rezultat = 0
        for k in reversed(self.koef):
            rezultat = rezultat * x + k
        return rezultat
# =====================================================================@001746=
# 6. podnaloga
# Sestavite metodo `__add__(self, other)` za seštevanje polinomov. Metoda
# naj sestavi in vrne nov objekt razreda `Polinom`, ki bo vsota polinomov
# `self` in `other`. Zgled:
# 
#     >>> Polinom([1, 0, 1]) + Polinom([4, 2])
#     Polinom([5, 2, 1])
# 
# _Pozor_: Pri seštevanju se lahko zgodi, da se nekateri koeficienti
# pokrajšajo: $(x^3 + 2x + 7) + (-x^3 - 2x + 10) = 17$.
# =============================================================================
    def __add__(self, other):
        max_len = max(len(self.koef), len(other.koef))
        novi = []
        for i in range(max_len):
            a = self.koef[i] if i < len(self.koef) else 0
            b = other.koef[i] if i < len(other.koef) else 0
            novi.append(a + b)
        return Polinom(novi)
# =====================================================================@001747=
# 7. podnaloga
# Sestavite metodo `__mul__` za množenje polinomov. Metoda
# naj sestavi in vrne nov objekt razreda `Polinom`, ki bo produkt polinomov.
# Zgled:
# 
#     >>> Polinom([1, 0, 1]) * Polinom([4, 2])
#     Polinom([4, 2, 4, 2])
# =============================================================================
    def __mul__(self, other):
        rezultat = [0] * (len(self.koef) + len(other.koef) - 1)
        for i in range(len(self.koef)):
            for j in range(len(other.koef)):
                rezultat[i + j] += self.koef[i] * other.koef[j]
        return Polinom(rezultat)
# =====================================================================@001748=
# 8. podnaloga
# Sestavite metodo `odvod(self, k)`, sestavi in vrne nov polinom, ki bo
# $k$-ti odvod polinoma `self`. Argument `k` naj ima privzeto vrednost 1.
# Zgled:
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, -1])
#     >>> p.odvod()
#     Polinom([1, 8, -9, 20, -5])
#     >>> p.odvod(2)
#     Polinom([8, -18, 60, -20])
# =============================================================================
    def odvod(self, k=1):
        koef = self.koef[:]
        for _ in range(k):
            novi = []
            for i in range(1, len(koef)):
                novi.append(i * koef[i])
            koef = novi

        return Polinom(koef)
# =====================================================================@001749=
# 9. podnaloga
# Sestavite metodo `__str__`, ki predstavi polinom v čitljivi obliki,
# kot kaže primer:
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, -1])
#     -x^5 + 5x^4 - 3x^3 + 4x^2 + x + 5
# 
# Za niz, ki ga funkcija vrne, naj velja naslednje:
# 
# * Polinom je sestavljen iz monomov oblike `ax^k`, kjer je `a` ustrezen
#   koeficient.
# * Monomi so med seboj povezani z znaki `+`; pred in za plusom je po en
#   presledek.
# * Namesto `x^1` bomo pisali samo `x`, `x^0` pa bomo izpustili in pisali
#   samo koeficient.
# * Če je koeficient 1, bomo namesto `1x^k` pisali `x^k`. Če je -1, bomo
#   namesto `-1x^k` pisali `-x^k`. To ne velja za prosti člen.
# * Če je koeficient negativen, bomo pri združevanju monomov uporabili
#   znak `-` namesto znaka `+`. Torej, namesto `ax^m + -bx^n` bomo pisali
#   `ax^m - bx^n`. To ne velja za vodilni člen.
# * Če je koeficient 0, bomo monom izpustili. To pravilo ne velja za
#   ničelni polinom.
# =============================================================================
    def __str__(self):
        if len(self.koef) == 0:
            return "0"
        deli = []

        for i in range(len(self.koef) - 1, -1, -1):
            a = self.koef[i]
            if a == 0:
                continue
            if i == 0:
                izraz = f"{abs(a)}"
            elif i == 1:
                izraz = "x" if abs(a) == 1 else f"{abs(a)}x"
            else:
                izraz = f"x^{i}" if abs(a) == 1 else f"{abs(a)}x^{i}"
            if len(deli) == 0:
                deli.append(("-" if a < 0 else "") + izraz)
            else:
                deli.append((" - " if a < 0 else " + ") + izraz)

        return "".join(deli)

# =====================================================================@027731=
# 10. podnaloga
# Sestavite metodi `__iter__` in `__next__`, ki bosta omogočili, da se po 
# neničelnih koeficientih polinoma sprehodimo kar s `for` zanko. Metodi naj 
# delujeta tako, da bomo ob sprehodu s for zanko dobili pare 
# `(koeficient, eksponent)` padajoče glede na eksponent in brez neničelnih 
# eksponentov. 
# 
# Lahko predpostavite, da se po polinomu nikoli ne bomo sprehajali v gnezdeni 
# zanki.
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, 0, -1])
#     >>> list(p)
#     >>> [(-1, 6), (5, 4), (-3, 3), (4, 2), (1, 1), (5, 0)]
# =============================================================================
    def __iter__(self):
        self._i = len(self.koef) - 1
        return self

    def __next__(self):
        while self._i >= 0:
            k = self.koef[self._i]
            e = self._i
            self._i -= 1

            if k != 0:
                return (k, e)

        raise StopIteration





def monom(a, i):
    if a == 0:
        return ""

    if a < 0:
        predznak = "-"
    else:
        predznak = ""
    a = abs(a)

    if i == 0:
        zapis = f"{a}"
    elif i == 1:
        zapis = "x" if a == 1 else f"{a}x"
    else:
        zapis = f"x^{i}" if a == 1 else f"{a}x^{i}"

    return predznak + zapis































































































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
        ] = "eyJwYXJ0IjoxNzQxLCJ1c2VyIjoxMTQyMn0:1wCcep:FLi89zPfV4iu35iZdIEkpQ3OCwCgINW8-dRRYaVFcvU"
        try:
            test_data = [
                ('Polinom([1, 2, 3]).koef', [1, 2, 3]),
                ('Polinom([1, 2, 0, 0]).koef', [1, 2]),
                ('Polinom([0, 0, 0, 0]).koef', []),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 7]).koef', [0, 0, 0, 0, 0, 0, 0, 7]),
            ]
            additional_tests = [
                (["l = [1, 2, 3, 0, 0, 0]",
                  "p = Polinom(l)",
                  "k = p.koef"],
                 {'l': [1, 2, 3, 0, 0, 0],
                  'k': [1, 2, 3]}),
                (["l = [1, 2, 3, 0, 0, 0]",
                  "p = Polinom(l)",
                  "l.extend([13, 14, 15])",
                  "k = p.koef"],
                 {'l': [1, 2, 3, 0, 0, 0, 13, 14, 15],
                  'k': [1, 2, 3]}),
                (["l = [1, 2, 3]",
                  "p = Polinom(l)",
                  "del l[-1]",
                  "del l[-1]", 
                  "k = p.koef"],
                 {'l': [1],
                  'k': [1, 2, 3]}),
            ]
            vse_ok = True
            for td in test_data:
                if not Check.equal(*td):
                    vse_ok = False
                    break
            if vse_ok:
                for td in additional_tests:
                    if Check.run(*td):
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
        ] = "eyJwYXJ0IjoxNzQyLCJ1c2VyIjoxMTQyMn0:1wCcep:Hb9C34gtw5pv3YJX5WcOoBDfqCWK7qCXM8vPM-YC7GI"
        try:
            test_data = [
                ('Polinom([7, 2, 0, 1]).stopnja()', 3),
                ('Polinom([1, 2, 3]).stopnja()', 2),
                ('Polinom([1, 2, 3, 4, 5, 13, -22]).stopnja()', 6),
                ('Polinom([1]).stopnja()', 0),
                ('Polinom([]).stopnja()', float('-inf')),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
        ] = "eyJwYXJ0IjoxNzQzLCJ1c2VyIjoxMTQyMn0:1wCcep:XcfQd-D5N1En3NYl900_gyEC0RdlsPBNzDEXRR1q1aY"
        try:
            test_data = [
                ('repr(Polinom([1, 2, 3]))', "Polinom([1, 2, 3])"),
                ('repr(Polinom([1, 2, 3, 0, 0]))', "Polinom([1, 2, 3])"),
                ('repr(Polinom([]))', "Polinom([])"),
                ('repr(Polinom([0, 0]))', "Polinom([])"),
                ('repr(Polinom([1, 3]))', "Polinom([1, 3])"),
                ('repr(Polinom([7]))', "Polinom([7])"),
                ('repr(Polinom([1, -2, 3, -1]))', "Polinom([1, -2, 3, -1])"),
                ('repr(Polinom([1, 0, 0, -1]))', "Polinom([1, 0, 0, -1])"),
                ('repr(Polinom([0, 0, 0, -5]))', "Polinom([0, 0, 0, -5])"),
                ('repr(Polinom([-1, 2, -3, 1]))', "Polinom([-1, 2, -3, 1])"),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
        ] = "eyJwYXJ0IjoxNzQ0LCJ1c2VyIjoxMTQyMn0:1wCcep:zJv6fxKSgKEbCUvBJI-HvcsKBcaBD5Nu7eJZC7S5Auk"
        try:
            test_data = [
                ('Polinom([1, 2, 3]) == Polinom([1, 2, 3, 0, 0])', True),
                ('Polinom([3, 2, 1, 0]) == Polinom([3, 2])', False),
                ('Polinom([3, 2, 1, 0]) == Polinom([3, 2, 1])', True),
                ('Polinom([1, 2, 3]) != Polinom([0, 1, 2, 3])', True),
                ('Polinom([1, 2, 3]) == Polinom([3, 2, 1])', False),
                ('Polinom([]) == Polinom([3, 2, 1])', False),
                ('Polinom([]) == Polinom([0])', True),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
        ] = "eyJwYXJ0IjoxNzQ1LCJ1c2VyIjoxMTQyMn0:1wCcep:Iv0RHrbWSTv34LrnSUM1YKIdnu_p8Sdm_BS4_5yyhLU"
        try:
            test_data = [
                ('Polinom([3, 2, 0, 1])(1)', 6),
                ('Polinom([1, 1, 1, 1, 1, 1, 1, 1, 1])(0)', 1),
                ('Polinom([1, 1, 1, 1, 1, 1, 1, 1, 1])(1)', 9),
                ('Polinom([1, 1, 1, 1, 1, 1, 1, 1, 1])(3)', 9841),
                ('Polinom([3, 2, 0, 1])(-3)', -30),
                ('Polinom([3, 2, 0, 1])(0.725)', 4.8310781249999994),
                ('Polinom([])(1337)', 0),
                ('Polinom([])(-666)', 0),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
        ] = "eyJwYXJ0IjoxNzQ2LCJ1c2VyIjoxMTQyMn0:1wCcep:slBoplp2grYuoCbchW4YXPclF29ptpUxfyu-T4ENe_c"
        try:
            test_data = [
                ('Polinom([1, 2, 3, 0, 0, 0, 0, 7]) + Polinom([4, 5])', Polinom([5, 7, 3, 0, 0, 0, 0, 7])),
                ('Polinom([1, 2, 3]) + Polinom([4, 5, 0, 0, 0, 0, 0, 0, -1])', Polinom([5, 7, 3, 0, 0, 0, 0, 0, -1])),
                ('Polinom([1, 2, 3]) + Polinom([4, 5])', Polinom([5, 7, 3])),
                ('Polinom([1, 0, 1]) + Polinom([4, 2])', Polinom([5, 2, 1])),
                ('Polinom([1, 2, 3]) + Polinom([-1, -2])', Polinom([0, 0, 3])),
                ('Polinom([1, 2, 3]) + Polinom([0, 0, -3])', Polinom([1, 2])),
            ]
            additional_tests = [
                (["p = Polinom([1, 2, 3])",
                  "q = Polinom([1, 2, 3, 4, 5, 6, 7])",
                  "r = p + q",
                  "p_koef, q_koef = p.koef, q.koef"],
                 {'r': Polinom([2, 4, 6, 4, 5, 6, 7]),
                  'p_koef': [1, 2, 3],
                  'q_koef': [1, 2, 3, 4, 5, 6, 7]}),
            ]
            vse_ok = True
            for td in test_data:
                if not Check.equal(*td):
                    vse_ok = False
                    break
            if vse_ok:
                for td in additional_tests:
                    if Check.run(*td):
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
        ] = "eyJwYXJ0IjoxNzQ3LCJ1c2VyIjoxMTQyMn0:1wCcep:0E1Y1Zv_KmRMiGt7aY-tay_Z0O8TPN3MYaJUHsUbA9M"
        try:
            test_data = [
                ('Polinom([1, 0, 1]) * Polinom([4, 2])', Polinom([4, 2, 4, 2])),
                ('Polinom([0, 0, 0, 0, 0, 0, 1]) * Polinom([0, 0, 0, 0, 0, 0, 1])',
                 Polinom([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])),
                ('Polinom([1, 0, 1]) * Polinom([])', Polinom([])),
                ('Polinom([]) * Polinom([4, 2])', Polinom([])),
                ('Polinom([]) * Polinom([])', Polinom([])),
                ('Polinom([1, 2, 3]) * Polinom([2])', Polinom([2, 4, 6])),
                ('Polinom([1, 2, 1]) * Polinom([1, 1])', Polinom([1, 3, 3, 1])),
                ('Polinom([1, 2, 1, 3, 1]) * Polinom([1, 1, 5, 4, 3, 1])', Polinom([1, 3, 8, 18, 20, 27, 22, 14, 6, 1])),
                ('Polinom([1, 2, 3]) * Polinom([0, 0, 0])', Polinom([])),
            ]
            additional_tests = [
                (["p = Polinom([1, 2, 3])",
                  "q = Polinom([1, 2, 3, 4, 5, 6, 7])",
                  "r = p * q",
                  "p_koef, q_koef = p.koef, q.koef"],
                 {'r': Polinom([1, 4, 10, 16, 22, 28, 34, 32, 21]),
                  'p_koef': [1, 2, 3],
                  'q_koef': [1, 2, 3, 4, 5, 6, 7]}),
            ]
            vse_ok = True
            for td in test_data:
                if not Check.equal(*td):
                    vse_ok = False
                    break
            if vse_ok:
                for td in additional_tests:
                    if Check.run(*td):
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
        ] = "eyJwYXJ0IjoxNzQ4LCJ1c2VyIjoxMTQyMn0:1wCcep:MeL2feP3boStJrOtvXpEHVSPfYTBlykXimv1wIIHMBg"
        try:
            test_data = [
                ('Polinom([5, 1, 4, -3, 5, -1]).odvod()', Polinom([1, 8, -9, 20, -5])),
                ('Polinom([5, 1, 4, -3, 5, -1]).odvod(2)', Polinom([8, -18, 60, -20])),
                ('Polinom([1, 2, 3]).odvod()', Polinom([2, 6])),
                ('Polinom([3, 2, 1, 0, 1, 2, 3]).odvod()', Polinom([2, 2, 0, 4, 10, 18])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod()',  Polinom([0, 0, 0, 0, 0, 0, 0, 8])),
                ('Polinom([5, 4, 3, 2, 1]).odvod()', Polinom([4, 6, 6, 4])),
                ('Polinom([1]).odvod()', Polinom([])),
                ('Polinom([]).odvod()', Polinom([])),
                ('Polinom([5, 4, 3, 2, 1]).odvod(0)', Polinom([5, 4, 3, 2, 1])),
                ('Polinom([1]).odvod(0)', Polinom([1])),
                ('Polinom([1, 2, 3]).odvod(2)', Polinom([6])),
                ('Polinom([3, 2, 1, 0, 1, 2, 3]).odvod(2)', Polinom([2, 0, 12, 40, 90])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod(2)', Polinom([0, 0, 0, 0, 0, 0, 56])),
                ('Polinom([1, 2, 3]).odvod(3)', Polinom([])),
                ('Polinom([3, 2, 1, 0, 1, 2, 3]).odvod(3)', Polinom([0, 24, 120, 360])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod(3)', Polinom([0, 0, 0, 0, 0, 336])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod(8)', Polinom([40320])),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
        ] = "eyJwYXJ0IjoxNzQ5LCJ1c2VyIjoxMTQyMn0:1wCcep:vBtkk1Kv_Bn8ZvTQ68J-amlAo55Mf96S3BnV6EA9cnc"
        try:
            test_data = [
                ('str(Polinom([1, 2, 3]))', "3x^2 + 2x + 1"),
                ('str(Polinom([-1, -2, -3]))', "-3x^2 - 2x - 1"),
                ('str(Polinom([-1, -1, 1]))', "x^2 - x - 1"),
                ('str(Polinom([1, 1, -1]))', "-x^2 + x + 1"),
                ('str(Polinom([1, 1, 1, 1, 1, 1, 1, 1]))', 'x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1'),
                ('str(Polinom([0, 0, 0, 0, 0, 0, 0, 1]))', 'x^7'),
                ('str(Polinom([5, 1, 4, -3, 5, -1]))', "-x^5 + 5x^4 - 3x^3 + 4x^2 + x + 5"),
                ('str(Polinom([1, 3]))', "3x + 1"),
                ('str(Polinom([1, -2, 3, -1]))', "-x^3 + 3x^2 - 2x + 1"),
                ('str(Polinom([1, 0, 0, -1]))', "-x^3 + 1"),
                ('str(Polinom([0, 0, 0, -5]))', "-5x^3"),
                ('str(Polinom([-1, 2, -3, 1]))', "x^3 - 3x^2 + 2x - 1"),
                ('str(Polinom([]))', "0"),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
        ] = "eyJwYXJ0IjoyNzczMSwidXNlciI6MTE0MjJ9:1wCcep:uwCATC02UNJ9wRJe7ENe7ipQvUwTxTwYgjuDxWmY7vk"
        try:
            test_data = [
                ("list(Polinom([1, 2, 3]))", [(3, 2), (2, 1), (1, 0)]),
                ("list(Polinom([-1, -2, -3]))", [(-3, 2), (-2, 1), (-1, 0)]),
                ("list(Polinom([-1, -1, 1]))", [(1, 2), (-1, 1), (-1, 0)]),
                ("list(Polinom([1, 1, -1]))", [(-1, 2), (1, 1), (1, 0)]),
                ("list(Polinom([1, 1, 1, 1, 1, 1, 1, 1]))", [(1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0)]),
                ("list(Polinom([0, 0, 0, 0, 0, 0, 0, 1]))", [(1, 7)]),
                ("list(Polinom([5, 1, 4, -3, 5, -1]))", [(-1, 5), (5, 4), (-3, 3), (4, 2), (1, 1), (5, 0)]),
                ("list(Polinom([1, 3]))", [(3, 1), (1, 0)]),
                ("list(Polinom([1, -2, 3, -1]))", [(-1, 3), (3, 2), (-2, 1), (1, 0)]),
                ("list(Polinom([1, 0, 0, -1]))", [(-1, 3), (1, 0)]),
                ("list(Polinom([0, 0, 0, -5]))", [(-5, 3)]),
                ("list(Polinom([-1, 2, -3, 1]))", [(1, 3), (-3, 2), (2, 1), (-1, 0)]),
                ("list(Polinom([1, 0, 0, 2, 0, 0, 0, 3, 4, 0, -4, 0]))", [(-4, 10), (4, 8), (3, 7), (2, 3), (1, 0)]),
                ("list(Polinom([]))", []),
            ]
            for td in test_data:
                if not Check.equal(*td):
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
