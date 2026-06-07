# =============================================================================
# Avtobusni prevozi
#
# Podatki o linijah mestnega avtobusnega prometa so zbrani v znakovni datoteki,
# kot je prikazano na spodnjem primeru za datoteko `linije.txt`.
# Za vsakim imenom linije so našteta imena postaj, kot si sledijo na tej liniji.
# Vsako ime je zapisano v svoji vrstici, vmes ni nobenih praznih vrstic.
# 
#     1
#     Sodisce
#     Knjiznica
#     Trg
#     Park
#     1A
#     Park
#     Trg
#     Gledalisce
#     2
#     Trgovina
#     Muzej
#     Sola
#     Gledalisce
# 
# V zgornji datoteki so podatki za tri linije z imeni `1`, `1A` in `2`.
# Linija `1` ima začetno postajo `Sodisce`, naslednja postaja je `Knjiznica`,
# potem `Trg`, končna postaja pa je `Park`. Sledijo podatki za linijo `1A` in
# zatem še za linijo `2`. Predpostavite lahko, da se vsako ime linije začne s
# številko in da se vsako ime postaje začne s črko. Vsaka linija vozi v obe smeri.
# =====================================================================@040194=
# 1. podnaloga
# Sestavite funkcijo `linije`, ki sprejme ime vhodne datoteke in vrne slovar,
# v katerem so ključi imena linij in vrednosti seznami pripadajočih postaj v
# vrstnem redu, kot so napisane v vhodni datoteki.
# 
#     >>> linije('linije.txt')
#     {'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'],
#      '1A': ['Park', 'Trg', 'Gledalisce'],
#      '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']}
# =============================================================================
def linije(dat):
    slovar = {}
    with open(dat, "r", encoding="utf-8") as vhodna:
        vsebina = vhodna.read()
        vsebina = vsebina.splitlines()
    linija = None
    for el in vsebina:
        if el[0].isdigit():
            linija = el
            slovar[linija] = []
        else:
            slovar[linija].append(el)
    return slovar
# =====================================================================@040195=
# 2. podnaloga
# Podatki v vhodni datoteki so nekoliko nepregledni. Sestavite funkcijo `pregledno`,
# ki sprejme slovar enake oblike kot je rezultat prejšnje podnaloge in ime izhodne
# datoteke, v katero pregledneje izpiše imena linij in postaj. Vsaka vrstica naj
# predstavlja svojo linijo, ki se začne z imenom linije in dvopičjem, nato pa naj
# bodo našteta postajališča, ločena s puščico. Zgleduj se po spodnjem primeru.
# 
#     slovar = {'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'],
#            '1A': ['Park', 'Trg', 'Gledalisce'],
#            '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']}
# 
# Po klicu `pregledno(slovar, 'pregledno.txt')` dobimo datoteko `pregledno.txt`
# z vsebino
# 
#     1: Sodisce -> Knjiznica -> Trg -> Park
#     1A: Park -> Trg -> Gledalisce
#     2: Trgovina -> Muzej -> Sola -> Gledalisce
# =============================================================================
def pregledno(slovar, izhodna):
    with open(izhodna, "w", encoding="utf-8") as dat:
        for linija in slovar:
            niz = ""
            for el in slovar[linija]:
                niz += str(el) + " -> " 
            dat.write(f"{linija}: {niz[:-4]}\n")

#def pregledno(slovar, izhodna):
#    with open(izhodna, "w", encoding="utf-8") as dat:
#        for linija in slovar:
#            postaje = " -> ".join(slovar[linija])
#            dat.write(f"{linija}: {postaje}\n")

# =====================================================================@040196=
# 3. podnaloga
# Sestavite funkcijo `obstaja_povezava`, ki sprejme slovar linij, začetno ter 
# končno postajo in vrne `True`, če obstaja povezava od začetne do končne postaje
# z **največ enim** prestopom, sicer pa `False`. Če začetne ali končne postaje 
# ni v slovarju, naj funkcija vrne `None`.
# 
#     >>> obstaja_povezava(slovar, 'Trgovina', 'Trg')
#     True
#     >>> obstaja_povezava(slovar, 'Sodisce', 'Sola')
#     False
#     >>> obstaja_povezava(slovar, 'Trg', 'Aaaaaa')
#     None
# =============================================================================
def obstaja_povezava(slovar, zacetna, koncna):
    vse_postaje = []
    for postaje in slovar.values():
        vse_postaje += postaje
    if zacetna not in vse_postaje or koncna not in vse_postaje:
        return None
    for postaje1 in slovar.values():
        if zacetna in postaje1:
            for prestopna in postaje1:
                for postaje2 in slovar.values():
                    if prestopna in postaje2 and koncna in postaje2:
                        return True
    return False




































































































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
        ] = "eyJwYXJ0Ijo0MDE5NCwidXNlciI6MTE0MjJ9:1wW8ed:MJFMM3et7ABP49F3O9fmlmP3WXxKHJ0Kx6lG8oFujto"
        try:
            primeri = [
                (
                    'linije_test.txt',
                    ['1', 'Sodisce', 'Knjiznica', 'Trg', 'Park', '1A', 'Park', 'Trg', 'Gledalisce', '2', 'Trgovina', 'Muzej', 'Sola', 'Gledalisce'],
                    {'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'], '1A': ['Park', 'Trg', 'Gledalisce'], '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']}
                ),
                (
                    'linije_lpp.txt',
                    ['1', 'D. Most P+R', 'Zgornji Log', 'Cesta V Gorice', 'Mestni Log', 'Tbilisijska', 'Koprska', 'Krimska', 'Gerbiceva', 'Jadranska', 'Hajdrihova', 'Tobacna', 'Askerceva', 'Drama', 'Posta', 'Ajdovscina', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Kino Siska', 'Remiza', 'Aleja', 'Kompas', 'Dravlje', 'Trata', 'Prusnikova', 'Podgora', 'Sentvid', 'Vizmarje', 'Stanezice P+R', '2', 'Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Roziceva', 'Kavciceva', 'Tovorni Kolodvor', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Ambrozev Trg', 'Poljanska', 'Lutkovno Gl.', 'Gornji Trg', 'Krizanke', 'Drama', 'Posta', 'Ajdovscina', 'Bavarski Dvor', 'Kolodvor', 'Friskovec', 'Viadukt', 'Savsko Naselje', 'Zale', 'Pokopaliska', 'Zelena Jama', '3', 'Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik', '3B', 'Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica Obr.', '3G', 'Zelezna', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Strelisce', 'Rakovnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica', 'Skofljica Javornik', 'Reber Pri Skofljici', 'Spilar', 'Mali Vrh', 'Razdrto', 'Smarje', 'Sap', 'Cikava', 'Brvace', 'Stara Posta', 'Pod Gozdom', 'Adamicev Spomenik', 'Ljubljanska', 'Os Brinje', 'Kongo', 'Dom Starejsih', 'Dom Obrtnikov', 'Vodicar', 'Krpan', 'Mrzle Njive', 'Grosuplje', '5', 'Podutik', 'Murkova', 'Omersova', 'Pod Kamno Gorico', 'Draveljska Gmajna', 'Koseze', 'Bratov Ucakar', 'Kneza Koclja', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Dalmatinova', 'Ilirska', 'Hrvatski Trg', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Glonarjeva', 'Jana Husa', 'Kodeljevo', 'Stepanja Vas', 'Emona', 'Nusdorferjeva', 'Stepanjsko Nas.', '6', 'Crnuce', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'D. Most P+R', '6B', 'Zelezna', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'Podvozna Pot', 'Dolgi Most Rotar', 'Kozarje', 'Na Gmajnici', 'Radna', 'Brezovica Posta', 'Solska', 'Japelj', 'Erbeznik', 'Mosticek', 'Notranje Gorice', '7', 'Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Na Jami', 'Bolnica P. Drzaja', 'Zgornja Siska', 'Trznica Koseze', 'Cebelarska', 'Plesiceva', 'Andreja Bitenca', 'Przanec', 'Przan', '8', 'Brod', 'Martinova', 'Tabor', 'Na Klancu', 'Kosmaceva', 'Sentvid', 'Podgora', 'Prusnikova', 'Imp', 'Tehnounion', 'Ljubljanske Brigade', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Bavarski Dvor', 'Razstavisce', 'Astra', 'Stadion', 'Mercator', 'Amzs', 'Smelt', 'Stozice', 'Ruski Car', 'Stara Jezica', 'Jezica', 'Sava', 'Elma', 'Slandrova', 'Obrtna Cona', 'Cesta Na Brod', 'Slovenijales', 'Brnciceva', '9', 'Stepanjsko Nas.', 'Nusdorferjeva', 'Emona', 'Stepanja Vas', 'Kodeljevo', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Poliklinika', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Mirje', 'Ziherlova', 'Murgle', 'Barje P+R', '11', 'Jezica P+R', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Streliska', 'Cukrarna', 'Klinicni Center', 'Bolnica', 'Trznica Moste', 'Zaloska', 'Pot Na Fuzine', 'Archinetova', 'Osenjakova', 'Chengdujska', 'Studenec', 'Polje', 'Cesta Na Vevce', 'Kaseljska', 'Petrol', 'Silos', 'Center Zalog', 'Zeleni Gaj', 'Agrokombinatska', 'Zalog', '12', 'Zelezna', 'Bezigrad', 'Razstavisce', 'Kolodvor', 'Friskovec', 'Viadukt', 'Srediska', 'Flajsmanova', 'Sola Jarse', 'Jarse', 'Kodrova', 'Zito', 'Hrastje', 'Sneberje', 'Trbeze', 'Zadobrova', 'Novo Polje', 'Polje-Kolodvor', 'Polje', 'Cesta Na Vevce', 'Vevce', '13', 'C. Stozice P+R', 'Boziceva', 'Kardeljeva Ploscad', 'Gasilska Brigada', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Dalmatinova', 'Zmajski Most', 'Poljanska', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Pod Golovcem', 'Stepanja Vas', 'Emona', 'Rast', 'Hrusica', 'Cesta V Bizovik', 'Dobrunje', 'Posta Dobrunje', 'Kpl', 'Zadvor', 'Cesta V Zavoglje', 'Krizisce Sostro', 'Sostro', '21', 'Bericevo', 'Reaktor', 'Sentjakob', 'Belinka', 'Nadgorica', 'Jeza', 'Zasavska', 'Os Maksa Pecarja', 'Pot V Hrastovec', 'Pot V Smrecje', 'Polanskova', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica', '22', 'Fuzine P+R', 'Rusjanov Trg', 'Preglov Trg', 'Brodarjev Trg', 'Pot Na Fuzine', 'Kajuhova', 'Tovorni Kolodvor', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Astra', 'Samova', 'Drenikova', 'Kino Siska', 'Sisenska', 'Kneza Koclja', 'Bratov Ucakar', 'Koseze', 'Bratov Babnik', 'Spar', 'Kamna Gorica', '24', 'Btc-Atlantis', 'Btc-Merkur', 'Btc-Emporium', 'Tovorni Kolodvor', 'Ob Sotocju', 'Kodeljevo', 'Stepanja Vas', 'Bilecanska', 'Krozna Pot', 'Hrusevska', 'Bizovik', 'Dobrunjska C.', 'Dobrunje-2', 'Pod Urhom', 'Zadvor-2', 'Os Sostro', 'Krizisce Sostro', 'Cesta V Zavoglje', 'Zadvor', 'Vevce Papirnica', 'Vevce', '27', 'Letaliska', 'Leskoskova', 'Btc-Emporium', 'Btc-Merkur', 'Btc-Kolosej', 'Btc-Trznica', 'Btc-Uprava', 'Kodrova', 'Jarse', 'Sola Jarse', 'Srediska', 'Viadukt', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Orlova', 'Izanska', 'Galjevica', 'Golouhova', 'Mihov Stradon', 'Jurckova', 'Bobrova', 'Ns Rudnik'],
                    {'1': ['D. Most P+R', 'Zgornji Log', 'Cesta V Gorice', 'Mestni Log', 'Tbilisijska', 'Koprska', 'Krimska', 'Gerbiceva', 'Jadranska', 'Hajdrihova', 'Tobacna', 'Askerceva', 'Drama', 'Posta', 'Ajdovscina', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Kino Siska', 'Remiza', 'Aleja', 'Kompas', 'Dravlje', 'Trata', 'Prusnikova', 'Podgora', 'Sentvid', 'Vizmarje', 'Stanezice P+R'], '2': ['Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Roziceva', 'Kavciceva', 'Tovorni Kolodvor', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Ambrozev Trg', 'Poljanska', 'Lutkovno Gl.', 'Gornji Trg', 'Krizanke', 'Drama', 'Posta', 'Ajdovscina', 'Bavarski Dvor', 'Kolodvor', 'Friskovec', 'Viadukt', 'Savsko Naselje', 'Zale', 'Pokopaliska', 'Zelena Jama'], '3': ['Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik'], '3B': ['Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica Obr.'], '3G': ['Zelezna', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Strelisce', 'Rakovnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica', 'Skofljica Javornik', 'Reber Pri Skofljici', 'Spilar', 'Mali Vrh', 'Razdrto', 'Smarje', 'Sap', 'Cikava', 'Brvace', 'Stara Posta', 'Pod Gozdom', 'Adamicev Spomenik', 'Ljubljanska', 'Os Brinje', 'Kongo', 'Dom Starejsih', 'Dom Obrtnikov', 'Vodicar', 'Krpan', 'Mrzle Njive', 'Grosuplje'], '5': ['Podutik', 'Murkova', 'Omersova', 'Pod Kamno Gorico', 'Draveljska Gmajna', 'Koseze', 'Bratov Ucakar', 'Kneza Koclja', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Dalmatinova', 'Ilirska', 'Hrvatski Trg', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Glonarjeva', 'Jana Husa', 'Kodeljevo', 'Stepanja Vas', 'Emona', 'Nusdorferjeva', 'Stepanjsko Nas.'], '6': ['Crnuce', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'D. Most P+R'], '6B': ['Zelezna', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'Podvozna Pot', 'Dolgi Most Rotar', 'Kozarje', 'Na Gmajnici', 'Radna', 'Brezovica Posta', 'Solska', 'Japelj', 'Erbeznik', 'Mosticek', 'Notranje Gorice'], '7': ['Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Na Jami', 'Bolnica P. Drzaja', 'Zgornja Siska', 'Trznica Koseze', 'Cebelarska', 'Plesiceva', 'Andreja Bitenca', 'Przanec', 'Przan'], '8': ['Brod', 'Martinova', 'Tabor', 'Na Klancu', 'Kosmaceva', 'Sentvid', 'Podgora', 'Prusnikova', 'Imp', 'Tehnounion', 'Ljubljanske Brigade', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Bavarski Dvor', 'Razstavisce', 'Astra', 'Stadion', 'Mercator', 'Amzs', 'Smelt', 'Stozice', 'Ruski Car', 'Stara Jezica', 'Jezica', 'Sava', 'Elma', 'Slandrova', 'Obrtna Cona', 'Cesta Na Brod', 'Slovenijales', 'Brnciceva'], '9': ['Stepanjsko Nas.', 'Nusdorferjeva', 'Emona', 'Stepanja Vas', 'Kodeljevo', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Poliklinika', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Mirje', 'Ziherlova', 'Murgle', 'Barje P+R'], '11': ['Jezica P+R', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Streliska', 'Cukrarna', 'Klinicni Center', 'Bolnica', 'Trznica Moste', 'Zaloska', 'Pot Na Fuzine', 'Archinetova', 'Osenjakova', 'Chengdujska', 'Studenec', 'Polje', 'Cesta Na Vevce', 'Kaseljska', 'Petrol', 'Silos', 'Center Zalog', 'Zeleni Gaj', 'Agrokombinatska', 'Zalog'], '12': ['Zelezna', 'Bezigrad', 'Razstavisce', 'Kolodvor', 'Friskovec', 'Viadukt', 'Srediska', 'Flajsmanova', 'Sola Jarse', 'Jarse', 'Kodrova', 'Zito', 'Hrastje', 'Sneberje', 'Trbeze', 'Zadobrova', 'Novo Polje', 'Polje-Kolodvor', 'Polje', 'Cesta Na Vevce', 'Vevce'], '13': ['C. Stozice P+R', 'Boziceva', 'Kardeljeva Ploscad', 'Gasilska Brigada', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Dalmatinova', 'Zmajski Most', 'Poljanska', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Pod Golovcem', 'Stepanja Vas', 'Emona', 'Rast', 'Hrusica', 'Cesta V Bizovik', 'Dobrunje', 'Posta Dobrunje', 'Kpl', 'Zadvor', 'Cesta V Zavoglje', 'Krizisce Sostro', 'Sostro'], '21': ['Bericevo', 'Reaktor', 'Sentjakob', 'Belinka', 'Nadgorica', 'Jeza', 'Zasavska', 'Os Maksa Pecarja', 'Pot V Hrastovec', 'Pot V Smrecje', 'Polanskova', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica'], '22': ['Fuzine P+R', 'Rusjanov Trg', 'Preglov Trg', 'Brodarjev Trg', 'Pot Na Fuzine', 'Kajuhova', 'Tovorni Kolodvor', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Astra', 'Samova', 'Drenikova', 'Kino Siska', 'Sisenska', 'Kneza Koclja', 'Bratov Ucakar', 'Koseze', 'Bratov Babnik', 'Spar', 'Kamna Gorica'], '24': ['Btc-Atlantis', 'Btc-Merkur', 'Btc-Emporium', 'Tovorni Kolodvor', 'Ob Sotocju', 'Kodeljevo', 'Stepanja Vas', 'Bilecanska', 'Krozna Pot', 'Hrusevska', 'Bizovik', 'Dobrunjska C.', 'Dobrunje-2', 'Pod Urhom', 'Zadvor-2', 'Os Sostro', 'Krizisce Sostro', 'Cesta V Zavoglje', 'Zadvor', 'Vevce Papirnica', 'Vevce'], '27': ['Letaliska', 'Leskoskova', 'Btc-Emporium', 'Btc-Merkur', 'Btc-Kolosej', 'Btc-Trznica', 'Btc-Uprava', 'Kodrova', 'Jarse', 'Sola Jarse', 'Srediska', 'Viadukt', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Orlova', 'Izanska', 'Galjevica', 'Golouhova', 'Mihov Stradon', 'Jurckova', 'Bobrova', 'Ns Rudnik']}
                ),
            ]
            for ime, datoteka, slovar in primeri:
                with Check.in_file(ime, datoteka):
                    if not Check.equal(f'linije("{ime}")', slovar):
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
        ] = "eyJwYXJ0Ijo0MDE5NSwidXNlciI6MTE0MjJ9:1wW8ed:7w1r78Xdsduba8vcNppxC1jVSE1ggWw0H73GtOpm3Z4"
        try:
            primeri = [
                (
                    'linije_test_pregledno.txt',
                    {'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'], '1A': ['Park', 'Trg', 'Gledalisce'], '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']},
                    ['1: Sodisce -> Knjiznica -> Trg -> Park', '1A: Park -> Trg -> Gledalisce', '2: Trgovina -> Muzej -> Sola -> Gledalisce']
                ),
                (
                    'linije_lpp_pregledno.txt',
                    {'1': ['D. Most P+R', 'Zgornji Log', 'Cesta V Gorice', 'Mestni Log', 'Tbilisijska', 'Koprska', 'Krimska', 'Gerbiceva', 'Jadranska', 'Hajdrihova', 'Tobacna', 'Askerceva', 'Drama', 'Posta', 'Ajdovscina', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Kino Siska', 'Remiza', 'Aleja', 'Kompas', 'Dravlje', 'Trata', 'Prusnikova', 'Podgora', 'Sentvid', 'Vizmarje', 'Stanezice P+R'], '2': ['Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Roziceva', 'Kavciceva', 'Tovorni Kolodvor', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Ambrozev Trg', 'Poljanska', 'Lutkovno Gl.', 'Gornji Trg', 'Krizanke', 'Drama', 'Posta', 'Ajdovscina', 'Bavarski Dvor', 'Kolodvor', 'Friskovec', 'Viadukt', 'Savsko Naselje', 'Zale', 'Pokopaliska', 'Zelena Jama'], '3': ['Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik'], '3B': ['Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica Obr.'], '3G': ['Zelezna', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Strelisce', 'Rakovnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica', 'Skofljica Javornik', 'Reber Pri Skofljici', 'Spilar', 'Mali Vrh', 'Razdrto', 'Smarje', 'Sap', 'Cikava', 'Brvace', 'Stara Posta', 'Pod Gozdom', 'Adamicev Spomenik', 'Ljubljanska', 'Os Brinje', 'Kongo', 'Dom Starejsih', 'Dom Obrtnikov', 'Vodicar', 'Krpan', 'Mrzle Njive', 'Grosuplje'], '5': ['Podutik', 'Murkova', 'Omersova', 'Pod Kamno Gorico', 'Draveljska Gmajna', 'Koseze', 'Bratov Ucakar', 'Kneza Koclja', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Dalmatinova', 'Ilirska', 'Hrvatski Trg', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Glonarjeva', 'Jana Husa', 'Kodeljevo', 'Stepanja Vas', 'Emona', 'Nusdorferjeva', 'Stepanjsko Nas.'], '6': ['Crnuce', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'D. Most P+R'], '6B': ['Zelezna', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'Podvozna Pot', 'Dolgi Most Rotar', 'Kozarje', 'Na Gmajnici', 'Radna', 'Brezovica Posta', 'Solska', 'Japelj', 'Erbeznik', 'Mosticek', 'Notranje Gorice'], '7': ['Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Na Jami', 'Bolnica P. Drzaja', 'Zgornja Siska', 'Trznica Koseze', 'Cebelarska', 'Plesiceva', 'Andreja Bitenca', 'Przanec', 'Przan'], '8': ['Brod', 'Martinova', 'Tabor', 'Na Klancu', 'Kosmaceva', 'Sentvid', 'Podgora', 'Prusnikova', 'Imp', 'Tehnounion', 'Ljubljanske Brigade', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Bavarski Dvor', 'Razstavisce', 'Astra', 'Stadion', 'Mercator', 'Amzs', 'Smelt', 'Stozice', 'Ruski Car', 'Stara Jezica', 'Jezica', 'Sava', 'Elma', 'Slandrova', 'Obrtna Cona', 'Cesta Na Brod', 'Slovenijales', 'Brnciceva'], '9': ['Stepanjsko Nas.', 'Nusdorferjeva', 'Emona', 'Stepanja Vas', 'Kodeljevo', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Poliklinika', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Mirje', 'Ziherlova', 'Murgle', 'Barje P+R'], '11': ['Jezica P+R', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Streliska', 'Cukrarna', 'Klinicni Center', 'Bolnica', 'Trznica Moste', 'Zaloska', 'Pot Na Fuzine', 'Archinetova', 'Osenjakova', 'Chengdujska', 'Studenec', 'Polje', 'Cesta Na Vevce', 'Kaseljska', 'Petrol', 'Silos', 'Center Zalog', 'Zeleni Gaj', 'Agrokombinatska', 'Zalog'], '12': ['Zelezna', 'Bezigrad', 'Razstavisce', 'Kolodvor', 'Friskovec', 'Viadukt', 'Srediska', 'Flajsmanova', 'Sola Jarse', 'Jarse', 'Kodrova', 'Zito', 'Hrastje', 'Sneberje', 'Trbeze', 'Zadobrova', 'Novo Polje', 'Polje-Kolodvor', 'Polje', 'Cesta Na Vevce', 'Vevce'], '13': ['C. Stozice P+R', 'Boziceva', 'Kardeljeva Ploscad', 'Gasilska Brigada', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Dalmatinova', 'Zmajski Most', 'Poljanska', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Pod Golovcem', 'Stepanja Vas', 'Emona', 'Rast', 'Hrusica', 'Cesta V Bizovik', 'Dobrunje', 'Posta Dobrunje', 'Kpl', 'Zadvor', 'Cesta V Zavoglje', 'Krizisce Sostro', 'Sostro'], '21': ['Bericevo', 'Reaktor', 'Sentjakob', 'Belinka', 'Nadgorica', 'Jeza', 'Zasavska', 'Os Maksa Pecarja', 'Pot V Hrastovec', 'Pot V Smrecje', 'Polanskova', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica'], '22': ['Fuzine P+R', 'Rusjanov Trg', 'Preglov Trg', 'Brodarjev Trg', 'Pot Na Fuzine', 'Kajuhova', 'Tovorni Kolodvor', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Astra', 'Samova', 'Drenikova', 'Kino Siska', 'Sisenska', 'Kneza Koclja', 'Bratov Ucakar', 'Koseze', 'Bratov Babnik', 'Spar', 'Kamna Gorica'], '24': ['Btc-Atlantis', 'Btc-Merkur', 'Btc-Emporium', 'Tovorni Kolodvor', 'Ob Sotocju', 'Kodeljevo', 'Stepanja Vas', 'Bilecanska', 'Krozna Pot', 'Hrusevska', 'Bizovik', 'Dobrunjska C.', 'Dobrunje-2', 'Pod Urhom', 'Zadvor-2', 'Os Sostro', 'Krizisce Sostro', 'Cesta V Zavoglje', 'Zadvor', 'Vevce Papirnica', 'Vevce'], '27': ['Letaliska', 'Leskoskova', 'Btc-Emporium', 'Btc-Merkur', 'Btc-Kolosej', 'Btc-Trznica', 'Btc-Uprava', 'Kodrova', 'Jarse', 'Sola Jarse', 'Srediska', 'Viadukt', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Orlova', 'Izanska', 'Galjevica', 'Golouhova', 'Mihov Stradon', 'Jurckova', 'Bobrova', 'Ns Rudnik']},
                    ['1: D. Most P+R -> Zgornji Log -> Cesta V Gorice -> Mestni Log -> Tbilisijska -> Koprska -> Krimska -> Gerbiceva -> Jadranska -> Hajdrihova -> Tobacna -> Askerceva -> Drama -> Posta -> Ajdovscina -> Gosposvetska -> Tivoli -> Stara Cerkev -> Kino Siska -> Remiza -> Aleja -> Kompas -> Dravlje -> Trata -> Prusnikova -> Podgora -> Sentvid -> Vizmarje -> Stanezice P+R', '2: Nove Jarse -> Nove Jarse-Smartinska -> Zito -> Kodrova -> Jarse -> Sola Jarse -> Roziceva -> Kavciceva -> Tovorni Kolodvor -> Zaloska -> Trznica Moste -> Bolnica -> Klinicni Center -> Ambrozev Trg -> Poljanska -> Lutkovno Gl. -> Gornji Trg -> Krizanke -> Drama -> Posta -> Ajdovscina -> Bavarski Dvor -> Kolodvor -> Friskovec -> Viadukt -> Savsko Naselje -> Zale -> Pokopaliska -> Zelena Jama', '3: Litostroj -> Kovinarska -> Litostrojska -> Slovenija Avto -> Kino Siska -> Stara Cerkev -> Tivoli -> Gosposvetska -> Ajdovscina -> Konzorcij -> Drama -> Krizanke -> Gornji Trg -> Privoz -> Strelisce -> Rakovnik -> Akademija -> Peruzzijeva -> Gornji Rudnik -> Spodnji Rudnik -> Rudnik', '3B: Litostroj -> Kovinarska -> Litostrojska -> Slovenija Avto -> Kino Siska -> Stara Cerkev -> Tivoli -> Gosposvetska -> Ajdovscina -> Konzorcij -> Drama -> Krizanke -> Gornji Trg -> Privoz -> Strelisce -> Rakovnik -> Akademija -> Peruzzijeva -> Gornji Rudnik -> Spodnji Rudnik -> Rudnik -> Pod Hribom -> Lavrica Pri Malci -> Lavrica -> Skofljica Petkovsek -> Skofljica Zaga -> Skofljica Obr.', '3G: Zelezna -> Bezigrad -> Razstavisce -> Bavarski Dvor -> Ajdovscina -> Konzorcij -> Drama -> Krizanke -> Gornji Trg -> Strelisce -> Rakovnik -> Spodnji Rudnik -> Rudnik -> Pod Hribom -> Lavrica Pri Malci -> Lavrica -> Skofljica Petkovsek -> Skofljica Zaga -> Skofljica -> Skofljica Javornik -> Reber Pri Skofljici -> Spilar -> Mali Vrh -> Razdrto -> Smarje -> Sap -> Cikava -> Brvace -> Stara Posta -> Pod Gozdom -> Adamicev Spomenik -> Ljubljanska -> Os Brinje -> Kongo -> Dom Starejsih -> Dom Obrtnikov -> Vodicar -> Krpan -> Mrzle Njive -> Grosuplje', '5: Podutik -> Murkova -> Omersova -> Pod Kamno Gorico -> Draveljska Gmajna -> Koseze -> Bratov Ucakar -> Kneza Koclja -> Slovenija Avto -> Kino Siska -> Stara Cerkev -> Tivoli -> Gosposvetska -> Dalmatinova -> Ilirska -> Hrvatski Trg -> Ambrozev Trg -> Cukrarna -> Gornje Poljane -> Glonarjeva -> Jana Husa -> Kodeljevo -> Stepanja Vas -> Emona -> Nusdorferjeva -> Stepanjsko Nas.', '6: Crnuce -> Rogovilc -> Kolodvor Crnuce -> Sava -> Jezica -> Stara Jezica -> Ruski Car -> Stozice -> Smelt -> Amzs -> Mercator -> Stadion -> Astra -> Razstavisce -> Bavarski Dvor -> Ajdovscina -> Konzorcij -> Drama -> Askerceva -> Tobacna -> Hajdrihova -> Glince -> Vic -> Bonifacija -> Dolgi Most -> D. Most P+R', '6B: Zelezna -> Bavarski Dvor -> Ajdovscina -> Konzorcij -> Drama -> Askerceva -> Tobacna -> Hajdrihova -> Glince -> Vic -> Bonifacija -> Dolgi Most -> Podvozna Pot -> Dolgi Most Rotar -> Kozarje -> Na Gmajnici -> Radna -> Brezovica Posta -> Solska -> Japelj -> Erbeznik -> Mosticek -> Notranje Gorice', '7: Nove Jarse -> Nove Jarse-Smartinska -> Zito -> Kodrova -> Jarse -> Sola Jarse -> Pokopaliska -> Zale -> Savske Stolpnice -> Prekmurska -> Bezigrad -> Razstavisce -> Bavarski Dvor -> Gosposvetska -> Tivoli -> Stara Cerkev -> Na Jami -> Bolnica P. Drzaja -> Zgornja Siska -> Trznica Koseze -> Cebelarska -> Plesiceva -> Andreja Bitenca -> Przanec -> Przan', '8: Brod -> Martinova -> Tabor -> Na Klancu -> Kosmaceva -> Sentvid -> Podgora -> Prusnikova -> Imp -> Tehnounion -> Ljubljanske Brigade -> Litostrojska -> Slovenija Avto -> Kino Siska -> Stara Cerkev -> Tivoli -> Gosposvetska -> Bavarski Dvor -> Razstavisce -> Astra -> Stadion -> Mercator -> Amzs -> Smelt -> Stozice -> Ruski Car -> Stara Jezica -> Jezica -> Sava -> Elma -> Slandrova -> Obrtna Cona -> Cesta Na Brod -> Slovenijales -> Brnciceva', '9: Stepanjsko Nas. -> Nusdorferjeva -> Emona -> Stepanja Vas -> Kodeljevo -> Zaloska -> Trznica Moste -> Bolnica -> Klinicni Center -> Poliklinika -> Friskovec -> Kolodvor -> Bavarski Dvor -> Ajdovscina -> Konzorcij -> Drama -> Mirje -> Ziherlova -> Murgle -> Barje P+R', '11: Jezica P+R -> Jezica -> Stara Jezica -> Ruski Car -> Stozice -> Smelt -> Amzs -> Mercator -> Stadion -> Astra -> Razstavisce -> Bavarski Dvor -> Ajdovscina -> Konzorcij -> Drama -> Krizanke -> Gornji Trg -> Privoz -> Streliska -> Cukrarna -> Klinicni Center -> Bolnica -> Trznica Moste -> Zaloska -> Pot Na Fuzine -> Archinetova -> Osenjakova -> Chengdujska -> Studenec -> Polje -> Cesta Na Vevce -> Kaseljska -> Petrol -> Silos -> Center Zalog -> Zeleni Gaj -> Agrokombinatska -> Zalog', '12: Zelezna -> Bezigrad -> Razstavisce -> Kolodvor -> Friskovec -> Viadukt -> Srediska -> Flajsmanova -> Sola Jarse -> Jarse -> Kodrova -> Zito -> Hrastje -> Sneberje -> Trbeze -> Zadobrova -> Novo Polje -> Polje-Kolodvor -> Polje -> Cesta Na Vevce -> Vevce', '13: C. Stozice P+R -> Boziceva -> Kardeljeva Ploscad -> Gasilska Brigada -> Bezigrad -> Razstavisce -> Bavarski Dvor -> Dalmatinova -> Zmajski Most -> Poljanska -> Ambrozev Trg -> Cukrarna -> Gornje Poljane -> Pod Golovcem -> Stepanja Vas -> Emona -> Rast -> Hrusica -> Cesta V Bizovik -> Dobrunje -> Posta Dobrunje -> Kpl -> Zadvor -> Cesta V Zavoglje -> Krizisce Sostro -> Sostro', '21: Bericevo -> Reaktor -> Sentjakob -> Belinka -> Nadgorica -> Jeza -> Zasavska -> Os Maksa Pecarja -> Pot V Hrastovec -> Pot V Smrecje -> Polanskova -> Rogovilc -> Kolodvor Crnuce -> Sava -> Jezica', '22: Fuzine P+R -> Rusjanov Trg -> Preglov Trg -> Brodarjev Trg -> Pot Na Fuzine -> Kajuhova -> Tovorni Kolodvor -> Sola Jarse -> Pokopaliska -> Zale -> Savske Stolpnice -> Prekmurska -> Bezigrad -> Astra -> Samova -> Drenikova -> Kino Siska -> Sisenska -> Kneza Koclja -> Bratov Ucakar -> Koseze -> Bratov Babnik -> Spar -> Kamna Gorica', '24: Btc-Atlantis -> Btc-Merkur -> Btc-Emporium -> Tovorni Kolodvor -> Ob Sotocju -> Kodeljevo -> Stepanja Vas -> Bilecanska -> Krozna Pot -> Hrusevska -> Bizovik -> Dobrunjska C. -> Dobrunje-2 -> Pod Urhom -> Zadvor-2 -> Os Sostro -> Krizisce Sostro -> Cesta V Zavoglje -> Zadvor -> Vevce Papirnica -> Vevce', '27: Letaliska -> Leskoskova -> Btc-Emporium -> Btc-Merkur -> Btc-Kolosej -> Btc-Trznica -> Btc-Uprava -> Kodrova -> Jarse -> Sola Jarse -> Srediska -> Viadukt -> Friskovec -> Kolodvor -> Bavarski Dvor -> Ajdovscina -> Konzorcij -> Drama -> Krizanke -> Gornji Trg -> Privoz -> Orlova -> Izanska -> Galjevica -> Golouhova -> Mihov Stradon -> Jurckova -> Bobrova -> Ns Rudnik']
                ),
            ]
            
            for ime, slovar, datoteka in primeri:
                pregledno(slovar, ime)
                if not Check.out_file(ime, datoteka):
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
        ] = "eyJwYXJ0Ijo0MDE5NiwidXNlciI6MTE0MjJ9:1wW8ed:ISWcc5wHkZe4tdOTxSSWnpBTMIniXUBTh-1kDQs2na0"
        try:
            slovar_test = {'1': ['Sodisce', 'Knjiznica', 'Trg', 'Park'], '1A': ['Park', 'Trg', 'Gledalisce'], '2': ['Trgovina', 'Muzej', 'Sola', 'Gledalisce']}
            slovar_lpp = {'1': ['D. Most P+R', 'Zgornji Log', 'Cesta V Gorice', 'Mestni Log', 'Tbilisijska', 'Koprska', 'Krimska', 'Gerbiceva', 'Jadranska', 'Hajdrihova', 'Tobacna', 'Askerceva', 'Drama', 'Posta', 'Ajdovscina', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Kino Siska', 'Remiza', 'Aleja', 'Kompas', 'Dravlje', 'Trata', 'Prusnikova', 'Podgora', 'Sentvid', 'Vizmarje', 'Stanezice P+R'], '2': ['Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Roziceva', 'Kavciceva', 'Tovorni Kolodvor', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Ambrozev Trg', 'Poljanska', 'Lutkovno Gl.', 'Gornji Trg', 'Krizanke', 'Drama', 'Posta', 'Ajdovscina', 'Bavarski Dvor', 'Kolodvor', 'Friskovec', 'Viadukt', 'Savsko Naselje', 'Zale', 'Pokopaliska', 'Zelena Jama'], '3': ['Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik'], '3B': ['Litostroj', 'Kovinarska', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Strelisce', 'Rakovnik', 'Akademija', 'Peruzzijeva', 'Gornji Rudnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica Obr.'], '3G': ['Zelezna', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Strelisce', 'Rakovnik', 'Spodnji Rudnik', 'Rudnik', 'Pod Hribom', 'Lavrica Pri Malci', 'Lavrica', 'Skofljica Petkovsek', 'Skofljica Zaga', 'Skofljica', 'Skofljica Javornik', 'Reber Pri Skofljici', 'Spilar', 'Mali Vrh', 'Razdrto', 'Smarje', 'Sap', 'Cikava', 'Brvace', 'Stara Posta', 'Pod Gozdom', 'Adamicev Spomenik', 'Ljubljanska', 'Os Brinje', 'Kongo', 'Dom Starejsih', 'Dom Obrtnikov', 'Vodicar', 'Krpan', 'Mrzle Njive', 'Grosuplje'], '5': ['Podutik', 'Murkova', 'Omersova', 'Pod Kamno Gorico', 'Draveljska Gmajna', 'Koseze', 'Bratov Ucakar', 'Kneza Koclja', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Dalmatinova', 'Ilirska', 'Hrvatski Trg', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Glonarjeva', 'Jana Husa', 'Kodeljevo', 'Stepanja Vas', 'Emona', 'Nusdorferjeva', 'Stepanjsko Nas.'], '6': ['Crnuce', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'D. Most P+R'], '6B': ['Zelezna', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Askerceva', 'Tobacna', 'Hajdrihova', 'Glince', 'Vic', 'Bonifacija', 'Dolgi Most', 'Podvozna Pot', 'Dolgi Most Rotar', 'Kozarje', 'Na Gmajnici', 'Radna', 'Brezovica Posta', 'Solska', 'Japelj', 'Erbeznik', 'Mosticek', 'Notranje Gorice'], '7': ['Nove Jarse', 'Nove Jarse-Smartinska', 'Zito', 'Kodrova', 'Jarse', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Gosposvetska', 'Tivoli', 'Stara Cerkev', 'Na Jami', 'Bolnica P. Drzaja', 'Zgornja Siska', 'Trznica Koseze', 'Cebelarska', 'Plesiceva', 'Andreja Bitenca', 'Przanec', 'Przan'], '8': ['Brod', 'Martinova', 'Tabor', 'Na Klancu', 'Kosmaceva', 'Sentvid', 'Podgora', 'Prusnikova', 'Imp', 'Tehnounion', 'Ljubljanske Brigade', 'Litostrojska', 'Slovenija Avto', 'Kino Siska', 'Stara Cerkev', 'Tivoli', 'Gosposvetska', 'Bavarski Dvor', 'Razstavisce', 'Astra', 'Stadion', 'Mercator', 'Amzs', 'Smelt', 'Stozice', 'Ruski Car', 'Stara Jezica', 'Jezica', 'Sava', 'Elma', 'Slandrova', 'Obrtna Cona', 'Cesta Na Brod', 'Slovenijales', 'Brnciceva'], '9': ['Stepanjsko Nas.', 'Nusdorferjeva', 'Emona', 'Stepanja Vas', 'Kodeljevo', 'Zaloska', 'Trznica Moste', 'Bolnica', 'Klinicni Center', 'Poliklinika', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Mirje', 'Ziherlova', 'Murgle', 'Barje P+R'], '11': ['Jezica P+R', 'Jezica', 'Stara Jezica', 'Ruski Car', 'Stozice', 'Smelt', 'Amzs', 'Mercator', 'Stadion', 'Astra', 'Razstavisce', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Streliska', 'Cukrarna', 'Klinicni Center', 'Bolnica', 'Trznica Moste', 'Zaloska', 'Pot Na Fuzine', 'Archinetova', 'Osenjakova', 'Chengdujska', 'Studenec', 'Polje', 'Cesta Na Vevce', 'Kaseljska', 'Petrol', 'Silos', 'Center Zalog', 'Zeleni Gaj', 'Agrokombinatska', 'Zalog'], '12': ['Zelezna', 'Bezigrad', 'Razstavisce', 'Kolodvor', 'Friskovec', 'Viadukt', 'Srediska', 'Flajsmanova', 'Sola Jarse', 'Jarse', 'Kodrova', 'Zito', 'Hrastje', 'Sneberje', 'Trbeze', 'Zadobrova', 'Novo Polje', 'Polje-Kolodvor', 'Polje', 'Cesta Na Vevce', 'Vevce'], '13': ['C. Stozice P+R', 'Boziceva', 'Kardeljeva Ploscad', 'Gasilska Brigada', 'Bezigrad', 'Razstavisce', 'Bavarski Dvor', 'Dalmatinova', 'Zmajski Most', 'Poljanska', 'Ambrozev Trg', 'Cukrarna', 'Gornje Poljane', 'Pod Golovcem', 'Stepanja Vas', 'Emona', 'Rast', 'Hrusica', 'Cesta V Bizovik', 'Dobrunje', 'Posta Dobrunje', 'Kpl', 'Zadvor', 'Cesta V Zavoglje', 'Krizisce Sostro', 'Sostro'], '21': ['Bericevo', 'Reaktor', 'Sentjakob', 'Belinka', 'Nadgorica', 'Jeza', 'Zasavska', 'Os Maksa Pecarja', 'Pot V Hrastovec', 'Pot V Smrecje', 'Polanskova', 'Rogovilc', 'Kolodvor Crnuce', 'Sava', 'Jezica'], '22': ['Fuzine P+R', 'Rusjanov Trg', 'Preglov Trg', 'Brodarjev Trg', 'Pot Na Fuzine', 'Kajuhova', 'Tovorni Kolodvor', 'Sola Jarse', 'Pokopaliska', 'Zale', 'Savske Stolpnice', 'Prekmurska', 'Bezigrad', 'Astra', 'Samova', 'Drenikova', 'Kino Siska', 'Sisenska', 'Kneza Koclja', 'Bratov Ucakar', 'Koseze', 'Bratov Babnik', 'Spar', 'Kamna Gorica'], '24': ['Btc-Atlantis', 'Btc-Merkur', 'Btc-Emporium', 'Tovorni Kolodvor', 'Ob Sotocju', 'Kodeljevo', 'Stepanja Vas', 'Bilecanska', 'Krozna Pot', 'Hrusevska', 'Bizovik', 'Dobrunjska C.', 'Dobrunje-2', 'Pod Urhom', 'Zadvor-2', 'Os Sostro', 'Krizisce Sostro', 'Cesta V Zavoglje', 'Zadvor', 'Vevce Papirnica', 'Vevce'], '27': ['Letaliska', 'Leskoskova', 'Btc-Emporium', 'Btc-Merkur', 'Btc-Kolosej', 'Btc-Trznica', 'Btc-Uprava', 'Kodrova', 'Jarse', 'Sola Jarse', 'Srediska', 'Viadukt', 'Friskovec', 'Kolodvor', 'Bavarski Dvor', 'Ajdovscina', 'Konzorcij', 'Drama', 'Krizanke', 'Gornji Trg', 'Privoz', 'Orlova', 'Izanska', 'Galjevica', 'Golouhova', 'Mihov Stradon', 'Jurckova', 'Bobrova', 'Ns Rudnik']}
            primeri = [
                (slovar_test, 'Trgovina', 'Trg', True),
                (slovar_test, 'Sodisce', 'Knjiznica', True),
                (slovar_test, 'Sodisce', 'Sola', False),
                (slovar_test, 'Trg', 'Aaaaaa', None),
                (slovar_lpp, 'Hajdrihova', 'Btc-Kolosej', True),
                (slovar_lpp, 'Hajdrihova', 'Ajdovscina', True),
                (slovar_lpp, 'Jadranska', 'C. Stozice P+R', False),
                (slovar_lpp, 'Haha', 'Aaaaaa', None),
            ]
            for slovar, zacetna, koncna, rezultat in primeri:
                if not Check.equal(f'obstaja_povezava({slovar}, "{zacetna}", "{koncna}")', rezultat):
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
